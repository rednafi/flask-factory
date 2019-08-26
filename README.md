# Flask Template

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/rednafi/protomate/blob/master/LICENSE) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)
[![twitter](https://img.shields.io/twitter/url/https/home?style=social)](https://twitter.com)
[![twitter-follow](https://img.shields.io/twitter/follow/rednafi?label=Follow&style=social)]()

## Directory Tree
Directory tree for serving a python package as a Flask API

```
flask-ascii-art
├── app
│   ├── api
│   │   ├── ascii_art.py
│   │   ├── main_func.py
│   │   ├── __init__.py
│   │   └── views.py
│   ├── __init__.py
└── run_flask.py
```

## Instructions

### Run the API Directly
To run the app, go to `flask-ascii-art/` directory and run:

```
python run_flask.py
```
The app will run locally in port `5000`.

### Run As a Docker Container

* Build the docker container:

    ```
    sudo docker build . --tag=flask-tmplt
    ```

* Run the docker container: 

    ```
    sudo docker run -d -p 5000:5000 flask-tmplt
    ```

### Hit the API

While the above container is running, the API can be accessed via any API development client like [Postman](https://www.getpostman.com/).

```
x-api-key : 1234

# replace <word> with what you'd like to see as ascii-art

base-link : localhoast:5000/ascii-art/<word>
```

### Stop and Delete the Container After Experimentation

* Check the docker process:

    ```
    sudo docker ps
    ```
    This should show all the running containers.

    ![process](https://github.com/rednafi/flask-tmplt/blob/master/imgs/containter_process.png)

* Stop the docker container:

    ```
    sudo docker stop <CONTAINER_ID> 
    ```

* Check the docker image:
   
  ```
  sudo docker images
  ```
  This should show all the docker images.

  ![images](https://github.com/rednafi/flask-tmplt/blob/master/imgs/docker_images.png)

  
* Delete the image:

  ```
  sudo docker rmi <IMAGE_ID>
  ``` 
