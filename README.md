# Flask Template

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

    ![process](https://github.com/rednafi/flask-tmplt/tree/master/imgs/container_process.png)

* Stop the docker container:

    ```
    sudo docker stop <CONTAINER_ID> 
    ```

* Check the docker image:
   
  ```
  sudo docker images
  ```
  This should show all the docker images.

  ![images](https://github.com/rednafi/flask-tmplt/tree/master/imgs/docker_images.png)

  
* Delete the image:

  ```
  sudo docker rmi <IMAGE_ID>
  ``` 


```
sudo rmi <>
```