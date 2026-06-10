# 🚀 Fitness Tracker - DevOps End-to-End Project

## 📌 Project Overview
This project demonstrates a complete DevOps pipeline including CI/CD, GitOps, Kubernetes deployment, observability, and AI-based Kubernetes operations automation.

---

## 🏗️ Architecture

GitHub → GitHub Actions → Docker → ECR/Docker Hub → ArgoCD → EKS Cluster → Kubernetes Workloads → KGateway → Datadog Monitoring → AI Agent

---

## ⚙️ Tech Stack

- Git & GitHub
- GitHub Actions (CI/CD)
- Docker
- Kubernetes (EKS)
- Helm Charts
- ArgoCD (GitOps)
- Datadog (Monitoring & Observability)
- Python (AI Agent)
- AWS EKS

---

## 🔄 CI/CD Pipeline

1. Code pushed to GitHub
2. GitHub Actions triggered
3. Docker image built
4. Image pushed to registry
5. ArgoCD syncs deployment to Kubernetes

---

## ☸️ Kubernetes Deployment

- Deployed using Helm charts
- Namespace: fitness-tracker
- Includes:
  - Application Deployment
  - MongoDB Deployment
  - Services (LoadBalancer & ClusterIP)

---

## 🔁 GitOps (ArgoCD)

- Continuous deployment enabled
- Auto-sync enabled
- Application status: Synced & Healthy

---

## 📊 Monitoring (Datadog)

- Kubernetes cluster monitoring
- Pod & container metrics
- CPU & Memory usage
- Logs monitoring
- Alerts configured for threshold violations

---

## 🤖 AI Agent (SRE Assistant)

### Features:
- Monitors Kubernetes cluster health
- Detects issues like CrashLoopBackOff
- Suggests kubectl troubleshooting commands
- Provides SRE remediation steps

### Run command:
```bash
python3 ai_agent.py
