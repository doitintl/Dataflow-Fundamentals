import argparse
import logging

import apache_beam as beam
from apache_beam.io import ReadFromCsv
from apache_beam.io import WriteToText
from apache_beam.options.pipeline_options import PipelineOptions


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

        results = (
                # Step 1: Create Pardo that yield a Key, Value pair.
                #         The key needs to be the track id and value the dict object

                # Step 2: Group all the records based on TrackId(Key)

                # Step 3: Create an Pardo That counts the amount op plays(Action 1)
        )

        results | 'Write' >> WriteToText(known_args.output)


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    run()
