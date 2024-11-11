# Fast API

## What is FastAPI ?

FastAPI is an open-source Python framework based on Starlette (for web routing) and Pydantic (for data validation). It’s designed for creating APIs and web applications that are fast, robust, and easy to develop.

Key features include:

- **Automatic interactive API documentation**: FastAPI automatically generates Swagger UI and ReDoc for interactive API documentation.

- **Type hints for validation**: It uses Python type hints to validate input and output data, simplifying error handling and reducing bugs.

- **Async support**: It’s fully asynchronous, supporting high-performance asynchronous I/O using async and await, which makes it ideal for applications that need to handle high volumes of requests.

- **Validation and Serialization**: Built-in data validation with Pydantic makes it easy to validate complex data structures directly from your Python data models.

## Install FastAPI

1. Use pip to install FastAPI along with uvicorn, which is an ASGI server used to run FastAPI applications.

```cmd
pip install fastapi uvicorn
```

1. Once installed, you can import FastAPI and start creating an app like this:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```

1. Save the code to a file (example: main.py) and run it with Uvicorn.

```cmd
uvicorn main:app --reload
```
