# MLOps Fraud Detection Platform on AWS

This project implements a **production-grade MLOps pipeline** for detecting fraudulent transactions using Machine Learning deployed on AWS.

## Architecture

GitHub → Jenkins → Docker → ECR → EKS → FastAPI → ML Model → S3  
Monitoring: Prometheus, Grafana, CloudWatch  
Automation: Terraform, CI/CD, Drift Detection

## Features
- Automated model training & evaluation
- Model versioning in S3
- CI/CD using Jenkins
- Containerized ML inference
- Kubernetes auto-scaling
- Data drift detection
- Real-time monitoring

## Tech Stack
- Python, Scikit-learn
- FastAPI
- Docker, Kubernetes (EKS)
- Terraform
- Jenkins
- AWS (S3, ECR, EKS)
- Prometheus, Grafana

## How to Run
1. Train model → `python training/train.py`
2. Save model → `python training/save_model.py`
3. Build Docker → `docker build -t fraud-api .`
4. Push to ECR → Jenkins
5. Deploy to EKS → Kubernetes
