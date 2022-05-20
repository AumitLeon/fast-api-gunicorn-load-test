# Load Test Simulation with Fast API, Gunicorn, and Uvicorn Workers

## Prequisites
This project requires yarb, poetry with python 3.10, and docker.

## Load testing
Run `yarn docker:build` to to build the test app.

Run `yarn docker:run` to run the app (by default it's exposing port 80).

Run `yarn exec:loadtest` to run the loadtest.
