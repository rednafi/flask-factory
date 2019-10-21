# Flask Template

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/rednafi/protomate/blob/master/LICENSE) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)
[![twitter](https://img.shields.io/twitter/url/https/home?style=social)](https://twitter.com)


## Directory Tree
Directory tree for serving multiple packages as Flask API with multiple endpoints

```
.
├──app/
|   ├── api_1
|   │   ├── __init__.py
|   │   ├── module_1.py
|   │   ├── module_main.py
|   │   └── views.py
|   ├── api_2
|   │   ├── __init__.py
|   │   ├── module_1.py
|   │   ├── module_main.py
|   │   └── views.py
|   └── __init__.py
├── .dockerignore
├── .env
├── .gitignore
├── deploy.sh
├── requirements.txt
└── run.py
```

## Instructions

### Run the API Directly
To run the app, go to the root directory and run:

```
$ python3 -m venv venv
$ source activate venv/bin/activate
$ pip install -r requirements.txt
$ python run.py
```
The app will run locally in port `5000`.

### Run As a Docker Container

* Build the docker container:

    ```bash
    $ sudo docker build . --tag=flask_template
    ```

* Run the docker container in attached terminal

    ```bash
    $ sudo docker run -p 5000:5000 flask_template
    ```

    or, run the container in detached mode

    ```bash
    $ sudo docker run -d -p 5000:5000 flask_template
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

### Deploy in a Server
For deploying the container in a server, make sure you have
    * Setup and configured the server properly
    * Have nginx installed
    * Have gunicorn installed
    * Configured a server block in proper way
To deploy the app in a server, first test the app in the server:

```bash
$ chmod +x deploy.sh
$ ./deploy.sh
```

If it runs without errors, run the following command to deploy the app in daemon mode.

```bash
$ ./deploy.sh -d
```
Check the [Dockerfile](https://github.com/rednafi/flask-tmplt/blob/master/Dockerfile) and [deploy.sh](https://github.com/rednafi/flask-tmplt/blob/master/deploy.sh) to follow how the deployment works.
