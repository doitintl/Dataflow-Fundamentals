# Dataflow Fundamentals LAB-01

## Batch Pipeline

[![Context](https://img.shields.io/badge/Dataflow%20Fundamentals-1-blue.svg)](#)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## Introduction

In this lab we will create our first Batch dataflow pipeline.
The goal of this lab is to understand and get familiar with the Apache Beam basics and how to use them.
The data we are using is fake and automatic generated. It represents data from an online music streaming services that tracks when a user hit the play start and stop button.
With our first pipeline we will calculate how often the users hits the play button for each song(Note there are multiple actions in the dataset).

## Lab Structure

In this lab folder is one folder with sample data named (drum roll) sampledata. As the name described in this folder contains the data file we are going to use in this lab.
There are also 2 python files in the lab. pipeline-lab1.py and pipeline-lab1-complete.py. 
1. pipeline-lab1.py is the file the start of the lab. you can use to create the pipeline. 
2. pipeline-lab1-complete.py contains the(a possible) solution for this lab. Only check this file when you are stuck. 

In the pipeline-lab1.py you can commands that splits this lab in smaller steps.
At the end of this file you can the find links pointing to the official beam documentation


## Run the pipeline with direct runner

1. You can run the pipeline with the following command:

```bash
 python pipeline-lab1.py --output=output.txt
```
or
```bash
 python3 pipeline-lab1.py --output=output.txt
```

## Run the pipeline on dataflow

1. First we need to create an Input and an output bucket and copy the data file from sample data in the input bucket.
2. You can also run the pipeline on dataflow with this command: (replace the DATAFLOW_REGION,BUCKET_NAME and PROJECT_ID variables)

```bash
python -m pipeline-lab1.py \
    --region DATAFLOW_REGION \
    --input gs://BUCKET_NAME/data.txt \
    --output gs://BUCKET_NAME/results/outputs \
    --runner DataflowRunner \
    --project PROJECT_ID \
    --temp_location gs://BUCKET_NAME/tmp/
```

## Links

- https://beam.apache.org/documentation/programming-guide/#creating-a-pipeline
- https://beam.apache.org/documentation/programming-guide/#pardo
- https://beam.apache.org/documentation/programming-guide/#groupbykey
- https://beam.apache.org/documentation/programming-guide/#pipeline-io
