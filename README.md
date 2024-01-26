# Dataflow-Fundamentals

[![Context](https://img.shields.io/badge/Dataflow%20Fundamentals-1-blue.svg)](#)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)


## Introduction

In this two-day workshop we will explore what Apache Beam en Dataflow is and how you can use it. 
The First day we are mainly focussing on understanding the mechanics. We will create our one Batch Pipeline. 
The second day we will dive deeper in streaming pipelines and the different mechanics Beam has to deal with the challenges.



## Repository Structure

``` 
[root]
  |
  └ Lab-1-Lab-1-batch-pipeline     | We create our own Batch Pipeline. 
  └ Lab-2-windowing                | We create our Batch Pipeline. 
  |--------------------------------|-----------------------------------------------------------------------------------
```

## Available Labs

| Lab/Folder                       | Description                                                   |
|----------------------------------|---------------------------------------------------------------|
| [df-lab-01](./Lab-1-batch-pipeline) | Batch pipeline that calculates the how often a song is played |
| [df-lab-02](./Lab-2-windowing)             | UNDER CONTRUCTION                                             |
| ..                               | ..                                                            |
                                   |


## Core Requirements

To run the pipelines with Dataflow you need to have a GCP project with billing enabled/


### Required Tools/Packages

- Python 3 
- pip

### Optional Tools/Packages

- `vscode` [installation](https://code.visualstudio.com/download) installation guide
- `pyCharm` [installation](https://www.jetbrains.com/help/pycharm/installation-guide.html) installation guide
- `gCloud` [installation](https://cloud.google.com/sdk/docs/install) installation guide


## Labs preperation Preparation

The preparation of your local environment is one of the first steps to handle all of our labs and is the basis for all our further activity using the local development environment of all participants. 

1. **Clone Repository**

   Please make sure that work with the latest main-branch version of our labs-repository. If there are changes to the kernel repository during the workshop, you can save the current local change state with `git stash` and get the new state with `git pull`.

   ```bash
   $ # sudo mkdir -p /opt/workshop ; cd /opt/workshop
   $ git clone https://github.com/doitintl/Dataflow-Fundamentals.git 
   $ cd Dataflow-Fundamentals ;
   ```

2. **GCP Credential Configuration (optional)** 

   Set default GCP credentials and set project
   ```ini
   gcloud config init
   bloud config set project <YOUR PROJECT>
   ```

3. **Installation requirements**

   Make sure you are using python 3 and have installed pip.

   ```bash
   $ pip install -r requirements.txt
   ```

4. **INIT/RUN** Lab

   _Go to the corresponding labs sub-directory and follow the corresponding instructions in the documentation stored there!s

## Links

- https://beam.apache.org/documentation/programming-guide/
- https://tour.beam.apache.org/
- https://beam.apache.org/get-started/resources/learning-resources/#getting-started
- 

## License

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

See [LICENSE](LICENSE) for full details.

    Licensed to the Apache Software Foundation (ASF) under one
    or more contributor license agreements.  See the NOTICE file
    distributed with this work for additional information
    regarding copyright ownership.  The ASF licenses this file
    to you under the Apache License, Version 2.0 (the
    "License"); you may not use this file except in compliance
    with the License.  You may obtain a copy of the License at

      https://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing,
    software distributed under the License is distributed on an
    "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.

## Copyright

Copyright © 2024 DoiT International