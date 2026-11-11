# Day 13: Notes & Developer English Practice

## Topic: HTTP Requests, REST APIs, Status Codes & API Documentation

---

## 1. Key Concepts & Architecture Mastered

### HTTP Status Code Ranges
- **`2xx` (Success):** Request succeeded (e.g. `200 OK`, `201 Created`).
- **`4xx` (Client Errors):** Problems caused by the client request (e.g. `400 Bad Request`, `401 Unauthorized`, `404 Not Found`, `429 Rate Limit`).
- **`5xx` (Server Errors):** Failures occurring on the remote server host (e.g. `500 Internal Server Error`, `502 Bad Gateway`, `503 Unavailable`).

### Serialization vs. Deserialization in APIs
- The API response body over the wire is a raw UTF-8 serialized byte/JSON string.
- Calling `response.json()` deserializes that payload directly into a native Python `dict` or `list`.

### Network Timeouts & Thread Blocking
- By default, `requests.get()` without a timeout will block execution indefinitely if a server accepts a socket connection but never responds.
- Specifying `timeout=5` guarantees that after 5 seconds, a `requests.exceptions.Timeout` exception is raised, allowing graceful failure.

---

## 2. Professional Developer English: API Integration Documentation

### Student's Raw Draft:
> **Function:** fetch_github_user(username)  
> **Method & Endpoint:** GET, https://api.github.com/users/{username}  
> **Parameters:** Username : string  
> **Success Response (200 OK):** Python Dict  
> **Error Handling:** Return None and Print Error  

### Polished Version (For OpenAPI / Team Documentation):
```markdown
### `fetch_github_user(username: str) -> dict | None`

#### Overview:
Retrieves publicly available profile metadata for a specified GitHub user account via the GitHub REST API.

- **HTTP Method:** `GET`
- **Endpoint:** `https://api.github.com/users/{username}`
- **Path Parameters:**
  - `username` (*string, required*): The unique GitHub username handle.
- **Request Headers:**
  - `Accept: application/vnd.github.v3+json`
- **Success Response (`200 OK`):**
  - Returns a dictionary representing the user profile (`name`, `bio`, `public_repos`, `followers`, `html_url`).
- **Error Scenarios:**
  - **`404 Not Found`:** Returned when the username does not exist; function reports user missing and returns `None`.
  - **`403 / 429 Rate Limited`:** Returned when unauthenticated request quotas are exhausted; function logs warning and returns `None`.
  - **Network / Timeout Failure:** Catches `requests.exceptions.RequestException` gracefully, preventing application crash.
```

---

## 3. High-Value Tech Vocabulary Learned
- **Client vs Server Errors:** 4xx (client-side fault) vs 5xx (server-side fault).
- **Socket / Connection Timeout:** Maximum duration allowed to establish or read from an HTTP connection before aborting.
- **Payload:** The core data sent or received in an HTTP message body, excluding headers.
- **Idempotent:** An HTTP operation (like `GET`) that can be executed multiple times without changing the server's state.

