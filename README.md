This project demonstrates a production‑ready FastAPI application deployed on Kubernetes with a fully automated CI/CD pipeline powered by GitHub Actions.

It covers the complete workflow from local development to cloud‑native deployment:

FastAPI Application A lightweight Python web API framework, containerized with Docker for portability and reproducibility.

Dockerized Build The app is packaged into a Docker image, tagged, and pushed to Docker Hub for versioned releases.

Kubernetes Deployment Kubernetes manifests (k8s/) define the deployment, service, and cluster configuration for scalable, resilient workloads.

CI/CD Pipeline GitHub Actions automates the process:

Run tests (optional, extendable with pytest)

Build Docker image

Push image to Docker Hub

Deploy updated image to Kubernetes cluster

Rollback automatically if deployment fails

Secrets Management Credentials (Docker Hub, kubeconfig) are securely stored in GitHub Secrets, ensuring safe automation.

🚀 Why This Project Matters
Provides a real‑world DevOps workflow for containerized applications.

Ensures zero‑downtime deployments with Kubernetes rolling updates.

Demonstrates best practices for CI/CD automation, reproducibility, and scalability.

Serves as a foundation for production systems, extendable with Helm, monitoring, and notifications.

🛠️ Tech Stack
FastAPI (Python web framework)

Docker (containerization)

Kubernetes (orchestration)

GitHub Actions (CI/CD automation)

Docker Hub (image registry)