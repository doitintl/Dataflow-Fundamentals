import argparse
import logging

import apache_beam as beam
from apache_beam.io import ReadFromCsv
from apache_beam.io import WriteToText
from apache_beam.options.pipeline_options import PipelineOptions


class ApplyKey(beam.DoFn):
    """
    Apply Key DoFn change an element in a Key Value pair.
    The Key is the Track ID and the values are all the properties in the element.
    """
    def process(self, element):
        yield element.TrackID, {"UserID": element.UserID, "TrackID": element.TrackID, "Action": element.Action,
                                "Duration": element.Duration}


class CountActions(beam.DoFn):
    """
    DoFn that counts the number of time the action PLAY is executed on for a specific track.
    """
    def process(self, element, *args, **kwargs):
        number_of_plays = 0
        key, value = element
        for item in value:
            if item['Action'] == 1:
                number_of_plays += 1
        yield key, number_of_plays


def run(argv=None):
    """Main entry point; defines and runs the AudioPlayer pipeline."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--input',
        dest='input',
        default='sampledata/data.csv',
        help='Input file to process.')
    parser.add_argument(
        '--output',
        dest='output',
        default='ouput.txt',
        help='Output file to write results to.')
    known_args, pipeline_args = parser.parse_known_args(argv)

    pipeline_options = PipelineOptions(pipeline_args)

    # The pipeline will be run on exiting the with block.
    with beam.Pipeline(options=pipeline_options) as p:
        # Read the CSV file into a PCollection.
        lines = p | 'Read' >> ReadFromCsv(path=known_args.input, header=0)

        counts = (
                lines
                | 'Split' >> beam.ParDo(ApplyKey())
                | 'GroupAndSum' >> beam.GroupByKey()
                | 'Count Actions' >> beam.ParDo(CountActions())
        )

        counts | 'Write' >> WriteToText(known_args.output)


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    run()
