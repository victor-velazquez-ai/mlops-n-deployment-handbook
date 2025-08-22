# MLOps & Deployment Handbook

A curated set of Jupyter notebooks showing how to **deploy ML models**, track experiments, and monitor them in production.

## Notebooks
1. Save & Load Models (joblib, pickle, ONNX)
2. FastAPI Serving
3. Dockerize a Model
4. CI/CD with GitHub Actions
5. Experiment Tracking with MLflow
6. Monitoring & Drift Detection
7. End-to-End Pipeline

## Setup
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000

```

## handy make targets
```bash
make run-api        # start FastAPI
make test           # run pytest
make docker-build   # build image
make docker-run     # run container on :8000
make mlflow-ui      # open MLflow UI (if you’ve run notebook 05/07)

```

