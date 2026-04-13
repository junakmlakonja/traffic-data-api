# 🚦 Traffic Data Analytics API

A high-performance backend API for real-time traffic data ingestion and analytics, built with Python and FastAPI. Fully containerized and deployed to Microsoft Azure with a complete CI/CD pipeline.

**🔗 Live API:** https://traffic-api.victorioushill-e335aa45.westeurope.azurecontainerapps.io/docs

---

## 🚀 Key Features

- **Real-time Ingestion** — API endpoints for receiving traffic speed and segment data (simulating TomTom/HERE feeds)
- **Automated Analytics** — Real-time average speed calculation and congestion monitoring
- **Relational Database** — PostgreSQL-ready architecture using SQLAlchemy ORM
- **Auto-generated Docs** — Interactive Swagger/OpenAPI documentation at `/docs`
- **Containerized** — Dockerized and deployed to Azure Container Apps
- **CI/CD Pipeline** — Automated build and deployment via Azure Pipelines on every push to `main`

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.13+ |
| Framework | FastAPI |
| ORM | SQLAlchemy |
| Database | SQLite (dev) / PostgreSQL (production) |
| Validation | Pydantic |
| Containerization | Docker |
| Registry | Azure Container Registry (ACR) |
| Hosting | Azure Container Apps |
| CI/CD | Azure Pipelines |

---

## 🏗️ Project Structure

```
traffic-api/
├── app/
│   ├── main.py          # API routing & business logic
│   ├── models.py        # Database models (SQLAlchemy)
│   ├── database.py      # Connection & session management
│   ├── routes/
│   │   └── traffic.py   # Traffic endpoints
│   ├── services/
│   │   └── processing.py # Data processing logic
│   └── __init__.py
├── Dockerfile
├── azure-pipelines.yml  # CI/CD pipeline definition
├── requirements.txt
└── README.md
```

---

## ☁️ Azure Infrastructure

```
GitHub Push
    └─► Azure Pipelines (CI/CD)
            ├─► Docker Build
            ├─► Push to Azure Container Registry (ACR)
            └─► Deploy to Azure Container Apps
```

- **Container Registry:** `trafficapiregistry.azurecr.io`
- **Resource Group:** `traffic-api-rg`
- **Region:** West Europe

---

## 🔧 Run Locally

**Prerequisites:** Python 3.13+, Docker

```bash
# Clone the repo
git clone https://github.com/junakmlakonja/traffic-data-api.git
cd traffic-data-api

# Install dependencies
pip install -r requirements.txt

# Run the API
python -m app.main
```

API will be available at `http://localhost:8000`
Interactive docs at `http://localhost:8000/docs`

**Or with Docker:**

```bash
docker build -t traffic-api .
docker run -p 8000:8000 traffic-api
```

---

## 📄 API Documentation

Interactive Swagger UI is available at the live URL:
👉 https://traffic-api.victorioushill-e335aa45.westeurope.azurecontainerapps.io/docs

---

## 👩‍💻 Author

**Sara Radosavljević**
[LinkedIn](https://www.linkedin.com/in/sara-radosavljević-75311a20/) | Belgrade, Serbia
