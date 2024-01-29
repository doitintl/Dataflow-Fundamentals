import argparse
import json
import logging

import apache_beam as beam
from apache_beam import io, WindowInto
from apache_beam.io import fileio
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.transforms.trigger import AfterWatermark, AccumulationMode
from apache_beam.transforms.window import FixedWindows, SlidingWindows


class ApplyKey(beam.DoFn):
    """
    Apply Key DoFn change an element in a Key Value pair.
    The Key is the Track ID and the values are all the properties in the element.
    """
    def process(self, element):
        data = json.loads(element.decode('utf-8'))
        yield data["TrackID"], data


class CountActions(beam.DoFn):
    """
    DoFn that counts the number of time the action PLAY is executed on for a specific track.
    """
    def process(self, element, *args, **kwargs):
        number_of_plays = 0
        key, value = element
        for item in value:
            if int(item['Action']) == 1:
                number_of_plays += 1
        yield f"song: {key} number_of_playsL {number_of_plays}"


def run(argv=None):
    """Main entry point; defines and runs the AudioPlayer pipeline."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--input_subscription',
        required= True,
        help='Input file to process.')
    parser.add_argument(
        '--output',
        dest='output',
        default='',
        help='Output file to write results to.')
    known_args, pipeline_args = parser.parse_known_args(argv)

    pipeline_options = PipelineOptions(pipeline_args)

    # The pipeline will be run on exiting the with block.
    with beam.Pipeline(options=pipeline_options) as p:
        # Read the CSV file into a PCollection.
        lines = (p
                 | "Read from Pub/Sub" >> io.ReadFromPubSub(subscription=known_args.input_subscription)
                 | "KV" >> beam.ParDo(ApplyKey())
        )

        results_fixed_window = (
                lines
                | "Fixed Window" >> WindowInto(FixedWindows(5*60),
                                         trigger=AfterWatermark(),
                                         accumulation_mode=AccumulationMode.ACCUMULATING)
                | 'Fixed Group And Sum' >> beam.GroupByKey()
                | 'Fixed Count Actions' >> beam.ParDo(CountActions())
        )

        results_sliding_window = (
                lines
                | "Sliding Window" >> WindowInto(SlidingWindows(5*60, 60),
                                         trigger=AfterWatermark(),
                                         accumulation_mode=AccumulationMode.ACCUMULATING)
                | 'Sliding GroupAndSum' >> beam.GroupByKey()
                | 'Sliding Count Actions' >> beam.ParDo(CountActions())
        )
        pathFix= known_args.output + "Fixed-output.txt"
        pathSliding=  known_args.output + "Sliding-output.txt"
        results_fixed_window | 'Write Fix' >> fileio.WriteToFiles(path=pathFix)
        results_sliding_window | 'Write Sliding' >> fileio.WriteToFiles(path=pathSliding)


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    run()
