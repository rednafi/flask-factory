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

## Instruction

### Run the API Directly
To run the app, go to `flask-ascii-art/` directory and run:

```
python run_flask.py
```
The app will run locally in port `5000`. You can access it via the following link:

```
http://0.0.0.0:5000/
```

### Run As a Docker Container

Build the docker container:

```
sudo docker build . --tag=flask-tmplt
```

Run the docker container: 

```
sudo docker run -d -p 5000:5000 flask-tmplt
```

### Hit the API

