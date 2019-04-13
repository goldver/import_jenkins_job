Docker service pipeline
========================

This job will create a new Docker service pipeline.

Usage
==================

Jenkins Job: [hhttps://jenkins.<HOST>.com/job/create_job]

The job will requires next inputs:

|  Parameter:    | Description:                           | Example:      |
|:-------------- |:---------------------------------------|:--------------|
| REPO_NAME      | Which repository                       | my_repo       |
| SERVICE_NAME   | Name of Service we want to create      | docker_test   |

python3 export_job.py -r my_repo -s docker_test

Jenkins
<#!/bin/bash -xe>

<cd $WORKSPACE/docker_automation_job>
<python3 export_job.py -r $REPO_NAME -s $SERVICE_NAME>

Contributing
------------
1. Fork the repository on Github
2. Create a named feature branch (like `add_component_x`)
3. Write you change
4. Write tests for your change (if applicable)
5. Run the tests, ensuring they all pass
6. Submit a Pull Request using Github

License and Authors
-------------------

Authors: [Michael Vershinin](mailto:goldver@gmail.com)

Support
-------

[Michael Vershinin](mailto:goldver@gmail.com)


