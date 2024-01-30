# Dataflow Fundamentals LAB-02

## Batch Pipeline

[![Context](https://img.shields.io/badge/Dataflow%20Fundamentals-1-blue.svg)](#)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## Introduction

In this lab we will create a streaming pipeline that includes windowing.
The goal of this lab is to get familiar with the Apache Beam windowing mechanism.
The data we are using is fake and automatic generated. It represents data from an online music streaming services that tracks when a user hit the play start and stop button.
With this pipeline we will calculate how often the users hits the play button for each song in a specific time window(Note there are multiple actions in the dataset).

## Lab Structure

In this lab folder is one folder with sample data named (drum roll) sampledata. As the name described in this folder contains the data file we are going to use in this lab.
There are also 2 python files in the lab. pipeline-lab1.py and pipeline-lab1-complete.py. 
1. dataIngestor.py this script publish data messages to pubsub to simulate the streaming data.
2. pipeline-lab2.py is the file the start of the lab. you can use to create the pipeline. 
3. pipeline-lab2-complete.py contains the(a possible) solution for this lab. Only check this file when you are stuck. 

In the pipeline-lab2.py you can find commands that splits this lab in smaller steps.
At the end of this file you can the find links pointing to the official beam documentation


## Setup the environment

For this lab we are going to use Pub/Sub as an input source.
For using pubsub you need a GCP project with a billing account, or you can use the emulator.

Please follow this link when you want to know how to set up the emulator: https://cloud.google.com/pubsub/docs/emulator

### For GCP
Fist we need to create a pubsub topic named audioPlayer.

```bash 
gcloud pubsub topics create audioPlayer    
```

After we created the topic we need to add the subscription audioPlayerPull.

```bash 
gcloud pubsub subscriptions create audioPlayerPull --topic=audioPlayer
```

### For Emulator

To set up the topic and the subscription you can use this command.
Please note that the emulator must already run.

More info here: https://cloud.google.com/pubsub/docs/emulator#using_the_emulator
```bash 
python subscriber.py PUBSUB_PROJECT_ID create audioPlayer audioPlayerPull
```

## Run the data simulator

In the dataIngester.py File you need to change the project id on line 8
If you have chosen for a different topic name you can modify that on line 9.

To create the pubsub topic you can do that by running this command if you have gcloud installed.
```bash
 gcloud pubsub topics create audioPlayer
```

To create the Subscription you can run the following command
```bash
gcloud pubsub subscriptions create audioPlayerPull --topic=audioPlayer
```

When these are created you can start the script by running.
As long as the script run it wil simulate streaming data.
NOTE: Close this script when you are done with the lab.

```bash
python dataIngestor.py 
```

or 

```bash
python3 dataIngestor.py 
```

## Run the pipeline with direct runner
replace the placeholder ${PROJECT_ID} with your project id.


1. You can run the pipeline with the following command:

```bash
 python pipeline-lab2.py --input_subscription="projects/${PROJECT_ID}/subscriptions/audioPlayerPull" --output=output.txt --streaming
```
or
```bash
 python3 pipeline-lab2.py --input_subscription="projects/${PROJECT_ID}/subscriptions/audioPlayerPull" --output=output.txt --streaming
```

## Run the pipeline on dataflow
replace the placeholder ${PROJECT_ID} with your project id.

1. First we need to create an Input and an output bucket and copy the data file from sample data in the input bucket.
2. You can also run the pipeline on dataflow with this command: (replace the DATAFLOW_REGION,BUCKET_NAME and PROJECT_ID variables)

```bash
python -m pipeline-lab2.py \
    --region DATAFLOW_REGION \
    --input_subscription="projects/${PROJECT_ID}/subscriptions/audioPlayerPull" \
    --output gs://BUCKET_NAME/results/outputs \
    --runner DataflowRunner \
    --project PROJECT_ID \
    --temp_location gs://BUCKET_NAME/tmp/ \
    --streaming
```

## Links

- https://beam.apache.org/documentation/programming-guide/#creating-a-pipeline
- https://beam.apache.org/documentation/programming-guide/#pardo
- https://beam.apache.org/documentation/programming-guide/#groupbykey
- https://beam.apache.org/documentation/programming-guide/#pipeline-io
- https://beam.apache.org/documentation/programming-guide/#windowing
- https://beam.apache.org/documentation/programming-guide/#triggers
- https://beam.apache.org/releases/pydoc/current/apache_beam.io.gcp.pubsub.html
- 
