
.PHONY: install run-api test fmt lint docker-build docker-run mlflow-ui

install:
	python -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

run-api:
	uvicorn app.main:app --reload --port 8000

test:
	pytest -q

fmt:
	black app tests

lint:
	flake8 app tests

docker-build:
	docker build -t mlops-handbook:latest .

docker-run:
	docker run -p 8000:8000 mlops-handbook:latest

mlflow-ui:
	mlflow ui --backend-store-uri file:./mlruns
