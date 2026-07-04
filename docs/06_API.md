# API Design

**Version:** 0.1

**Author:** Emiliano Mayen

**Status:** Draft

---

# Overview

The AI Pipeline Monitor API provides a RESTful interface that allows users, dashboards, and AI agents to retrieve pipeline information, execution history, system health metrics, and AI-generated recommendations.

The API acts as the communication layer between the frontend dashboard, the monitoring engine, the AI Agent, and the database.

---

# Architecture

User

↓

Streamlit Dashboard

↓

FastAPI

↓

Business Logic

↓

DuckDB Database

---

# Base URL

```
http://localhost:8000/api/v1
```

Future versions may support cloud deployment.

---

# Authentication

Version 1

No authentication required.

Future versions

- API Keys
- OAuth 2.0
- JWT Authentication

---

# Endpoints

## GET /pipelines

Description

Returns all registered pipelines.

Example Response

```json
[
    {
        "pipeline_id": 1,
        "pipeline_name": "Marketing Spend",
        "status": "Completed"
    }
]
```

---

## GET /pipelines/{id}

Description

Returns detailed information for a specific pipeline.

---

## GET /executions

Description

Returns execution history.

Optional Parameters

- pipeline_id
- status
- date

---

## GET /errors

Description

Returns all detected execution errors.

---

## GET /health

Description

Returns platform health metrics.

Example Response

```json
{
    "completed": 482,
    "failed": 8,
    "running": 3,
    "warning": 4
}
```

---

## POST /ask

Description

Allows users to ask questions to the AI Agent.

Request

```json
{
    "question":"Which pipelines failed today?"
}
```

Response

```json
{
    "answer":"Eight pipelines failed during the last 24 hours. The most common error was HTTP 401 Unauthorized."
}
```

---

## GET /recommendations

Description

Returns AI-generated recommendations.

---

## GET /statistics

Description

Returns operational statistics.

Example

- Average execution time
- Success rate
- Failure rate
- Daily executions

---

## GET /history/{pipeline_id}

Description

Returns execution history for a specific pipeline.

---

# HTTP Status Codes

| Code | Meaning |
|-------|----------|
| 200 | Success |
| 201 | Resource Created |
| 400 | Bad Request |
| 401 | Unauthorized |
| 404 | Not Found |
| 500 | Internal Server Error |

---

# API Versioning

The API follows URL versioning.

Example

```
/api/v1
```

Future versions

```
/api/v2
```

---

# Future Endpoints

Future releases may include:

POST /login

POST /logout

POST /notifications

GET /dashboard

GET /alerts

POST /feedback

GET /prediction

POST /incident

GET /knowledge-base

---

# API Design Principles

The API follows the principles below:

- RESTful Design
- Stateless Communication
- JSON Responses
- Versioned Endpoints
- Consistent Naming
- Scalability
- Security
- Extensibility

---

# Planned Technologies

| Component | Technology |
|------------|------------|
| Framework | FastAPI |
| Documentation | Swagger UI |
| Response Format | JSON |
| Validation | Pydantic |
| Testing | Pytest |
