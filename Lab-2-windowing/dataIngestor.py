import csv
from json import dumps
from google.cloud import pubsub_v1
import random
from time import sleep

# Provide your Google Cloud project ID and Pub/Sub topic name
project_id = '----'
topic_name = 'audioPlayer'

# gcloud pubsub topics create audioPlayer
# gcloud pubsub subscriptions create audioPlayerPull --topic=audioPlayer


# Provide the path to your CSV file
csv_file = './sampledata/data.csv'

batch_settings = pubsub_v1.types.BatchSettings(
    max_messages=10,  # default 100
    max_bytes=1024,  # default 1 MB
    max_latency=1,  # default 10 ms
)

future = []
publisher = pubsub_v1.PublisherClient(batch_settings)


# Resolve the publish future in a separate thread.
def callback(future: pubsub_v1.publisher.futures.Future) -> None:
    message_id = future.result()
    print(message_id)


def publish_to_pubsub(project_id, topic_name, data):
    topic_path = publisher.topic_path(project_id, topic_name)
    try:
        future = publisher.publish(topic_path, dumps(data).encode('utf-8'))
        future.add_done_callback(callback)
    except Exception as e:
        print(e)


def read_csv_and_publish(project_id, topic_name, csv_file):
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file, delimiter=',', quotechar='"')
        fields = next(csv_reader)

        for row in csv_reader:
            data = dict(zip(fields, row))
            sleep(random.uniform(0, 0.3))
            publish_to_pubsub(project_id, topic_name, data)



read_csv_and_publish(project_id, topic_name, csv_file)
