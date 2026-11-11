# Day 13: HTTP Requests, REST APIs, Status Codes & Error Handling

## Learning Objectives
1. How HTTP works: Request Methods (`GET`, `POST`), Status Codes (`200`, `400`, `404`, `429`, `500`).
2. The `requests` library: `response.status_code`, `response.json()`, query parameters `params={...}`.
3. Network defensive engineering: setting timeouts (`timeout=5`) and handling connection errors (`requests.exceptions.RequestException`).
4. Why API communication is the backbone of AI engineering (LLM APIs, embedding endpoints, webhooks).

---

## Daily Task: CLI GitHub & Weather Data Fetcher (Without AI)
Build a resilient CLI tool that:
1. Prompts user for a GitHub username (e.g. `khorshedcodes` or `torvalds`).
2. Calls the public GitHub REST API: `https://api.github.com/users/{username}`.
3. Handles all edge cases gracefully:
   - Status 200: extracts and displays name, bio, public repo count, follower count, and account creation date.
   - Status 404: prints `"User not found. Please verify username."`
   - Status 403 / 429: prints `"Rate limit exceeded. Try again later."`
   - Connection/Timeout error: catches `requests.exceptions.RequestException` and displays a clean error (no crashes!).
4. Uses modular functions and type hints.

---

## Developer English Task: API Integration Documentation
Write clear technical documentation for your fetcher function following industry API docs format:
- Endpoint URL & Method
- Request Parameters & Headers
- Success Response Schema
- Error Scenarios

