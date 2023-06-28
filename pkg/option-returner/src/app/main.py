from fastapi import FastAPI, HTTPException, Response
import os

version = os.getenv("VERSION", "v2.0.3")

app = FastAPI()


@app.get("/option/{option_target}")
def get_option(option_target: str):
    # Get option from env
    option = os.getenv(option_target)
    if not option:
        raise HTTPException(status_code=404, detail="Option target not found")
    return {"option_value": option}


@app.get("/eigen/node/spec-version")
def get_spec_version():
    return {"api_version": "v1.0.0"}


@app.get("/eigen/node/version")
def get_version():
    return {"version": version}


@app.get("/eigen/node/health", status_code=200)
def get_health(response: Response):
    # TODO: randomize response code from 200, 206, 503
    response.status_code = 200


@app.get("/eigen/node/services")
def get_services():
    return {"services": [
        {
            "id": "db-1",
            "name": "Database",
            "description": "Database description",
            "status": "Up",
        },
        {
            "id": "idx-2",
            "name": "Indexer",
            "description": "Indexer description",
            "status": "Down",
        }
    ]}


@app.get("/eigen/node/services/{service_id}/health")
def get_service_health(service_id: str, response: Response):
    if service_id == "db-1":
        response.status_code = 200
    elif service_id == "idx-2":
        response.status_code = 503
    else:
        raise HTTPException(status_code=404, detail="Service not found")
