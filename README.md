

<div align="center">
    <h1> Flask Factory </h1>
    <h4>Flask App Template with Factory Pattern Architecture</h4>
</div>


<div align="center">
    <a href="https://github.com/rednafi/flask-factory/issues"><img src="https://img.shields.io/github/issues/rednafi/pysanity" /></a>
    <a href="https://github.com/rednafi/flask-factory/network/members"><img src="https://img.shields.io/github/forks/rednafi/flask-factory" /></a>
    <a href="https://github.com/rednafi/flask-factory/stargazers"><img src="https://img.shields.io/github/stars/rednafi/flask-factory" /></a>
    <a href="https://github.com/rednafi/flask-factory/stargazers"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" /></a>
    <a href="https://twitter.com/intent/retweet?tweet_id=1222434622442594304"><img src="https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com%2Frednafi%2Fpysanity" /></a>

</div>

<p>&nbsp;</p>

## Architecture

Directory tree for serving multiple packages as Flask API with multiple endpoints

```.
├── app
│   ├── api_a
│   │   ├── __init__.py
│   │   ├── module_main.py
│   │   ├── module_sub.py
│   │   └── views.py
│   ├── api_b
│   │   ├── __init__.py
│   │   ├── module_main.py
│   │   ├── module_sub.py
│   │   └── views.py
│   ├── __init__.py
│   └── tests
│       ├── __init__.py
│       └── test_api.py
├── docker-compose.yml
├── Dockerfile
├── flask_run.py
├── README.md
├── requirements.txt
└── settings.toml

4 directories, 17 files
```

## Setup

* Install [docker](https://docs.docker.com/install/) and [docker-compose](https://docs.docker.com/compose/install/) on your machine

* Clone the repository & `cd` to the root directory

## Run the App Locally Without Docker

* Create and activate python virtual environment via:

    ```bash
    python3.8 -m venv venv
    source venv/bin/activate
    ```

* Install the dependencies via:

    ```bash
    pip install -r requirements.txt
    ```

* Go to the environment file (`.env`),
uncomment `ENV_FOR_DYNACONF="development"` and comment out `ENV_FOR_DYNACONF="production"` variable.

* Run the app by executing the `flask_run.py` file:

    ```bash
    python flask_run.py
    ```

    The app will run locally in port `5000`.

## Run the App in a Docker Container

* Go to the environment file (`.env`),
uncomment `ENV_FOR_DYNACONF="production"` and comment out `ENV_FOR_DYNACONF="development"` variable.

* Run the docker container

    ```bash
    docker-compose up
    ```

    The app will run locally in port `5000`.


## Hit the API

While the above container is running, the API can be accessed via any API development client like [Postman](https://www.getpostman.com/).

```
# this shoud go with your header

x-api-key : ABCD1234

# add your desired integer/float, replacing the <number>

base-link : localhoast:5000/api-a/<number>
```

Once you hit the api, you should see something like this (you numbers may be different since we are returning random numbers each time):

 ```bash
 {
    "random_first": 111,
    "random_second": 82,
    "seed": 123
}
 ```

## Stop the Container

Run

```bash
docker-compose down
```

## Remarks
This template is developed and tested on

- Python 3.8
- Docker version 19.03
- docker-compose 1.25.4
- Ubuntu 18.04 LTS
