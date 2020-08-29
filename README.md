

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
├── requirements-dev.txt
└── settings.toml

4 directories, 17 files
```

## Setup

* Install [docker](https://docs.docker.com/install/) and [docker-compose](https://docs.docker.com/compose/install/) on your machine

* Clone the repository & `cd` to the root directory

## Run

* Go to the environment file (`.env`),
uncomment `ENV_FOR_DYNACONF="production"` and comment out `ENV_FOR_DYNACONF="development"` variable.

* Run the docker container

    ```bash
    docker-compose up
    ```

    The app will run locally in port `4000`.


## Check the API

While the above container is running, the API can be accessed via any API development client like [Postman](https://www.getpostman.com/).

### With CuRL

Run the following command to test the api with curl. Make sure you're sending `X-Api-Key: 1234ABCD` with the header:

```
curl -H "Accept: application/json" -H "Content-Type: application/json" -H "X-Api-Key: 1234ABCD" http://localhost:4000/api-a/123
```

It should return a response similar to this:

```json
{
    "random_first":16,
    "random_second":73,
    "seed":123
}
```

### With Python (Httpx)

[Httpx](https://github.com/encode/httpx) is a modern and faster alternative to Python's revered [requests](https://github.com/psf/requests) library with similar public API.

* Install `httpx` in your local environment:

    ```
    pip install httpx
    ```

* Run:
    ```python
    import httpx

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "X-Api-Key": "1234ABCD",
    }
    
    with httpx.Client() as client:
        resp = client.get("http://localhost:4000/api-a/123", headers=headers)
        resp_json = resp.json()

    # Check successful status code
    assert resp.status_code == 200

    # Print JSON response
    print(resp_json)
    ```

## Stop the Container

Run:

```bash
docker-compose down
```

## Remarks

This template is developed and tested on

- Python 3.8
- Docker version 19.03.12
- docker-compose 1.26.2
- Ubuntu 20.04 LTS
