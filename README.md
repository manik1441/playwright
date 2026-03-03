# QA Test Automation Framework

A unified framework for UI, API, and Database testing using Playwright, Requests, and SQLite, orchestrated by Pytest.

## Features
* **UI Testing:** Playwright with Page Object Model (POM).
* **API Testing:** `requests` library with Facade pattern.
* **DB Testing:** `sqlite3` and `pandas` for data validation.
* **Parallel Execution:** Fast execution using `pytest-xdist`.
* **Reporting:** HTML reports via `pytest-html`.
* **Containerization:** Docker support for consistent environments.

## Setup Instructions

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   playwright install chromium
2. **Run Tests:**  
    Run all tests: pytest
    Run tests in parallel: pytest -n auto
    Run specific marker: pytest -m ui
3. **Run with Docker:**

    docker build -t qa-framework.

    docker run -v $(pwd)/reports:/app/reports qa-framework