# FastAPI Learning Journal

**A structured, hands-on journey toward becoming a proficient Python Backend Developer.**

A daily learning repository focused on building a strong foundation in HTTP, RESTful API design, FastAPI, database integration, authentication, testing, and deployment.

This repository documents my progress through practical implementations, concept notes, API testing, and increasingly complex backend projects.

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Learning-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Planned-4169E1?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Status](https://img.shields.io/badge/Status-In%20Progress-blue)](https://github.com/Abhix126/FastAPI_Learning_Journal)

---

## Overview

The **FastAPI Learning Journal** is a project-based learning initiative designed to strengthen my understanding of Python backend development through consistent daily practice.

Instead of focusing exclusively on theoretical knowledge, this repository emphasizes understanding how backend systems work, implementing concepts through code, testing API behavior, and documenting the results.

**Primary objectives:**

- Understand HTTP communication and RESTful API principles.
- Develop backend applications using Python and FastAPI.
- Learn request validation, data serialization, and error handling.
- Integrate relational databases using PostgreSQL and SQLAlchemy.
- Implement authentication, authorization, and API security.
- Write automated tests and improve application reliability.
- Explore asynchronous programming, Docker, and deployment.
- Build production-oriented backend projects suitable for a developer portfolio.

## Learning Approach

Each practice day follows a consistent workflow:

1. **Learn:** Study the underlying concepts and their practical applications.
2. **Implement:** Build a working example or backend feature.
3. **Test:** Verify functionality using Postman, browser developer tools, or automated tests.
4. **Document:** Record concepts, implementation details, and test results.
5. **Publish:** Commit and push the completed work to GitHub.

The goal is to develop a deeper understanding of backend engineering rather than simply following tutorials.

## Technology Stack

The tools and technologies will be introduced progressively throughout the learning journey.

| Category | Technologies |
|---|---|
| Programming Language | Python 3.12 |
| Backend Framework | FastAPI |
| API Standards | HTTP, REST, JSON |
| Data Validation | Pydantic |
| Database | PostgreSQL |
| ORM & Migrations | SQLAlchemy, Alembic |
| Authentication | JWT, OAuth2 concepts |
| API Testing | Postman, HTTPX |
| Automated Testing | pytest |
| Development Tools | PyCharm, Git, GitHub |
| Containerization | Docker |
| Deployment | To be explored during advanced stages |

> **Note:** The table represents the planned learning stack. Not all technologies have been implemented yet.

## Learning Roadmap

The learning roadmap progresses from backend fundamentals to advanced API development and deployment.

| Phase | Focus Areas | Status |
|---|---|---|
| 01 | HTTP fundamentals and REST API principles | In progress |
| 02 | FastAPI fundamentals and routing | Planned |
| 03 | Pydantic models, validation, and error handling | Planned |
| 04 | CRUD operations and API architecture | Planned |
| 05 | PostgreSQL, SQLAlchemy, and Alembic | Planned |
| 06 | Authentication, authorization, and security | Planned |
| 07 | Asynchronous programming and file handling | Planned |
| 08 | Automated testing and API reliability | Planned |
| 09 | Docker, configuration, and deployment | Planned |
| 10 | Integrated backend projects and capstones | Planned |

The detailed curriculum is maintained in [`docs/roadmap.md`](docs/roadmap.md).

## Daily Progress Tracker

| Day | Date | Topic | Implementation | Status |
|---|---|---|---|---|
| 01 | 17 Oct 2026 | HTTP Fundamentals | Python HTTP Server | Completed |
| 02 | 18 Oct 2026 | REST Architecture and HTTP Methods | Upcoming | Planned |

This table will be updated as each practice day is completed.

### Day 01 — HTTP Fundamentals

**Objective:** Understand how HTTP requests and responses work before introducing a web framework.

Implemented a local HTTP API server using Python's built-in `http.server` module.

**Features implemented:**

- HTTP server running on `127.0.0.1:8000`
- GET request handling
- JSON response serialization
- HTTP status codes
- Response headers
- Endpoint routing
- Custom 404 error responses
- Graceful server shutdown

**Implemented endpoints:**

| Method | Endpoint | Description | Status |
|---|---|---|---|
| GET | `/` | Welcome message | 200 |
| GET | `/health` | Server health check | 200 |
| GET | `/info` | Application information | 200 |
| GET | `/unknown` | Unknown route handling | 404 |

**Documentation:**

- [Concepts Covered](D1_171026(SAT)/ConceptsCovered.md)
- [Implementation and Test Results](D1_171026(SAT)/Task_Completed.md)
- [Source Code](D1_171026(SAT)/practical/server.py)

## Repository Structure

```text
FastAPI_Learning_Journal/
│
├── D1_171026(SAT)/
│   ├── ConceptsCovered.md
│   ├── Task_Completed.md
│   └── practical/
│       ├── server.py
│       └── Screenshots/
│           ├── ss1.png
│           ├── ss2.png
│           ├── ss3.png
│           ├── ss4.png
│           └── ss5.png
│
├── docs/
│   └── roadmap.md
│
├── .gitignore
└── README.md
```

Future practice days will be added in separate folders following the same organizational pattern.

## Running the Day 01 Project

### Prerequisites

- Python 3.12 or a compatible Python 3 version
- Git
- Postman or a web browser for testing

### Clone the repository

```bash
git clone https://github.com/Abhix126/FastAPI_Learning_Journal.git
cd FastAPI_Learning_Journal
```

### Start the HTTP server

```bash
python "D1_171026(SAT)/practical/server.py"
```

Expected output:

```text
Server running at http://127.0.0.1:8000
```

### Test the endpoints

Open a browser or Postman and send GET requests to:

```text
http://127.0.0.1:8000/
http://127.0.0.1:8000/health
http://127.0.0.1:8000/info
```

Example health-check response:

```json
{
  "status": "healthy"
}
```

To stop the server, press `Ctrl + C` in the terminal.

> Day 01 intentionally uses Python's standard library to demonstrate HTTP fundamentals. FastAPI will be introduced in subsequent exercises.

## Documentation Standards

Each completed practice day aims to include:

| File or Folder | Purpose |
|---|---|
| `ConceptsCovered.md` | Technical concepts, explanations, and examples |
| `Task_Completed.md` | Implementation summary, code explanations, and test results |
| `practical/` | Working source code |
| `practical/Screenshots/` | Evidence of API behavior and testing |

This structure makes it easier to revisit concepts, track progress, and demonstrate practical learning.

## Future Project Goals

As the learning journey progresses, I plan to build applications that combine multiple backend concepts, including:

- Task Management REST API
- User Authentication and Authorization API
- Database-Driven CRUD Service
- File Upload and Processing API
- Backend Service for AI-Powered Applications

These projects will emphasize maintainable code, clear API design, reliable testing, and practical software engineering principles.

## Learning Outcomes

By completing this journal, I aim to become comfortable with:

- Designing and implementing RESTful APIs independently.
- Building maintainable FastAPI applications.
- Working with PostgreSQL and relational data models.
- Implementing secure authentication workflows.
- Writing automated backend tests.
- Debugging and documenting API behavior.
- Packaging and deploying backend services.
- Explaining technical decisions during Python backend interviews.

## Author

**Abhijit Saha**

Aspiring Python Backend Developer

GitHub: [@Abhix126](https://github.com/Abhix126)

---

*Building backend engineering skills through consistent practice, practical implementation, and continuous improvement.*