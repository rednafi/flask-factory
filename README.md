# Flask Template

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/rednafi/protomate/blob/master/LICENSE) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)
[![twitter](https://img.shields.io/twitter/url/https/home?style=social)](https://twitter.com)


## Directory Tree
Directory tree for serving multiple packages as Flask API with multiple endpoints

```
.
├── app
│   ├── api_1
│   │   ├── __init__.py
│   │   ├── module_1.py
│   │   ├── module_main.py
│   │   └── views.py
│   ├── api_2
│   │   ├── __init__.py
│   │   ├── module_1.py
│   │   ├── module_main.py
│   │   └── views.py
│   ├── __init__.py
│   └── tests
│       └── test_api.py
├── docker-compose.yml
├── Dockerfile
├── README.md
├── requirements.txt
├── run.py
└── rushfile.yml

4 directories, 16 files
```

## Instructions

* Clone the repository & `cd` to the root directory

### Run the Flask App Locally Without Docker
* Go to the environment file (`.env`),
uncomment `RUNTIME_ENVIRONMENT='DEVELOPMENT'` and comment out `RUNTIME_ENVIRONMENT='PRODUCTION'` variable.

* Run the app:
    ```
    $ pip3 install rush-cli
    $ rush offline_run
    ```
    The app will run locally in port `5000`.

### Run the Flask App Locally as a Docker Container

* Go to the environment file (.env), uncomment RUNTIME_ENVIRONMENT='PRODUCTION' and comment out RUNTIME_ENVIRONMENT='DEVELOPMENT' variable.

* Run the docker container
    ```
    rush docker_deploy
    ```


### Hit the API

While the above container is running, the API can be accessed via any API development client like [Postman](https://www.getpostman.com/).

```
x-api-key : ABCD1234

# add your desired integer/float, replacing the <number>

base-link : localhoast:5000/api_1/<number>
```
Once you hit the api, you should see something like this (you numbers may be different since we are returning random numbers each time):

 ```bash
 {
    "random_first": 111,
    "random_second": 82,
    "seed": 123
}
 ```

### Stop and Delete the Container After Experimentation

* Check the docker process:

    ```bash
    $ sudo docker ps
    ```
    This should show all the running containers.

    ![Imgur](https://imgur.com/SUHI5pb.png)

* Stop the docker container:

    ```bash
    $ sudo docker stop <CONTAINER_ID>
    ```
* Delete the docker container

    ```bash
    $ sudo docker rm <CONTAINER_ID>
    ```
* Check the docker image:

  ```bash
  $ sudo docker images
  ```
  This should show all the docker images.

  ![Imgur](https://imgur.com/oP4pZpL.png)


* Delete the image:

  ```bash
  $ sudo docker rmi <IMAGE_ID>
  ```

Check the [Dockerfile](https://github.com/rednafi/flask-tmplt/blob/master/Dockerfile), [docker-compose.yml](https://github.com/rednafi/flask-tmplt/blob/master/docker-compose.yml) and [Bakefile](https://github.com/rednafi/flask-tmplt/blob/master/Bakefile) to follow how the deployment works.
