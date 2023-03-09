# How to use fastapi with python

# Function to create an api with fastapi
def fastapi_api(name, years):
    from fastapi import FastAPI
    app = FastAPI()

    @app.get('/')
    def index():
        return {
            'name': name,
            'years': years,
            'age': 25,
            'job': 'python developer'
        }

    return app

# Create an api with fastapi
app = fastapi_api('leo', 3)

# https://pypi.org/project/fastapi/

# Run the api with uvicorn
import uvicorn # pip install uvicorn
uvicorn.run(app, host='localhost', port=8000)