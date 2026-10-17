# Day 01 — Client–Server Communication & Web Fundamentals

> **Daily REST API & FastAPI Practice**
>
> **Date:** 17 October 2026 (Saturday)  
> **Week:** 01 | **Day:** 01  
> **Level:** Beginner — Foundation  
> **Estimated Duration:** 2 Hours  
> **Primary Focus:** Understanding HTTP communication and client-server architecture  
> **Practical Project:** Build and Test a Local HTTP API

---

## Session Information

### Topics to Cover / Revise

| Topic | Concepts Covered |
|---|---|
| Client–Server Architecture | Client, server, frontend, backend, database |
| HTTP Communication | Request-response lifecycle, stateless communication |
| Web Fundamentals | DNS, IP addresses, ports, localhost, URLs |
| HTTP Requests | Methods, paths, headers, request bodies |
| HTTP Responses | Status codes, headers, response bodies |
| HTTP Security | HTTP vs HTTPS, TLS |
| Web APIs | APIs, endpoints, JSON, REST introduction |
| API Testing | Postman, Chrome Developer Tools |

### Tools and Technologies

| Tool | Purpose |
|---|---|
| Python 3.12+ | Build a basic HTTP server |
| PyCharm / VS Code | Write and execute Python code |
| Postman | Send requests and inspect responses |
| Google Chrome | Inspect browser HTTP communication |
| Chrome Developer Tools | Analyze network requests |
| Git / GitHub | Version control and documentation |

**Note:** FastAPI will be introduced in upcoming lessons. Today's server uses Python's standard library to demonstrate how HTTP communication works.

### Learning Objectives

By the end of Day 01, you should be able to:

- Explain client-server architecture.
- Differentiate between frontend, backend, and database.
- Describe the HTTP request-response lifecycle.
- Understand URLs, DNS, IP addresses, and ports.
- Explain HTTP and HTTPS.
- Identify HTTP request and response components.
- Understand APIs, endpoints, and JSON.
- Build a basic HTTP server using Python.
- Test local API endpoints using Postman.
- Inspect HTTP communication using browser developer tools.

---

# Index

## Part A — Theory

1. [Client–Server Architecture](#clientserver-architecture)
2. [Frontend, Backend, and Database](#frontend-backend-and-database)
3. [HTTP Request–Response Lifecycle](#http-requestresponse-lifecycle)
4. [Understanding URLs](#understanding-urls)
5. [DNS and IP Addresses](#dns-and-ip-addresses)
6. [Ports and Localhost](#ports-and-localhost)
7. [How a Browser Loads a Website](#how-a-browser-loads-a-website)
8. [HTTP Fundamentals](#http-fundamentals)
9. [HTTP vs HTTPS](#http-vs-https)
10. [HTTP Request Structure](#http-request-structure)
11. [HTTP Response Structure](#http-response-structure)
12. [APIs and Endpoints](#apis-and-endpoints)
13. [JSON Data Format](#json-data-format)
14. [Introduction to REST](#introduction-to-rest)
15. [Introduction to Postman](#introduction-to-postman)
16. [Browser Developer Tools](#browser-developer-tools)

## Part B — Practical Assignment

1. [Project Overview](#project-overview)
2. [Project Objective](#project-objective)
3. [Functional Requirements](#functional-requirements)
4. [Project Structure](#project-structure)
5. [Implementation Guidelines](#implementation-guidelines)
6. [Running the Application](#running-the-application)
7. [Testing with Postman](#testing-with-postman)
8. [Expected Results](#expected-results)
9. [Acceptance Criteria](#acceptance-criteria)
10. [Submission Requirements](#submission-requirements)

## References

- [Official Learning Resources](#official-learning-resources)
- [Day 01 Completion Checklist](#day-01-completion-checklist)

---

# PART A — THEORY

---

## Client–Server Architecture

### What Is Client–Server Architecture?

Client-server architecture is a computing model where a **client requests resources or services** and a **server processes those requests and returns responses**.

In simple terms:

- **Client:** Requests information or services.
- **Server:** Processes requests and provides responses.
- **Request:** A message sent from the client to the server.
- **Response:** A message returned from the server to the client.

### Example: Online Shopping Application

Suppose you search for a laptop on an e-commerce website.

The following events may occur:

1. You enter a search query.
2. The browser sends a request to the backend.
3. The backend processes the search.
4. The backend queries a database.
5. The database returns matching products.
6. The backend prepares an HTTP response.
7. The browser displays the products.

### Architecture Diagram

```text
                  CLIENT
             (Web Browser)
                    |
                    |
              HTTP Request
                    |
                    v
              BACKEND SERVER
              (Python API)
                    |
                    |
              Database Query
                    |
                    v
                DATABASE
               (PostgreSQL)
                    |
                    |
               Query Result
                    |
                    v
              BACKEND SERVER
                    |
                    |
              HTTP Response
                    |
                    v
                  CLIENT
```

### Important Points

- Clients initiate requests.
- Servers process requests.
- Multiple clients can communicate with one server.
- A server can communicate with databases or other services.
- Not every HTTP request requires database access.

### Real-World Examples

| Client | Server |
|---|---|
| Chrome browser | Website backend |
| Android application | Mobile application API |
| Postman | REST API server |
| Python HTTPX client | External web API |
| React frontend | FastAPI backend |

---

## Frontend, Backend, and Database

A typical web application contains three major components.

### Frontend

The frontend is the part of an application that users interact with.

It is responsible for:

- Displaying information.
- Collecting user input.
- Sending requests to the backend.
- Rendering responses.
- Managing user-interface interactions.

Common technologies:

- HTML
- CSS
- JavaScript
- React
- Vue
- Angular

### Backend

The backend is responsible for server-side application logic.

Typical responsibilities include:

- Processing HTTP requests.
- Validating user input.
- Authentication and authorization.
- Executing business logic.
- Accessing databases.
- Communicating with external APIs.
- Preparing HTTP responses.

Common technologies:

- Python with FastAPI
- Python with Django
- Node.js
- Java with Spring Boot
- C# with ASP.NET Core

### Database

A database stores and retrieves application data.

Examples:

- PostgreSQL
- MySQL
- SQLite
- MongoDB

### Example: User Login

```text
Frontend
   |
   | Email + Password
   v
Backend API
   |
   | Retrieve User Record
   v
Database
   |
   | User Data + Password Hash
   v
Backend API
   |
   | Verify Password
   v
Authentication Result
   |
   v
Frontend
```

The backend should verify passwords using secure password-hashing techniques.

Passwords should never be stored in plaintext.

### Comparison

| Component | Main Responsibility |
|---|---|
| Frontend | User interaction |
| Backend | Application logic |
| Database | Persistent data storage |

---

## HTTP Request–Response Lifecycle

HTTP communication follows a request-response model.

A client sends a request to a server, and the server returns a response.

### HTTP Request

An HTTP request describes what the client wants the server to do.

Example:

```http
GET /users/10 HTTP/1.1
Host: api.example.com
Accept: application/json
```

The client requests information about user `10`.

### HTTP Response

The server processes the request and returns a response.

Example:

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "id": 10,
    "name": "Rahul",
    "department": "Engineering"
}
```

### Request–Response Flow

```text
Client
   |
   | 1. Prepare HTTP Request
   |
   v
Server
   |
   | 2. Receive Request
   |
   | 3. Validate Request
   |
   | 4. Execute Application Logic
   |
   | 5. Access Database (If Required)
   |
   | 6. Prepare HTTP Response
   |
   v
Client
   |
   | 7. Receive Response
   |
   | 8. Process Returned Data
   v
Display Result
```

### Important Observations

- The client initiates the HTTP request.
- The server decides how to handle it.
- The server may access databases or external services.
- The response contains information about the outcome.
- A response may contain JSON, HTML, text, or binary data.

---

## Understanding URLs

URL stands for **Uniform Resource Locator**.

A URL identifies the location of a resource and how it can be accessed.

### Example

```text
https://api.example.com:443/users/10?details=true
```

### URL Components

| Component | Value | Description |
|---|---|---|
| Scheme | `https` | Protocol used |
| Hostname | `api.example.com` | Server hostname |
| Port | `443` | Network port |
| Path | `/users/10` | Resource path |
| Query String | `details=true` | Additional parameters |

### General Syntax

```text
scheme://hostname:port/path?key=value
```

The port is optional in the written URL.

For example:

```text
https://example.com
```

HTTPS normally uses port `443` by default.

HTTP normally uses port `80`.

### Path vs Query Parameters

Path:

```text
/users/10
```

This commonly identifies a specific resource.

Query string:

```text
/users?department=engineering
```

This commonly provides filtering or other request parameters.

We will explore path and query parameters in detail during FastAPI development.

---

## DNS and IP Addresses

### What Is an IP Address?

An IP address identifies a network interface or destination in IP-based communication.

Example IPv4 address:

```text
192.168.1.10
```

Example IPv6 address:

```text
2001:db8::1
```

Computers use IP addresses to route network traffic.

### What Is DNS?

DNS stands for **Domain Name System**.

DNS helps translate human-readable domain names into information needed to locate network services.

For example:

```text
example.com
```

may resolve to one or more IP addresses.

### DNS Resolution Flow

```text
Browser
   |
   | Domain Name
   v
DNS Resolution
   |
   | IP Address
   v
Browser Connects to Server
```

### Why Is DNS Important?

Humans can remember:

```text
example.com
```

more easily than numerical IP addresses.

DNS makes internet services easier to locate and manage.

---

## Ports and Localhost

### What Is a Port?

A port is a logical number used by transport protocols to identify communication endpoints.

A computer can run multiple network services simultaneously.

Ports help incoming traffic reach the appropriate service.

### Common Ports

| Port | Common Usage |
|---|---|
| 80 | HTTP |
| 443 | HTTPS |
| 5432 | PostgreSQL |
| 3306 | MySQL |
| 8000 | Common development server port |
| 8080 | Alternative HTTP port |

A port number does not guarantee which application is running on it.

### What Is Localhost?

`localhost` is a hostname that normally resolves to a loopback address.

Common loopback addresses:

```text
127.0.0.1
::1
```

These refer to the local machine.

### Example

```text
http://127.0.0.1:8000
```

Components:

```text
http        -> Scheme
127.0.0.1   -> Loopback IP Address
8000        -> Port
```

This URL attempts to connect to a server running on your own computer.

### Localhost vs Public Server

| Localhost | Public Server |
|---|---|
| Refers to the local machine | Can be accessible over a network |
| Common during development | Common in deployment |
| Does not require internet access | Accessibility depends on network configuration |
| Example: `127.0.0.1:8000` | Example: `api.example.com` |

---

## How a Browser Loads a Website

Consider the URL:

```text
https://example.com/products
```

A simplified browser request sequence is:

1. The browser parses the URL.
2. It identifies the scheme, hostname, and path.
3. It checks for cached DNS information.
4. DNS resolution occurs if required.
5. A network connection is established.
6. For HTTPS, TLS security is negotiated.
7. The browser sends an HTTP request.
8. The server processes the request.
9. The server returns an HTTP response.
10. The browser processes the response.
11. If the response contains HTML, the browser may render the page and request additional resources.

### Important Networking Detail

Modern HTTP versions can use different transport mechanisms.

| HTTP Version | Common Transport |
|---|---|
| HTTP/1.1 | TCP |
| HTTP/2 | TCP |
| HTTP/3 | QUIC over UDP |

Transport-level networking will be covered only when required for backend development.

---

## HTTP Fundamentals

HTTP stands for **Hypertext Transfer Protocol**.

It is an application-layer protocol used for communication between clients and servers.

HTTP is commonly used by:

- Websites.
- REST APIs.
- Mobile application backends.
- Cloud services.
- AI inference APIs.
- File upload services.
- Multimedia applications.

### Important Characteristics

**Request–Response Communication**

A client sends a request, and the server returns a response.

```text
Client ---- HTTP Request ----> Server

Client <--- HTTP Response ---- Server
```

**Stateless Communication**

HTTP is stateless at the protocol level.

This means HTTP does not require the server to remember previous requests to interpret the current request.

Example:

```http
GET /products HTTP/1.1
Host: api.example.com
```

and:

```http
GET /products/10 HTTP/1.1
Host: api.example.com
```

are separate requests.

Applications can still maintain sessions using:

- Cookies.
- Session identifiers.
- Authentication tokens.
- Server-side storage.

**Extensible Headers**

HTTP headers allow clients and servers to exchange additional information.

Example:

```http
Accept: application/json
```

This indicates that the client can accept JSON responses.

---

## HTTP vs HTTPS

HTTPS stands for **Hypertext Transfer Protocol Secure**.

HTTPS protects HTTP communication using TLS.

### Comparison

| Feature | HTTP | HTTPS |
|---|---|---|
| Encryption | Not provided by HTTP itself | Provided by TLS |
| Default Port | 80 | 443 |
| Confidentiality | Not inherently protected | Protected in transit |
| Integrity | Not inherently protected | Protected by TLS |
| Server Authentication | Not inherently provided | Typically uses TLS certificates |
| Production Usage | Limited use cases | Standard for public applications |

### Example

HTTP:

```text
http://example.com
```

HTTPS:

```text
https://example.com
```

### Why HTTPS Matters

Consider a login request containing credentials.

Without transport encryption, an attacker with access to the network path may be able to inspect or modify transmitted information.

HTTPS helps protect against such attacks.

**Important:** HTTPS does not automatically prevent application vulnerabilities such as SQL injection, broken authorization, or insecure file uploads.

---

## HTTP Request Structure

An HTTP request contains information describing what the client wants.

For HTTP/1.1, the general structure is:

```text
Request Line
Headers

Optional Request Body
```

The blank line separates headers from the body.

### Request Line

Example:

```http
GET /users/10 HTTP/1.1
```

| Component | Meaning |
|---|---|
| GET | HTTP method |
| `/users/10` | Request target |
| HTTP/1.1 | Protocol version |

### HTTP Methods

| Method | Common Purpose |
|---|---|
| GET | Retrieve resources |
| POST | Submit data or create resources |
| PUT | Create or replace resource state |
| PATCH | Apply partial modifications |
| DELETE | Remove resources |

Examples:

```http
GET /users HTTP/1.1
```

```http
POST /users HTTP/1.1
```

```http
PUT /users/10 HTTP/1.1
```

```http
PATCH /users/10 HTTP/1.1
```

```http
DELETE /users/10 HTTP/1.1
```

The actual behavior depends on the server implementation.

### Request Headers

Headers provide additional request information.

Common headers:

| Header | Purpose |
|---|---|
| Host | Identifies the requested host |
| Accept | Indicates acceptable response formats |
| Content-Type | Identifies the request body format |
| Authorization | Carries authentication credentials |
| User-Agent | Identifies the requesting software |

Example:

```http
GET /users HTTP/1.1
Host: api.example.com
Accept: application/json
User-Agent: ExampleClient/1.0
```

### Request Body

A request body contains data sent to the server.

It is commonly used with POST, PUT, and PATCH requests.

Example:

```http
POST /users HTTP/1.1
Host: api.example.com
Content-Type: application/json

{
    "name": "Amit",
    "email": "amit@example.com"
}
```

GET requests do not normally include request bodies.

---

## HTTP Response Structure

An HTTP response communicates the result of processing a request.

General HTTP/1.1 structure:

```text
Status Line
Response Headers

Optional Response Body
```

### Status Line

Example:

```http
HTTP/1.1 200 OK
```

| Component | Meaning |
|---|---|
| HTTP/1.1 | Protocol version |
| 200 | Status code |
| OK | Reason phrase |

### Status Code Categories

| Range | Category | Meaning |
|---|---|---|
| 100–199 | Informational | Request processing information |
| 200–299 | Success | Request succeeded |
| 300–399 | Redirection | Further action or redirection |
| 400–499 | Client Error | Request-related problem |
| 500–599 | Server Error | Server failed to fulfill request |

### Common Status Codes

| Code | Meaning | Example |
|---|---|---|
| 200 | OK | Successful retrieval |
| 201 | Created | Resource created |
| 204 | No Content | Successful operation without response body |
| 400 | Bad Request | Invalid request |
| 401 | Unauthorized | Missing or invalid authentication |
| 403 | Forbidden | Insufficient permissions |
| 404 | Not Found | Unknown resource |
| 422 | Unprocessable Content | Semantically invalid request content |
| 500 | Internal Server Error | Unexpected server failure |

### Response Headers

Common response headers:

| Header | Purpose |
|---|---|
| Content-Type | Describes the response body format |
| Content-Length | Indicates body length when supplied |
| Cache-Control | Controls caching behavior |
| Location | Identifies a related resource |
| Set-Cookie | Instructs the client to store a cookie |

Example:

```http
Content-Type: application/json
```

### Response Body

Example JSON response:

```json
{
    "id": 10,
    "name": "Amit",
    "email": "amit@example.com"
}
```

Response bodies may contain:

- JSON.
- HTML.
- Plain text.
- Images.
- Audio.
- Video.
- Binary files.

Not every response contains a body.

For example, HTTP `204 No Content` responses must not include response content.

---

## APIs and Endpoints

API stands for **Application Programming Interface**.

An API defines how software components interact.

A web API commonly exposes functionality using HTTP.

### Example: Weather Application

Request:

```http
GET /weather?city=Delhi HTTP/1.1
Host: api.example.com
```

Illustrative response:

```json
{
    "city": "Delhi",
    "temperature": 28,
    "unit": "celsius"
}
```

The frontend can use the returned data to display weather information.

### What Is an Endpoint?

An API endpoint is an address at which an API exposes an operation or resource.

Example:

```text
https://api.example.com/users
```

Components:

```text
Base URL: https://api.example.com

Path: /users
```

Common operations:

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/users` | Retrieve users |
| GET | `/users/10` | Retrieve user 10 |
| POST | `/users` | Create a user |
| PATCH | `/users/10` | Modify user information |
| DELETE | `/users/10` | Delete user 10 |

The HTTP method and path together commonly identify an API operation.

---

## JSON Data Format

JSON stands for **JavaScript Object Notation**.

It is a lightweight text-based format used to exchange structured data.

### Example

```json
{
    "id": 1,
    "name": "Ravi",
    "is_active": true,
    "skills": [
        "Python",
        "PostgreSQL",
        "FastAPI"
    ]
}
```

### JSON Data Types

| Type | Example |
|---|---|
| String | `"Python"` |
| Number | `100` |
| Boolean | `true` |
| Null | `null` |
| Array | `[1, 2, 3]` |
| Object | `{"name": "Ravi"}` |

### JSON vs Python Dictionary

JSON:

```json
{
    "active": true,
    "manager": null
}
```

Python:

```python
{
    "active": True,
    "manager": None
}
```

Important differences:

- JSON uses `true`, `false`, and `null`.
- Python uses `True`, `False`, and `None`.
- JSON object keys must be strings.
- JSON strings require double quotes.

### Why JSON Is Commonly Used

- Human-readable structure.
- Widely supported.
- Easy to parse.
- Suitable for structured API data.
- Supported by browsers and backend frameworks.

---

## Introduction to REST

REST stands for **Representational State Transfer**.

REST is an architectural style for designing distributed hypermedia systems.

RESTful APIs commonly expose resources using HTTP methods and resource-oriented URLs.

Example:

```text
GET /users
GET /users/10
POST /users
DELETE /users/10
```

However, using HTTP methods and JSON does not automatically make an API fully RESTful.

REST also defines architectural constraints.

These constraints will be studied in upcoming lessons.

### REST vs HTTP

| HTTP | REST |
|---|---|
| Communication protocol | Architectural style |
| Defines request-response semantics | Defines architectural constraints |
| Supports different API styles | Commonly implemented using HTTP |
| Not limited to REST APIs | Not itself a communication protocol |

---

## Introduction to Postman

Postman is an API development and testing tool.

It allows developers to:

- Send HTTP requests.
- Inspect responses.
- Configure request headers.
- Send JSON bodies.
- Configure authentication.
- Organize requests into collections.
- Use variables and environments.
- Write automated API tests.

### Installing Postman

1. Open the official website:

   https://www.postman.com/downloads/

2. Download the Windows desktop application.
3. Install Postman.
4. Launch the application.
5. Open a workspace and create a new HTTP request.

### Important Interface Components

| Component | Purpose |
|---|---|
| Method Selector | Choose HTTP method |
| URL Field | Enter endpoint URL |
| Params | Configure query parameters |
| Headers | Configure request headers |
| Body | Send request data |
| Authorization | Configure authentication |
| Send | Execute request |
| Response Body | Display returned data |
| Response Headers | Inspect metadata |
| Status | Display HTTP status |
| Time | Display request duration |

### Example Public API

Method:

```http
GET
```

URL:

```text
https://jsonplaceholder.typicode.com/users/1
```

The endpoint normally returns sample user information in JSON format.

Expected successful status:

```http
200 OK
```

The practical assignment will use Postman to test your own local HTTP server.

---

## Browser Developer Tools

Modern browsers provide tools for inspecting HTTP communication.

In Google Chrome, these tools are available through **Developer Tools**.

### Opening Developer Tools

Press:

```text
F12
```

or:

```text
Ctrl + Shift + I
```

Select the **Network** tab.

### Inspecting Requests

1. Open a website.
2. Open Developer Tools.
3. Select Network.
4. Refresh the page.
5. Select a network request.
6. Inspect its details.

Important information includes:

- Request URL.
- HTTP method.
- Status code.
- Request headers.
- Response headers.
- Response body.
- Timing information.

### Postman vs Browser DevTools

| Postman | Browser DevTools |
|---|---|
| Manually construct API requests | Inspect browser network activity |
| Test different HTTP methods | Analyze actual browser requests |
| Configure request bodies | Inspect browser response content |
| Organize requests into collections | Debug frontend-backend communication |
| Automate API tests | Analyze browser networking and loading |

Both tools will be used throughout the FastAPI learning roadmap.

---

# PART B — PRACTICAL ASSIGNMENT

---

## Project Overview

**Project Name:** Local HTTP API Server

**Difficulty:** Beginner

**Estimated Duration:** 40–60 Minutes

**Language:** Python

**Library:** Python Standard Library — `http.server`

**API Testing Tool:** Postman

**Development Environment:** PyCharm / VS Code

### Project Description

Develop a small Python application that runs a local HTTP server.

The server must accept HTTP GET requests and return JSON responses.

After implementing the server, use Postman to test the endpoints and inspect the communication.

This project demonstrates how a client communicates with a server before introducing FastAPI.

> **Important:** Python's `http.server` is suitable for this local educational exercise. It is not recommended for production deployment.

---

## Project Objective

Build a local HTTP API capable of:

- Listening for incoming HTTP requests.
- Identifying requested URL paths.
- Processing GET requests.
- Returning valid JSON responses.
- Sending appropriate HTTP status codes.
- Returning useful response headers.
- Handling unknown endpoints.
- Communicating with Postman as an HTTP client.

By completing this project, you should understand the basic request-response lifecycle from both the client and server perspectives.

---

## Functional Requirements

The application must implement the following endpoints.

| Method | Endpoint | Purpose | Expected Status |
|---|---|---|---|
| GET | `/` | Return welcome message | 200 |
| GET | `/health` | Return server health information | 200 |
| GET | `/info` | Return application information | 200 |
| GET | `/unknown` | Return an error for an undefined route | 404 |

### Welcome Endpoint

**Method:**

```http
GET
```

**Path:**

```text
/
```

Expected JSON:

```json
{
    "message": "Welcome to Daily FastAPI Practice"
}
```

Expected status:

```http
200 OK
```

### Health Endpoint

**Method:**

```http
GET
```

**Path:**

```text
/health
```

Expected JSON:

```json
{
    "status": "healthy"
}
```

Expected status:

```http
200 OK
```

### Information Endpoint

**Method:**

```http
GET
```

**Path:**

```text
/info
```

Expected JSON:

```json
{
    "application": "Local HTTP API",
    "language": "Python",
    "day": 1
}
```

Expected status:

```http
200 OK
```

### Unknown Endpoint

**Method:**

```http
GET
```

**Path:**

```text
/unknown
```

Expected JSON:

```json
{
    "error": "Endpoint not found"
}
```

Expected status:

```http
404 Not Found
```

---

## Project Structure

Create the following files:

```text
D1_171026(SAT)/
│
├── Concepts.md
├── Tasks_Completed.md
├── mistakes.md
│
└── practical/
    │
    ├── server.py
    │
    └── screenshots/
        ├── welcome.png
        ├── health.png
        ├── info.png
        ├── not_found.png
        └── browser_network.png
```

The screenshot files should be created after completing the tests.

---

## Implementation Guidelines

Use Python's built-in `http.server` module.

You should implement the server independently.

### Required Modules

Explore the following modules:

```python
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
```

### Required Concepts

Your implementation should demonstrate:

- Creating a custom request handler.
- Handling GET requests.
- Reading the requested path.
- Returning different responses based on the path.
- Serializing Python dictionaries into JSON.
- Sending HTTP status codes.
- Setting the `Content-Type` header.
- Writing response content.
- Starting a local HTTP server.

### Suggested Implementation Flow

1. Import the required modules.
2. Define a custom class inheriting from `BaseHTTPRequestHandler`.
3. Implement the `do_GET()` method.
4. Read the requested path.
5. Match the path against supported endpoints.
6. Prepare the appropriate Python dictionary.
7. Convert the dictionary to JSON.
8. Send the correct HTTP status.
9. Set the response Content-Type to `application/json`.
10. Write the JSON response to the client.
11. Start the HTTP server on port `8000`.

### Important Constraints

- Do not use FastAPI or Flask for this exercise.
- Do not use external packages.
- Use valid JSON responses.
- Return HTTP 404 for unsupported paths.
- Use `127.0.0.1` as the listening address.
- Handle only GET requests for now.
- Keep the implementation simple and readable.

The purpose is to understand HTTP communication, not to build a production framework.

---

## Running the Application

Open the project in PyCharm or VS Code.

Navigate to the practical directory.

Example:

```powershell
cd "D1_171026(SAT)\practical"
```

Start the application:

```powershell
python server.py
```

Your server should listen at:

```text
http://127.0.0.1:8000
```

You may display a startup message such as:

```text
HTTP Server running at http://127.0.0.1:8000
```

Keep the terminal running while testing the endpoints.

### Stopping the Server

Press:

```text
Ctrl + C
```

This interrupts the running server process.

---

## Testing with Postman

### Create a Collection

Open Postman and create a collection named:

```text
Daily FastAPI Practice
```

Inside it, organize the Day 01 requests.

Suggested collection structure:

```text
Daily FastAPI Practice
│
└── Day 01 - HTTP Fundamentals
    │
    ├── GET - Welcome
    ├── GET - Health
    ├── GET - Info
    └── GET - Unknown
```

### Test the Welcome Endpoint

Method:

```http
GET
```

URL:

```text
http://127.0.0.1:8000/
```

Verify:

- Status is `200 OK`.
- Response contains the welcome message.
- Response body is valid JSON.
- Content-Type is `application/json`.

### Test the Health Endpoint

Method:

```http
GET
```

URL:

```text
http://127.0.0.1:8000/health
```

Verify:

- Status is `200 OK`.
- Response contains `"status": "healthy"`.
- Response body is valid JSON.

### Test the Information Endpoint

Method:

```http
GET
```

URL:

```text
http://127.0.0.1:8000/info
```

Verify:

- Status is `200 OK`.
- Response contains application information.
- JSON fields are correctly formatted.

### Test the Unknown Endpoint

Method:

```http
GET
```

URL:

```text
http://127.0.0.1:8000/unknown
```

Verify:

- Status is `404 Not Found`.
- Response contains an error message.
- Response body is valid JSON.

### Browser Network Inspection

After testing with Postman:

1. Open Chrome.
2. Navigate to:

   ```text
   http://127.0.0.1:8000/health
   ```

3. Press `F12`.
4. Open the Network tab.
5. Refresh the page.
6. Select the `/health` request.
7. Inspect the request and response details.

Record:

- Request URL.
- Request method.
- Status code.
- Response Content-Type.
- Response body.

Compare the results with Postman.

---

## Expected Results

After successful implementation:

- The Python server should start without errors.
- The server should accept GET requests on port `8000`.
- Each defined endpoint should return its corresponding JSON response.
- Unsupported endpoints should return HTTP 404.
- Postman should display the correct response status.
- Chrome should successfully communicate with the local server.
- The response Content-Type should be `application/json`.

### Expected Endpoint Summary

| Endpoint | Status | Result |
|---|---|---|
| `/` | 200 | Welcome message |
| `/health` | 200 | Health information |
| `/info` | 200 | Application metadata |
| `/unknown` | 404 | Error response |

---

## Acceptance Criteria

The project is complete when:

- [ ] The Python HTTP server starts successfully.
- [ ] The server listens on `127.0.0.1:8000`.
- [ ] The welcome endpoint returns HTTP 200.
- [ ] The health endpoint returns HTTP 200.
- [ ] The information endpoint returns HTTP 200.
- [ ] Unknown endpoints return HTTP 404.
- [ ] Every response contains valid JSON.
- [ ] The correct Content-Type header is returned.
- [ ] All four endpoints are tested using Postman.
- [ ] The requests are saved in a Postman collection.
- [ ] At least one request is inspected using Chrome DevTools.
- [ ] Screenshots of successful tests are saved.
- [ ] Implementation and testing results are documented.

---

## Submission Requirements

After completing the practical assignment, provide:

**Source Code**

```text
practical/server.py
```

**Postman Screenshots**

```text
practical/screenshots/welcome.png
practical/screenshots/health.png
practical/screenshots/info.png
practical/screenshots/not_found.png
```

**Browser Screenshot**

```text
practical/screenshots/browser_network.png
```

**Documentation**

```text
Tasks_Completed.md
```

The completion document should contain:

- Project objective.
- Implemented endpoints.
- Implementation summary.
- Testing results.
- Problems encountered.
- Solutions applied.
- Final completion status.

Record debugging mistakes separately in:

```text
mistakes.md
```

Do not mark tasks as completed until they have been implemented and verified.

---

# REFERENCES

---

## Official Learning Resources

### HTTP and Web Fundamentals

- [MDN — HTTP Overview](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview)
- [MDN — HTTP Messages](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Messages)
- [MDN — HTTP Methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods)
- [MDN — HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status)

### Python HTTP Server

- [Python — http.server Documentation](https://docs.python.org/3/library/http.server.html)
- [Python — json Module](https://docs.python.org/3/library/json.html)

### API Testing

- [Postman Learning Center](https://learning.postman.com/)
- [JSONPlaceholder](https://jsonplaceholder.typicode.com/)

### Future FastAPI Development

- [FastAPI Official Documentation](https://fastapi.tiangolo.com/)

---

# DAY 01 COMPLETION CHECKLIST

## Theory — Concepts Covered / Revised

- [ ] Client-server architecture
- [ ] Frontend, backend, and database
- [ ] HTTP request-response lifecycle
- [ ] URL structure
- [ ] DNS and IP addresses
- [ ] Ports and localhost
- [ ] Browser request lifecycle
- [ ] HTTP fundamentals
- [ ] HTTP vs HTTPS
- [ ] HTTP request structure
- [ ] HTTP response structure
- [ ] APIs and endpoints
- [ ] JSON data format
- [ ] REST introduction
- [ ] Postman fundamentals
- [ ] Browser Developer Tools

## Practical — Project Completion

- [ ] Created the local HTTP server.
- [ ] Implemented all required GET endpoints.
- [ ] Implemented JSON responses.
- [ ] Implemented HTTP 404 handling.
- [ ] Tested all endpoints in Postman.
- [ ] Inspected HTTP communication in Chrome.
- [ ] Saved the required screenshots.
- [ ] Documented completed tasks and results.

---

## Day 01 Summary

Today's focus is understanding how clients and servers communicate over HTTP.

The practical project reinforces the concepts by implementing a simple HTTP server and testing it with Postman.

After completing this session, you should understand:

- How an HTTP server receives requests.
- How URL paths identify requested operations.
- How a server prepares responses.
- How HTTP status codes communicate results.
- How JSON is exchanged between clients and servers.
- How Postman and browser tools help inspect API communication.

**Next Session:** Day 02 — REST Architecture, HTTP Methods, Safe and Idempotent Operations, and Resource-Oriented API Design.

> **Progress Status:** Pending evaluation.  
> **Documentation:** Update `Tasks_Completed.md` after verifying the implementation.
>
> **End of Day 01 — Concepts.md**