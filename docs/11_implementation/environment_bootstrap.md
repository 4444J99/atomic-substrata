---
title: "Environment Bootstrap"
artifact_id: uaks_v1_environment_bootstrap_20260311
status: drafted_from_context
generated_at: 2026-03-12T19:28:12Z
source_lineage: "Derived from the UAKS architecture conversation artifact set."
---

# Environment Bootstrap

Document ID: uaks_v1_environment_bootstrap_20260311

## 1. Prerequisites

### 1.1 Required Tools

| Tool | Version | Purpose |
|------|---------|---------|
| Docker | 24.x | Container runtime |
| Docker Compose | 2.x | Local orchestration |
| Python | 3.11 | Runtime |
| kubectl | 1.28 | Kubernetes CLI |
| Terraform | 1.6 | Infrastructure |

### 1.2 System Requirements

- 8GB RAM minimum
- 50GB disk space
- macOS or Linux

## 2. Local Development Setup

### 2.1 Quick Start

```bash
# Clone repository
git clone https://github.com/organvm/uaks.git
cd uaks

# Bootstrap environment
make bootstrap

# Start services
make up

# Verify
make health
```

### 2.2 Manual Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start local database
docker-compose up -d postgres redis

# Run migrations
python -m alembic upgrade head

# Start application
python -m uaks.app
```

## 3. Cloud Environment Setup

### 3.1 Infrastructure

```bash
# Initialize Terraform
cd infrastructure
terraform init
terraform plan -out=tfplan
terraform apply tfplan
```

### 3.2 Application

```bash
# Deploy to Kubernetes
kubectl apply -f k8s/

# Check status
kubectl get pods
kubectl get services
```

## 4. Configuration

### 4.1 Environment Variables

```bash
# Database
DATABASE_URL=postgresql://user:pass@localhost:5432/uaks

# Redis
REDIS_URL=redis://localhost:6379

# Auth
AUTH_SECRET=your-secret-key

# Features
FEATURE_FLAGS=graph,assembly
```

## 5. Source Lineage

Derived from the UAKS architecture conversation artifact set.
