# Setting Up a Python Docker Environment

This guide outlines the steps to create a Docker environment for a Python application.

## 1. Create a Dockerfile

In your project's root directory, create a file named `Dockerfile` with the following content:

```Dockerfile
FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```

## 2 Create a requirements.txt file

In the same directory, create a requirements.txt file listing your Python dependencies:

```
flask==2.0.1
requests==2.26.0
```

## 3 Build the Docker image

Open a terminal in your project directory and run:

```
docker build -t my-python-app .
```

This command builds a Docker image named my-python-app based on the Dockerfile in the current directory.

## 4 Run the Docker container

To run the container with a bind mount for development, use:

```
docker run -it --rm -v $(pwd):/app my-python-app bash
```
