# Daily FastAPI Practice — Complete REST API Engineering Roadmap

> **Track:** REST API Development with Python and FastAPI  
> **Level:** HTTP beginner → industry-ready junior Python backend developer  
> **Duration:** 10 weeks / 70 calendar days (approximately 8–10 weeks at ~2 hours per day)  
> **Practice model:** Concepts to Cover / Revise → Tasks to Complete → Verify → Document  
> **Primary stack:** Python 3.12+, FastAPI, Pydantic v2, PostgreSQL, SQLAlchemy 2.x, Alembic, Pytest, HTTPX, Docker

## 1. Purpose and scope

Build the skills to design, implement, secure, test, document, and deploy maintainable REST APIs independently. The curriculum targets the **minimum practical industry standard for junior Python backend roles**, not expert-level mastery of every distributed-systems topic.

### Prerequisites

- Comfortable with Python functions, classes, exceptions, modules, virtual environments, typing basics, and Git.
- Basic SQL familiarity is helpful; PostgreSQL knowledge can develop alongside this track.
- No prior knowledge of HTTP, REST, ASGI, or FastAPI is assumed.

### Expected outcomes

By the end, you should be able to:

1. Explain HTTP semantics and REST design decisions clearly.
2. Build typed FastAPI endpoints with robust validation and consistent responses.
3. Model relational data, manage transactions, and evolve schemas safely.
4. Implement authentication, authorization, and essential API protections.
5. Handle concurrency appropriately and avoid blocking asynchronous endpoints.
6. Write unit and integration tests covering successful and failure cases.
7. Containerize, configure, observe, and deploy a backend service.
8. Present one polished, independently built capstone project in interviews.

### Explicitly deferred topics

Full-scale microservices, Kubernetes, service meshes, advanced distributed tracing, complex event-driven architectures, LLM orchestration, RAG, and agent frameworks are **not prerequisites** for this roadmap. They can follow after the core track.

## 2. Time commitment and pacing

| Daily time | Estimated pace | Guidance |
|---|---|---|
| 1 hour | 14–18 weeks | Split most days into two sessions |
| **2 hours** | **8–10 weeks** | Recommended; includes hands-on coding |
| 3 hours | 6–8 weeks | More project work and revision |
| 4 hours | 5–6 weeks | Intensive; leave time for debugging |

The 70-day schedule includes review and consolidation days. These are **estimates, not a guarantee of job readiness**. Advance based on evidence of competence, not the calendar alone.

**Typical two-hour session:**

| Activity | Target time |
|---|---:|
| Concepts to cover/revise | 30 min |
| Guided examples / experimentation | 20 min |
| Independent implementation tasks | 45 min |
| Tests, debugging, verification | 15 min |
| Notes and Git commit | 10 min |

## 3. Practice and documentation rules

Every day contains **Concepts to Cover / Revise**, **Tasks to Complete**, and **Completion Criteria**. These replace question-and-answer files.

- `Concepts.md`: concepts actually studied, examples, important insights, and revision flags.
- `Tasks_Completed.md`: actual implementation, commands/endpoints, evidence, test results, and pending tasks.
- `practical/`: code and experiments; place reusable application code in the appropriate project directory.
- `mistakes.md`: debugging observations, root causes, and fixes; create when needed.
- Do not mark a concept as understood or a task as completed merely because it appears in this roadmap.
- Write code independently first; request hints or reviews before full solutions.
- End each day with a small Git commit and an honest progress summary.

### Suggested repository structure

```text
Daily_FastAPI_Practice/
├── README.md
├── docs/
│   ├── roadmap.md
│   └── FastAPI_DailyPractice_masterprompt.md
├── D1_171026(SAT)/
│   ├── Concepts.md
│   ├── Tasks_Completed.md
│   ├── practical/
│   └── mistakes.md
├── D2_181026(SUN)/
│   └── ...
├── ...
├── projects/
│   ├── task_management_api/
│   └── media_processing_api/
├── .gitignore
└── README.md
```

The day/date naming scheme is illustrative: create the daily folder for the date you actually practice. Do not commit virtual environments, secrets, private uploads, or generated databases.

## 4. Ten-week overview

| Week | Focus | Deliverable |
|---|---|---|
| 1 | HTTP, web foundations, REST | HTTP request/response experiments and API contract |
| 2 | FastAPI + Pydantic | In-memory Task API |
| 3 | REST design + app architecture | Modular, validated Task API |
| 4 | PostgreSQL + SQLAlchemy + Alembic | Persistent Task API |
| 5 | Authentication + security | Protected multi-user API |
| 6 | Async + uploads + background processing | File-processing prototype |
| 7 | Testing + debugging | Reliable automated test suite |
| 8 | Docker + deployment + observability | Deployed containerized API |
| 9 | Independent capstone build | Secure Media & Document Processing API |
| 10 | Capstone hardening + interviews | Portfolio-ready project and interview notes |

---

# WEEK 1 — HTTP, REST, AND WEB FOUNDATIONS

**Goal:** Understand the protocol and architectural decisions before using a framework.

### Day 1 — Client–server communication and the web
**Concepts to Cover / Revise**
- Client, server, resource, endpoint, request, response, API.
- Network basics: IP address, hostname, DNS, ports, localhost.
- HTTP vs HTTPS; TLS purpose; stateless communication.
- Request lifecycle: client → network → server → response.

**Tasks to Complete**
- Draw and explain a request-response lifecycle for a browser and backend.
- Inspect two HTTP requests using browser developer tools or `curl -v`.
- Identify host, method, path, status, headers, and response body.
- Write a short explanation of why HTTPS matters for APIs.

**Completion Criteria:** Explain every major component of a basic HTTP exchange without relying on a framework.

### Day 2 — HTTP messages and representation
**Concepts to Cover / Revise**
- Request line, response status line, headers, body.
- Content types: JSON, text, multipart; `Content-Type` vs `Accept`.
- Query parameters, URL encoding, path segments, fragments.
- JSON objects, arrays, types, and serialization limitations.

**Tasks to Complete**
- Inspect a JSON API response and annotate its components.
- Send GET requests with path and query parameters using `curl` or Postman.
- Build valid and invalid JSON examples; explain errors.
- Compare a JSON request body with a multipart upload request.

**Completion Criteria:** Correctly describe message structure and common representation formats.

### Day 3 — HTTP methods and semantics
**Concepts to Cover / Revise**
- GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS.
- Safe vs idempotent methods; what they do and do not guarantee.
- Resource naming; request side effects; retries.
- PUT replacement vs PATCH partial modification.

**Tasks to Complete**
- Design method/path combinations for task CRUD.
- Explain which operations can safely be retried and why.
- Compare PUT and PATCH with sample payloads.
- Inspect method-specific requests in an API client.

**Completion Criteria:** Select appropriate methods and explain safety/idempotency accurately.

### Day 4 — HTTP status codes and error responses
**Concepts to Cover / Revise**
- 1xx–5xx categories.
- Common codes: 200, 201, 202, 204, 301/302, 304, 400, 401, 403, 404, 409, 415, 422, 429, 500, 503.
- `Location`, `Retry-After`, and meaningful error bodies.
- Difference between authentication failure and permission denial.

**Tasks to Complete**
- Map 12 API scenarios to suitable status codes.
- Design JSON error response examples for invalid input and missing resources.
- Inspect successful and failing requests using an API client.
- Explain why returning HTTP 200 for every error is problematic.

**Completion Criteria:** Choose defensible response codes for routine API outcomes.

### Day 5 — REST architecture and API contracts
**Concepts to Cover / Revise**
- REST constraints: client-server, statelessness, cacheability, uniform interface, layered system, optional code-on-demand.
- Resource-oriented URIs; representations; hypermedia as a REST constraint.
- RESTful conventions vs formal REST constraints.
- API contract and OpenAPI overview.

**Tasks to Complete**
- Design a task API resource map with routes and response codes.
- Define example request/response JSON for create, list, update, and delete.
- Identify two poorly designed routes and redesign them.
- Draft an API contract in Markdown.

**Completion Criteria:** Explain why an API is resource-oriented and distinguish REST from merely using JSON over HTTP.

### Day 6 — Headers, caching, CORS, and tooling
**Concepts to Cover / Revise**
- Authorization, cookies, origin, user agent, content negotiation.
- Cache-Control, ETag, conditional requests (intro).
- CORS and browser preflight; why CORS is not authentication.
- Postman, `curl`, browser DevTools; reproducible requests.

**Tasks to Complete**
- Inspect headers on multiple requests.
- Trigger or inspect an OPTIONS/preflight exchange where possible.
- Create a Postman collection or curl script for the planned Task API.
- Document three security misconceptions about CORS and HTTP headers.

**Completion Criteria:** Read and reason about routine HTTP headers and browser constraints.

### Day 7 — Week 1 revision and mini-assessment
**Concepts to Cover / Revise**
- Review weak points from Days 1–6.
- Request lifecycle, methods, status codes, REST resource design.

**Tasks to Complete**
- Produce a complete endpoint contract for a Task API.
- Explain five realistic HTTP scenarios without notes.
- Validate examples and correct inconsistencies.
- Update `Concepts.md`, `Tasks_Completed.md`, and `mistakes.md` as appropriate.

**Completion Criteria:** Explain and design a small HTTP API independently.

---

# WEEK 2 — FASTAPI AND PYDANTIC FUNDAMENTALS

**Goal:** Build a functioning typed API with validation and documentation.

### Day 8 — Environment setup and first FastAPI app
**Concepts to Cover / Revise**
- Virtual environments, dependency installation, reproducible dependencies.
- FastAPI, Starlette, ASGI, Uvicorn; development reload.
- App instance, route decorators, request lifecycle overview.

**Tasks to Complete**
- Create a Python 3.12 virtual environment and install FastAPI and Uvicorn.
- Implement `GET /health` and `GET /`.
- Run the server locally and inspect `/docs` and `/openapi.json`.
- Record installation, launch, and troubleshooting commands.

**Completion Criteria:** Run and inspect a FastAPI application from a clean environment.

### Day 9 — Routing, path, and query parameters
**Concepts to Cover / Revise**
- Path operation decorators; parameter types and coercion.
- Required/optional query parameters, defaults, constraints.
- Route ordering and ambiguity; validation errors.

**Tasks to Complete**
- Create `GET /tasks` and `GET /tasks/{task_id}`.
- Add optional filters such as `completed` and `limit`.
- Test invalid path and query values.
- Explain generated OpenAPI parameter documentation.

**Completion Criteria:** Implement and validate parameterized routes.

### Day 10 — Pydantic request models
**Concepts to Cover / Revise**
- BaseModel, type annotations, required vs optional fields.
- `Field`, constraints, nested models, defaults and default factories.
- Serialization vs validation; Pydantic v2 basics.

**Tasks to Complete**
- Define `TaskCreate` and `TaskUpdate` models.
- Implement `POST /tasks` using in-memory storage.
- Test missing, malformed, and out-of-range values.
- Document why separate create/update schemas are useful.

**Completion Criteria:** Design and validate nontrivial JSON request bodies.

### Day 11 — Responses, status codes, and serialization
**Concepts to Cover / Revise**
- `response_model`, return annotations, response filtering.
- JSON-compatible serialization, dates, enums, UUIDs.
- Status codes and response headers; 201 and 204 semantics.

**Tasks to Complete**
- Define `TaskRead` without exposing internal fields.
- Return 201 for create and 204 for delete.
- Verify response shape through `/docs` and tests/manual requests.
- Add an enum field and date/time field.

**Completion Criteria:** Return correct, documented, validated responses.

### Day 12 — Error handling and validation customization
**Concepts to Cover / Revise**
- `HTTPException`, request validation errors, custom exception handlers.
- Consistent error shapes and safe error messages.
- 404 vs 409 vs 422; avoiding sensitive traceback leakage.

**Tasks to Complete**
- Return 404 for missing task IDs.
- Return 409 for a defined conflict (e.g., duplicate unique task code).
- Add a custom domain exception and handler.
- Verify error response shapes manually.

**Completion Criteria:** Handle routine failures predictably.

### Day 13 — OpenAPI and endpoint usability
**Concepts to Cover / Revise**
- OpenAPI schema, Swagger UI, ReDoc.
- Tags, summaries, descriptions, examples, response documentation.
- API discoverability and consistent naming.

**Tasks to Complete**
- Document every Task API endpoint.
- Add example request bodies and response descriptions.
- Export or inspect the OpenAPI JSON schema.
- Ask another person (or a fresh session) to follow the docs without your help.

**Completion Criteria:** API behavior can be understood from its contract.

### Day 14 — Week 2 review: in-memory Task API
**Concepts to Cover / Revise**
- Routing, validation, response models, errors, OpenAPI.

**Tasks to Complete**
- Finish GET/POST/PUT/PATCH/DELETE routes using temporary in-memory data.
- Test expected success and failure scenarios.
- Remove duplicated logic and document limitations of in-memory storage.
- Commit a working Week 2 milestone.

**Completion Criteria:** Functional, documented in-memory CRUD API.

---

# WEEK 3 — REST DESIGN AND APPLICATION ARCHITECTURE

**Goal:** Organize code for maintenance and predictable behavior.

### Day 15 — Modular FastAPI project structure
**Concepts to Cover / Revise**
- Packages/modules, `APIRouter`, application entry point.
- Separation of routes, schemas, services, repositories, configuration.
- Why architecture should match project complexity.

**Tasks to Complete**
- Split the Task API into `main.py`, routers, schemas, and services.
- Add `/api/v1` prefix and tags.
- Verify imports, startup, and all existing routes.

**Completion Criteria:** Clear module boundaries with no behavior regression.

### Day 16 — Dependency injection
**Concepts to Cover / Revise**
- `Depends`, dependency trees, caching per request.
- `yield` dependencies and cleanup.
- Reusable dependencies for configuration, database sessions, and users.

**Tasks to Complete**
- Create a reusable pagination dependency.
- Inject a service dependency into routes.
- Implement and test a cleanup-oriented `yield` dependency.

**Completion Criteria:** Explain and use dependency injection rather than hard-coded globals.

### Day 17 — Resource design and CRUD semantics
**Concepts to Cover / Revise**
- Resource identity, URL naming, nested resources.
- PUT vs PATCH semantics and partial update behavior.
- Idempotency, duplicate submissions, optimistic conflicts (intro).

**Tasks to Complete**
- Review all task routes against HTTP semantics.
- Implement PUT and PATCH with clearly documented behavior.
- Verify duplicate, missing, and unchanged update scenarios.

**Completion Criteria:** Predictable update semantics and consistent resources.

### Day 18 — Filtering, sorting, and pagination
**Concepts to Cover / Revise**
- Filter parameters, sort allowlists, limit/offset pagination.
- Stable ordering and deterministic results.
- Cursor pagination concepts and when to prefer it.

**Tasks to Complete**
- Add `status`, `priority`, and search filters.
- Implement sorting and limit/offset pagination.
- Verify boundaries, empty pages, and invalid sort fields.

**Completion Criteria:** List endpoints behave consistently under filtering and pagination.

### Day 19 — Configuration and settings
**Concepts to Cover / Revise**
- Environment variables, settings models, `.env` in local development.
- Development vs production configuration.
- Secret handling, defaults, fail-fast validation.

**Tasks to Complete**
- Add a typed settings module (e.g., `pydantic-settings`).
- Configure API prefix, app name, and environment-dependent options.
- Create `.env.example` and `.gitignore` rules.
- Confirm secrets are not printed or committed.

**Completion Criteria:** Configuration is centralized and safe to share.

### Day 20 — Consistency, errors, and maintainability
**Concepts to Cover / Revise**
- Domain errors vs transport errors.
- Input validation vs business rule validation.
- Logging fundamentals, consistent error contracts, simple API versioning.

**Tasks to Complete**
- Move business rules out of route handlers.
- Add structured error handling for domain conflicts.
- Refactor duplicated code and verify route behavior.

**Completion Criteria:** Thin routes and reusable business logic.

### Day 21 — Week 3 architecture review
**Concepts to Cover / Revise**
- Router structure, dependencies, response consistency, API contracts.

**Tasks to Complete**
- Review project structure and annotate each layer's responsibility.
- Run manual regression tests for all endpoints.
- Write a short architecture note and a list of technical debt.

**Completion Criteria:** Maintainable modular API ready for persistence.

---

# WEEK 4 — POSTGRESQL, SQLALCHEMY, AND MIGRATIONS

**Goal:** Build durable database-backed endpoints.

### Day 22 — Relational modeling for APIs
**Concepts to Cover / Revise**
- Primary/foreign keys, constraints, indexes, normalization.
- Users, tasks, categories, ownership, timestamps.
- Schema design tradeoffs and data integrity.

**Tasks to Complete**
- Design a relational schema and ER diagram.
- Define constraints and indexes with justification.
- Create a local PostgreSQL database and role with least privilege.

**Completion Criteria:** Defensible schema with clear relationships.

### Day 23 — SQLAlchemy 2.x ORM fundamentals
**Concepts to Cover / Revise**
- Engine, declarative models, `Mapped`, `mapped_column`.
- ORM objects vs rows; database-generated IDs.
- Sessions and identity map (intro).

**Tasks to Complete**
- Define SQLAlchemy models for User, Task, Category.
- Configure an engine and session factory.
- Run a small script to insert and query sample records.

**Completion Criteria:** ORM models map correctly to PostgreSQL tables.

### Day 24 — Sessions, transactions, and CRUD
**Concepts to Cover / Revise**
- Transaction boundaries, commit, rollback, flush, refresh.
- Session lifecycle and per-request dependency.
- Exceptions and safe rollback behavior.

**Tasks to Complete**
- Implement a database session dependency.
- Replace in-memory task creation and retrieval with ORM operations.
- Verify rollback on a failed write.

**Completion Criteria:** Database work uses clear transaction boundaries.

### Day 25 — Relationships and querying
**Concepts to Cover / Revise**
- One-to-many and many-to-many relationships.
- Joins, eager/lazy loading, N+1 query problem.
- Query filtering and result ordering.

**Tasks to Complete**
- Implement task ownership and categories.
- Add endpoints that return related data safely.
- Inspect generated SQL or query logs to detect unnecessary queries.

**Completion Criteria:** Correct relational queries without obvious N+1 pitfalls.

### Day 26 — Alembic migrations
**Concepts to Cover / Revise**
- Schema versioning, migration revisions, upgrade/downgrade.
- Autogeneration limitations; reviewing migration scripts.
- Safe schema changes and data migrations (intro).

**Tasks to Complete**
- Initialize Alembic and create an initial migration.
- Add a column with a reviewed migration.
- Test migration against a disposable development database.

**Completion Criteria:** Database schema can be recreated and evolved reproducibly.

### Day 27 — Database-backed API integration
**Concepts to Cover / Revise**
- Persistence, unique constraints, 409 conflicts.
- Database pagination, indexes, query efficiency.
- Serialization boundaries between ORM and API models.

**Tasks to Complete**
- Complete database-backed CRUD routes.
- Verify filters, pagination, relationships, and constraints.
- Inspect query plans for at least one filtered query.

**Completion Criteria:** All core API operations persist correctly.

### Day 28 — Week 4 database review
**Concepts to Cover / Revise**
- Sessions, transactions, migrations, constraints, relationships.

**Tasks to Complete**
- Rebuild the database from migrations.
- Run CRUD scenarios including conflict and rollback cases.
- Document database setup and common failure modes.

**Completion Criteria:** Reproducible persistent Task API.

---

# WEEK 5 — AUTHENTICATION, AUTHORIZATION, AND SECURITY

**Goal:** Protect data and enforce user-specific access.

### Day 29 — Security fundamentals and password handling
**Concepts to Cover / Revise**
- Authentication vs authorization; threat modeling basics.
- Password hashing (Argon2/bcrypt), salts, never storing plaintext.
- Registration validation and generic failure responses.

**Tasks to Complete**
- Implement user registration with a reputable password-hashing library.
- Verify passwords securely.
- Prevent duplicate account creation without leaking sensitive details.

**Completion Criteria:** Passwords are never stored or logged in plaintext.

### Day 30 — Login and token authentication
**Concepts to Cover / Revise**
- Bearer tokens, JWT structure, claims, signatures, expiry.
- OAuth2 password-flow concepts and limitations.
- Token validation and secret/key management.

**Tasks to Complete**
- Implement a login endpoint and short-lived access tokens.
- Protect a `GET /users/me` endpoint.
- Test missing, invalid, tampered, and expired tokens.

**Completion Criteria:** Authentication reliably accepts valid tokens and rejects invalid ones.

### Day 31 — Authorization and object ownership
**Concepts to Cover / Revise**
- Roles, permissions, object-level authorization.
- Horizontal privilege escalation / broken object-level authorization.
- Least privilege and default-deny behavior.

**Tasks to Complete**
- Restrict task CRUD to the owning user.
- Add one role-protected operation if appropriate.
- Verify one user cannot access another user's tasks.

**Completion Criteria:** Cross-user access is blocked in tests.

### Day 32 — Token lifecycle and account protections
**Concepts to Cover / Revise**
- Token expiration, refresh/revocation strategies (overview).
- Login rate limiting and brute-force protection.
- Secure cookies vs bearer headers, CSRF distinctions.

**Tasks to Complete**
- Document your chosen token strategy and its limitations.
- Implement an appropriate rate-limit demonstration or local guard.
- Verify logout/revocation behavior if implemented; do not claim JWTs are revoked without server-side support.

**Completion Criteria:** Understand token lifecycle and common misuse risks.

### Day 33 — API security controls
**Concepts to Cover / Revise**
- Input validation, injection risks, ORM parameterization.
- CORS configuration, HTTPS, secret handling, security headers.
- Request size limits, error disclosure, logging redaction.

**Tasks to Complete**
- Restrict allowed origins for a known frontend.
- Test malformed payloads and oversized request handling where configured.
- Audit logs and code for leaked tokens, credentials, or stack traces.

**Completion Criteria:** Essential security controls are implemented or clearly documented as deployment responsibilities.

### Day 34 — Security-focused API review
**Concepts to Cover / Revise**
- OWASP API Security Top 10 overview.
- Authorization bypass, excessive data exposure, unsafe defaults.
- Secure dependency management and update practices.

**Tasks to Complete**
- Create a simple threat checklist for Task API routes.
- Attempt unauthorized access scenarios against a local test environment.
- Fix identified issues and record evidence.

**Completion Criteria:** No known basic auth/ownership bypasses in tested flows.

### Day 35 — Week 5 security milestone
**Concepts to Cover / Revise**
- Registration, login, JWT, authorization, security tradeoffs.

**Tasks to Complete**
- Demonstrate end-to-end user registration → login → authorized CRUD.
- Demonstrate negative security tests.
- Document auth flow and configuration requirements.

**Completion Criteria:** Working protected multi-user API.

---

# WEEK 6 — ASYNC, FILE UPLOADS, AND BACKGROUND WORK

**Goal:** Handle I/O and media-related backend operations safely.

### Day 36 — AsyncIO foundations
**Concepts to Cover / Revise**
- Coroutines, event loop, `await`, tasks, concurrency vs parallelism.
- I/O-bound vs CPU-bound work.
- Blocking operations and why they matter in async endpoints.

**Tasks to Complete**
- Compare sequential and concurrent simulated I/O tasks.
- Explain why `time.sleep()` inside an async route is problematic.
- Build a small nonblocking async example.

**Completion Criteria:** Correctly distinguish concurrency, parallelism, and blocking.

### Day 37 — Sync vs async FastAPI endpoints
**Concepts to Cover / Revise**
- `def` vs `async def` route behavior.
- Threadpool usage, blocking database clients, async-compatible clients.
- Timeouts, cancellation, resource cleanup.

**Tasks to Complete**
- Create safe sync and async endpoints for contrasting I/O workloads.
- Identify blocking calls in existing routes.
- Add timeout handling to an outbound HTTP call.

**Completion Criteria:** Choose sync/async approaches based on dependencies and workload.

### Day 38 — Middleware and application lifecycle
**Concepts to Cover / Revise**
- Middleware order and request/response interception.
- Lifespan startup/shutdown, shared resources.
- Correlation/request IDs and basic timing logs.

**Tasks to Complete**
- Add request timing and correlation IDs.
- Configure an application lifespan handler.
- Verify resource initialization and cleanup.

**Completion Criteria:** Middleware and lifecycle are used appropriately.

### Day 39 — Multipart and secure uploads
**Concepts to Cover / Revise**
- Multipart form data, `UploadFile`, streaming uploads.
- File-size and content validation, filename/path safety.
- Temporary storage, storage paths, media metadata.

**Tasks to Complete**
- Implement authenticated `POST /uploads`.
- Accept a limited set of document/image formats with validation.
- Store files under generated identifiers, not user-provided paths.
- Record upload metadata in PostgreSQL.

**Completion Criteria:** Files are uploaded and stored without trusting filenames or declared content types alone.

### Day 40 — Downloads, storage abstraction, and streaming
**Concepts to Cover / Revise**
- File responses and streaming responses.
- Local vs object storage (S3/MinIO concepts).
- Authorization, signed URLs, content disposition, cleanup.

**Tasks to Complete**
- Implement authenticated metadata and download endpoints.
- Create a storage service interface so local storage can later be replaced.
- Verify unauthorized users cannot download private files.

**Completion Criteria:** Files can be retrieved safely through an abstraction.

### Day 41 — Background tasks and job status
**Concepts to Cover / Revise**
- FastAPI `BackgroundTasks` for lightweight in-process work.
- Durable queues/workers for long-running or critical tasks.
- Job states, retries, idempotency, failure and cancellation concepts.

**Tasks to Complete**
- Implement a lightweight post-upload processing demo.
- Add a `processing_jobs` table with status and error metadata.
- Expose `GET /jobs/{id}`; document limitations of in-process work.
- Sketch a future Redis/worker architecture without implementing it yet.

**Completion Criteria:** Distinguish demo background work from durable production job processing.

### Day 42 — Week 6 media prototype review
**Concepts to Cover / Revise**
- Async correctness, uploads, downloads, lifecycle, job status.

**Tasks to Complete**
- Demonstrate upload → validate → store → process → status → download.
- Test missing files, invalid formats, oversized files, and denied access.
- Record storage and cleanup decisions.

**Completion Criteria:** Working local media/document processing prototype.

---

# WEEK 7 — TESTING, DEBUGGING, AND RELIABILITY

**Goal:** Validate behavior automatically and detect regressions.

### Day 43 — Pytest fundamentals
**Concepts to Cover / Revise**
- Test discovery, assertions, fixtures, parametrization.
- Unit vs integration vs end-to-end tests.
- Arrange–Act–Assert and test naming.

**Tasks to Complete**
- Set up Pytest.
- Write tests for pure validation and service functions.
- Parametrize valid and invalid input cases.

**Completion Criteria:** Repeatable automated unit tests.

### Day 44 — FastAPI endpoint testing
**Concepts to Cover / Revise**
- `TestClient`, HTTPX, sync/async test approaches.
- Request assertions, response JSON, status, headers.
- Test isolation and deterministic data.

**Tasks to Complete**
- Test health, create, read, update, and delete routes.
- Cover 2xx, 4xx, and representative error cases.
- Confirm tests do not require a running development server.

**Completion Criteria:** Endpoint behavior is covered with automated tests.

### Day 45 — Database integration testing
**Concepts to Cover / Revise**
- Disposable test databases and schema setup.
- Transaction rollback and cleanup strategies.
- Dependency overrides for database sessions.

**Tasks to Complete**
- Create a dedicated test database/configuration.
- Override the DB dependency in tests.
- Verify isolation across multiple test runs.

**Completion Criteria:** Database tests cannot corrupt development data.

### Day 46 — Authentication and authorization tests
**Concepts to Cover / Revise**
- Auth fixtures, token generation, permission matrix.
- Negative security testing, object ownership checks.

**Tasks to Complete**
- Test registration/login success and failure.
- Test expired/invalid tokens.
- Test access to another user's resources.

**Completion Criteria:** Critical auth boundaries are tested automatically.

### Day 47 — Mocking external dependencies
**Concepts to Cover / Revise**
- Mock vs fake vs stub; when not to mock.
- Dependency overrides and HTTP service simulation.
- Failure injection, timeout testing.

**Tasks to Complete**
- Replace an external service dependency with a test fake.
- Test timeout and upstream failure handling.
- Ensure no real network calls are required for unit tests.

**Completion Criteria:** External failures are handled and testable.

### Day 48 — Debugging, quality tools, and logs
**Concepts to Cover / Revise**
- Debugger, tracebacks, structured logging, request IDs.
- Ruff formatting/linting, typing checks (intro), coverage interpretation.
- Error reproduction and root-cause analysis.

**Tasks to Complete**
- Configure a formatter/linter and run it on the project.
- Debug an intentionally broken endpoint.
- Generate a test coverage report and identify untested critical paths.

**Completion Criteria:** Repeatable quality checks and actionable debugging notes.

### Day 49 — Week 7 quality gate
**Concepts to Cover / Revise**
- Test pyramid, failure paths, security regressions, coverage limitations.

**Tasks to Complete**
- Run the full test suite from a clean checkout/configuration.
- Fix flaky tests and document setup.
- Add a minimal `make`/PowerShell/script command to run quality checks.

**Completion Criteria:** Consistent test results and no known critical failures.

---

# WEEK 8 — DOCKER, DEPLOYMENT, AND OPERATIONS

**Goal:** Run and troubleshoot a backend outside the IDE.

### Day 50 — Packaging and production configuration
**Concepts to Cover / Revise**
- Dependency pinning/lock strategies, `.env.example`.
- Dev/test/prod settings, secrets and runtime configuration.
- Startup validation and fail-fast behavior.

**Tasks to Complete**
- Document installation from a clean environment.
- Separate development and production configuration.
- Verify startup fails clearly when required settings are missing.

**Completion Criteria:** Application starts reproducibly with explicit configuration.

### Day 51 — Docker fundamentals
**Concepts to Cover / Revise**
- Image vs container, Dockerfile, layers, build context.
- `.dockerignore`, ports, volumes, non-root execution.
- Health checks and container logs.

**Tasks to Complete**
- Create a Dockerfile for FastAPI.
- Build and run the image locally.
- Confirm `/health` works from the host.

**Completion Criteria:** FastAPI runs inside a container.

### Day 52 — Docker Compose and PostgreSQL
**Concepts to Cover / Revise**
- Multi-service configuration, networks, volumes.
- Environment injection and startup readiness.
- Database persistence and migrations in deployment.

**Tasks to Complete**
- Add FastAPI and PostgreSQL services to Compose.
- Run migrations against the containerized database.
- Verify persistence across application restarts.

**Completion Criteria:** Reproducible two-service local deployment.

### Day 53 — Production serving and HTTPS
**Concepts to Cover / Revise**
- ASGI serving, worker processes, reverse proxies.
- HTTPS termination, forwarded headers, trusted proxies.
- Graceful shutdown, startup readiness, request limits.

**Tasks to Complete**
- Write a production-style start command.
- Document reverse proxy and TLS requirements.
- Verify health checks and graceful restart behavior locally where feasible.

**Completion Criteria:** Explain the difference between local dev server setup and production hosting.

### Day 54 — Logging, health checks, and observability
**Concepts to Cover / Revise**
- Liveness vs readiness, structured logs, request IDs.
- Metrics and alerting basics; sensitive-data redaction.
- Failure diagnosis with logs and status codes.

**Tasks to Complete**
- Add health/readiness endpoints with appropriate behavior.
- Add structured request logs without secrets.
- Simulate a database outage and inspect failure handling.

**Completion Criteria:** Common operational failures are diagnosable.

### Day 55 — CI/CD and deployment workflow
**Concepts to Cover / Revise**
- CI pipeline stages: lint, test, build.
- GitHub Actions fundamentals, secrets handling.
- Deployment options and rollback concepts.

**Tasks to Complete**
- Create a CI workflow that runs tests and lint checks.
- Build the container in CI if feasible.
- Document a simple deployment and rollback procedure.

**Completion Criteria:** Automated checks run on repository changes.

### Day 56 — Week 8 production milestone
**Concepts to Cover / Revise**
- Containerization, configuration, migrations, logs, TLS, CI.

**Tasks to Complete**
- Deploy to an accessible environment if available (or reproduce locally with Docker Compose).
- Perform a smoke test against the deployed API.
- Write a runbook: start, stop, migrate, diagnose, recover.

**Completion Criteria:** Documented, testable deployment with basic operational hygiene.

---

# WEEK 9 — INDEPENDENT CAPSTONE: SECURE MEDIA & DOCUMENT API

**Goal:** Build a new application with less step-by-step guidance.

### Capstone requirements

Implement a REST API for authenticated users to upload and manage documents/images, trigger a lightweight processing job, check status, and retrieve authorized results. Use local storage initially with a replaceable storage abstraction. **Do not add real GPU inference, video generation, or complex queues yet.**

### Day 57 — Requirements and API contract
**Concepts to Cover / Revise**
- Functional/nonfunctional requirements, actors, resources, API contract.

**Tasks to Complete**
- Write use cases, endpoint table, error scenarios, and acceptance criteria.
- Define scope and explicit non-goals.

**Completion Criteria:** Implementable requirements and contract.

### Day 58 — Data model and project skeleton
**Concepts to Cover / Revise**
- Resource ownership, media metadata, job records, migrations.

**Tasks to Complete**
- Design schema and create FastAPI modules.
- Configure settings, database, and initial migrations.

**Completion Criteria:** Application skeleton and reproducible schema.

### Day 59 — Authentication and permissions
**Concepts to Cover / Revise**
- Reusable auth dependencies and object-level access.

**Tasks to Complete**
- Add registration/login or reuse a carefully reviewed auth module.
- Enforce per-user asset ownership.

**Completion Criteria:** Private assets cannot be accessed by other users.

### Day 60 — Secure upload pipeline
**Concepts to Cover / Revise**
- Upload streaming, validation, generated filenames, storage errors.

**Tasks to Complete**
- Implement upload endpoint and metadata persistence.
- Handle invalid/empty/oversized files and partial failure cleanup.

**Completion Criteria:** Safe uploads with predictable failure behavior.

### Day 61 — Asset listing, retrieval, deletion
**Concepts to Cover / Revise**
- Filtering, pagination, download authorization, delete semantics.

**Tasks to Complete**
- Implement asset list, detail, download, and delete.
- Handle missing resources and cleanup consistently.

**Completion Criteria:** Complete authenticated asset CRUD lifecycle.

### Day 62 — Processing job workflow
**Concepts to Cover / Revise**
- Job status state machine, failure states, retry concepts.

**Tasks to Complete**
- Implement a small processing operation (e.g., image thumbnail or document metadata extraction).
- Create job records and status endpoints.
- Make job execution limitations explicit; use a worker if durability is required.

**Completion Criteria:** End-to-end processing flow with visible status.

### Day 63 — Capstone integration review
**Concepts to Cover / Revise**
- Service boundaries, consistency, failure recovery.

**Tasks to Complete**
- Run end-to-end scenarios from upload to result retrieval.
- Resolve critical functional defects.
- Prepare a gap list for Week 10.

**Completion Criteria:** Working feature-complete capstone prototype.

---

# WEEK 10 — HARDENING, DOCUMENTATION, AND INTERVIEW READINESS

**Goal:** Turn the capstone into a credible portfolio artifact.

### Day 64 — Test coverage and edge cases
**Concepts to Cover / Revise**
- Critical path tests, invalid inputs, ownership, cleanup.

**Tasks to Complete**
- Add integration tests for uploads, retrieval, deletion, and jobs.
- Test auth failures, invalid content, and storage errors.

**Completion Criteria:** Automated tests cover key workflows and security boundaries.

### Day 65 — Performance and resource limits
**Concepts to Cover / Revise**
- Query indexes, pagination, memory use, streaming, timeouts.
- Basic load testing concepts and safe resource limits.

**Tasks to Complete**
- Inspect slow queries and obvious bottlenecks.
- Verify upload limits and cleanup under failure.
- Run a small controlled load test locally.

**Completion Criteria:** Known bottlenecks and limits are documented.

### Day 66 — Security audit and configuration
**Concepts to Cover / Revise**
- Ownership checks, secret leakage, CORS, dependency vulnerabilities.

**Tasks to Complete**
- Review every endpoint for access control.
- Audit dependencies and committed files for secrets.
- Confirm deployment settings are safe for the target environment.

**Completion Criteria:** No known critical security misconfigurations.

### Day 67 — Docker and deployment verification
**Concepts to Cover / Revise**
- Compose, migrations, health checks, logs, restart behavior.

**Tasks to Complete**
- Containerize the capstone.
- Verify fresh setup and migration steps.
- Smoke-test the deployed/local-containerized service.

**Completion Criteria:** Reproducible deployment from README instructions.

### Day 68 — Documentation and portfolio presentation
**Concepts to Cover / Revise**
- API documentation, architecture diagrams, clear project narrative.

**Tasks to Complete**
- Write README: features, architecture, stack, setup, endpoints, tests, tradeoffs.
- Add OpenAPI examples and screenshots only where useful.
- Document future enhancements separately from implemented features.

**Completion Criteria:** Another developer can understand and run the project.

### Day 69 — Interview simulation and design discussion
**Concepts to Cover / Revise**
- HTTP semantics, DI, ORM sessions, JWT, async, testing, Docker.
- Tradeoffs: sync vs async, local vs object storage, background task vs durable queue.

**Tasks to Complete**
- Explain the architecture without reading notes.
- Walk through one request end to end.
- Debug a failing endpoint and justify a design decision.
- Prepare concise answers to common junior backend questions.

**Completion Criteria:** Can explain code, design choices, and limitations independently.

### Day 70 — Final assessment and next steps
**Concepts to Cover / Revise**
- Review weak competencies and remaining technical debt.

**Tasks to Complete**
- Re-run tests, lint, migrations, and smoke checks.
- Review the readiness checklist below.
- Record final project links, verified capabilities, and follow-up learning priorities.

**Completion Criteria:** Portfolio-ready API and an honest skills gap assessment.

---

## 5. Project milestones and definition of done

### Project A — Task Management REST API (Weeks 2–5)

**Minimum features:**
- [ ] Typed CRUD endpoints with correct HTTP status codes.
- [ ] Pydantic request and response schemas.
- [ ] Modular routers, services, and dependencies.
- [ ] PostgreSQL persistence with SQLAlchemy 2.x.
- [ ] Alembic migrations and database constraints.
- [ ] Registration/login with hashed passwords and validated tokens.
- [ ] Object-level ownership checks.
- [ ] Filtering, sorting, and pagination.
- [ ] OpenAPI documentation and meaningful errors.

### Project B — Secure Media & Document Processing API (Weeks 6, 9–10)

**Minimum features:**
- [ ] Authenticated uploads with size/content validation.
- [ ] Secure file identifiers and storage abstraction.
- [ ] PostgreSQL metadata and owner relationships.
- [ ] Authorized listing, retrieval, download, and deletion.
- [ ] Lightweight processing operation and job status.
- [ ] Documented behavior on failure and partial cleanup.
- [ ] Unit/integration tests including unauthorized access.
- [ ] Dockerized deployment, migrations, logs, and health checks.
- [ ] Complete README and usable OpenAPI schema.

### Quality bar for both projects

- Tests pass repeatedly in a clean environment.
- No secrets, tokens, virtual environments, or private uploads committed.
- Failure responses are meaningful and do not expose internal details.
- API and database schemas match actual behavior.
- Authorization is checked for each private resource.
- Setup instructions are accurate and reproducible.
- You can explain the architecture and key tradeoffs without relying on generated explanations.

## 6. Industry-readiness checklist

Use this as a **competency checklist**, not a claim that every employer uses identical requirements.

| Competency | Evidence to demonstrate | Status |
|---|---|---|
| HTTP and REST | Design and explain resource endpoints, methods, status codes | Not assessed |
| FastAPI + Pydantic | Validated, documented CRUD endpoints | Not assessed |
| Application structure | Routers, services, dependencies, settings | Not assessed |
| PostgreSQL + ORM | Relationships, transactions, efficient queries | Not assessed |
| Migrations | Recreate and evolve schema using Alembic | Not assessed |
| Authentication | Secure password verification and token validation | Not assessed |
| Authorization | Negative tests for cross-user access | Not assessed |
| Async fundamentals | Explain and avoid blocking async routes | Not assessed |
| Uploads / I/O | Safe file handling and resource limits | Not assessed |
| Testing | Repeatable unit and integration suite | Not assessed |
| Docker + deployment | Reproducible runtime and documented startup | Not assessed |
| Debugging + docs | Logs, API contract, README, design explanations | Not assessed |

**Readiness rule:** Mark a competency `Demonstrated` only after independently completing and explaining a working example. `Reviewed` means studied but not yet proven in practice.

## 7. Daily progress template

Use this template at the end of each session; save it in your daily notes or a separate progress tracker.

```markdown
# Day XX — [Topic]
Date: YYYY-MM-DD

## Concepts to Cover / Revise
- [ ] Concept A — Not started / Reviewed / Demonstrated
- [ ] Concept B — Not started / Reviewed / Demonstrated

## Tasks to Complete
- [ ] Task A
  - Evidence: [file, endpoint, test, command]
  - Result: [pass/fail/pending]
- [ ] Task B

## Verification
- Tests/commands executed:
- Results:
- Known limitations:

## Mistakes and Corrections
- Issue:
- Root cause:
- Fix:

## Daily Summary
- Concepts demonstrated:
- Concepts needing revision:
- Tasks completed:
- Tasks pending:
- Next step:
```

## 8. Suggested tooling and references

| Area | Suggested tool | Why |
|---|---|---|
| Editor | PyCharm / VS Code | Python development and debugging |
| Runtime | Python 3.12+ | Stable modern Python features |
| Framework | FastAPI | Typed ASGI APIs |
| Server | Uvicorn | Local and deployed ASGI serving |
| Schemas | Pydantic v2 | Validation and serialization |
| Settings | pydantic-settings | Typed environment configuration |
| Database | PostgreSQL | Relational persistence |
| ORM | SQLAlchemy 2.x | Database mapping and querying |
| Migrations | Alembic | Versioned schema changes |
| API client | Postman / curl | Manual API inspection |
| Tests | Pytest + HTTPX | Unit and endpoint testing |
| Quality | Ruff | Formatting and linting |
| Containers | Docker + Compose | Reproducible services |
| CI | GitHub Actions | Automated checks |

### Official documentation

- [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/)
- [FastAPI advanced user guide](https://fastapi.tiangolo.com/advanced/)
- [HTTP semantics — RFC 9110](https://www.rfc-editor.org/rfc/rfc9110)
- [Pydantic documentation](https://docs.pydantic.dev/latest/)
- [SQLAlchemy 2.0 documentation](https://docs.sqlalchemy.org/en/20/)
- [Alembic documentation](https://alembic.sqlalchemy.org/en/latest/)
- [PostgreSQL documentation](https://www.postgresql.org/docs/)
- [Pytest documentation](https://docs.pytest.org/en/stable/)
- [HTTPX documentation](https://www.python-httpx.org/)
- [Docker documentation](https://docs.docker.com/)
- [OWASP API Security Top 10](https://owasp.org/API-Security/)

## 9. What comes after this roadmap?

After completing the core track, choose **one** specialization rather than adding everything at once:

1. **AI application APIs:** model inference endpoints, request streaming, model service integration.
2. **Multimedia backends:** S3/MinIO, FFmpeg, resumable uploads, queues, workers, progress events.
3. **RAG APIs:** ingestion endpoints, pgvector retrieval, access-controlled document search.
4. **Agentic systems:** tool endpoints, orchestration, approval gates, durable execution and tracing.
5. **Advanced backend engineering:** Redis, Celery/Dramatiq, caching, observability, distributed systems.

The current roadmap is complete when you can independently **design → build → secure → test → document → deploy** a modest production-oriented REST API, not merely when all 70 days have elapsed.
