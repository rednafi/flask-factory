

<div align="center">
    <h1> Flask Factory </h1>
    <h4>Flask App Template with Factory Pattern Architecture</h4>
</div>



## Architecture

Directory tree for serving multiple packages as Flask API with multiple endpoints

```
.
├── app
│   ├── api_a
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── sub.py
│   │   └── views.py
│   ├── api_b
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── sub.py
│   │   └── views.py
│   ├── flask_run.py
│   ├── __init__.py
│   ├── settings.py
│   └── tests
│       ├── __init__.py
│       └── test_api.py
├── .env
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── pyproject.toml
├── requirements-dev.txt
├── requirements.in
└── requirements.txt

4 directories, 21 files
```

## Setup

* Install [docker](https://docs.docker.com/install/) and [docker-compose](https://docs.docker.com/compose/install/) on your machine.

* Clone the repository & `cd` to the root directory.

## Run

Run the docker container:

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
## Run the Tests

Run:

```
pytest
```

If you run the tests while the docker container is running, pytest will run all tests. However, pytest will only run the unit tests if you run the tests offline.

## Stop the Container

Run:

```bash
docker-compose down
```

## Remarks

This template is developed and tested on

- Python 3.8
- Docker version 19.03.13
- docker-compose 1.26.2
- Ubuntu 20.04 LTS
