# API Test Framework
![Python](https://img.shields.io/badge/python-3.13-blue?logo=python&logoColor=white)
![PyTest](https://img.shields.io/badge/pytest-8.3.5-orange?logo=pytest&logoColor=white)
![Build](https://img.shields.io/badge/build-passing-brightgreen)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)

## Overview

This project is a professional API testing framework using Python and PyTest. It includes:

* Automated API tests with verbose output

* JSON snapshots for QA evidence

* HTML reports for human-readable, portfolio-ready results

* JUnit XML reports for CI/CD integration

* Markdown-style test titles and descriptions for clarity

This setup demonstrates real-world QA best practices and is designed for both local testing and CI/CD pipelines.

## Project Structure
````
API-Test-Framework/
│
├─ utils/
│   ├─ api_helpers.py       # API helper functions (e.g., get_users)
│   └─ validators.py        # Validators (e.g., is_valid_email)
├─ tests/
│   ├─ test_users.py        # PyTest test cases
│   └─ snapshots/           # JSON snapshots saved per test
├─ reports/                 # HTML and JUnit XML reports
└─ pytest.ini (optional)
````
## Setup
### 1. Python Environment

* Python 3.13+ recommended

* Install dependencies (terminal):
```Bash
pip install pytest pytest-html
```

* Optional: pytest-asyncio if testing asynchronous APIs

### 2. Handling Python Path

To ensure Python can find the utils module:

**Option A – Temporary for terminal** (OS Powershell/Pycharm Terminal):
```Powershell
cd "C:\Users\bgroo\PycharmProjects\API-Test-Framework"
$env:PYTHONPATH="${PWD}"
``` 
**Option B – Permanent for PyCharm terminal** :

Use a .env file in project root:
```Bash
PYTHONPATH=C:\Users\YourUserName\PycharmProjects\API-Test-Framework
```

Configure **Run/Debug Configurations → Environment → Env File** in PyCharm.

This allows the framework to import helper modules correctly in both the terminal and UI.

## Running Tests
### From PyCharm UI

1. Run/Debug Configurations → + → Python tests → pytest

2. Target: tests/ folder or project root

3. Working directory: project root

4. Additional arguments:
```` Plain text
-v --html=reports/report.html --self-contained-html --junitxml=reports/junit-report.xml
````
5. **Environment vairables:** set PYTHONPATH as above if necessary
6. Click **Run**

## From Terminal/PowerShell
```Power Shell
cd "C:\Users\bgroo\PycharmProjects\API-Test-Framework"
$env:PYTHONPATH="${PWD}"
pytest -v --html=reports/report.html --self-contained-html --junitxml=reports/junit-report.xml
````
## Docker Validation

All API tests are fully containerized using Docker, allowing reproducible test execution and report generation.

### **Prerequisites**
- Docker installed on your machine
- Optional: PowerShell or terminal access

### **Build Docker Image**
Run from project root:

```powershell
docker buildx build -t api-test-framework .
```
### Run Tests in Docker

This executes all tests in tests/ and generates HTML & JUnit reports, plus JSON snapshots:

docker run --rm `
  -e PYTHONPATH=/app `
  -v ${PWD}/reports:/app/reports `
  -v ${PWD}/tests/snapshots:/app/tests/snapshots `
  api-test-framework

**Explanation:**

`PYTHONPATH=/app` → ensures Python can import utils/ and config/.

`reports/` → HTML report and JUnit XML are persisted to host machine.

`tests/snapshots/` → JSON snapshots of API responses are saved for QA validation.

### Output
* HTML report: `reports/report.html`

* JUnit XML report: `reports/junit-report.xml`

* Snapshots: `tests/snapshots/*.json`
  
*This setup ensures portable, reproducible testing for QA, development, and CI/CD pipelines.*


## Features

### 1. Verbose Test Output
* Use -v to show file name, function name, and pass/fail status in console.

### 2. Snapshots

* Tests save JSON snapshots of API responses to tests/snapshots/.

* Snapshots are also embedded inline in the HTML report for QA review.

### 3. HTML Report

* Generated in reports/report.html

* Human-readable, includes:

    * Test titles and descriptions (Markdown)

    * Inline JSON snapshots

    * Pass/fail color coding
  
## **HTML SnapShot**

![API-Test-Framework-Report.png](tests/snapshots/API-Test-Framework-Report.png)

*Snapshot of PyTest HTML report showing test results and embedded snapshots.*

### 4. JUnit XML Report

* Generated in `reports/junit-report.xml`

* Compatible with CI/CD pipelines (Jenkins, GitHub Actions, GitLab, etc.)

## QA-Friendly Test Data Matrix

| Test Case | API Endpoint | Input / Params | Expected Output | Snapshot / Notes |
|-----------|-------------|----------------|----------------|-----------------|
| `test_get_users_status_code` | `/users` | None | HTTP **200 OK** | Snapshot of full user list saved in `snapshots/` |
| `test_get_users_length` | `/users` | None | **10 users** returned | JSON snapshot shows array of 10 user objects |
| `test_user_fields` | `/users` | None | Each user object contains: `id`, `name`, `email` | Snapshot highlights missing or invalid fields if test fails |
| `test_all_user_emails_are_valid` | `/users` | None | All `email` fields are valid format | Snapshot shows invalid emails if any exist |
| `test_user_1_name_is_leanne_graham` | `/users/1` | `id=1` | `name` equals `"Leanne Graham"` | Snapshot stores single user object for verification |


### Best Practices

* Keep snapshots/ and reports/ in version control only if suitable for portfolio/demo.

* Use Markdown-style labels in test docstrings for clarity (python):

```Python
"""
# Title: Verify Users Endpoint Status Code
# Description: Ensure the /users endpoint responds with HTTP 200 OK.
"""
```
* Use `save_snapshot(name, data, request)` to save API responses and attach them to HTML report.

* Always run tests from the project root to avoid import errors.


## CI/CD Integration

* **JUnit XML** allows pipelines to parse test results automatically

* HTML reports can be archived for QA review

* Snapshots provide historical API response verification

## Author

**Byron McDowell**  

- LinkedIn: [linkedin.com/in/byron-mcdowell](https://www.linkedin.com/in/byron-mcdowell)  
- GitHub: [github.com/byron-mcdowell](https://github.com/byron-mcdowell)  

Feel free to connect or explore more of my projects.
## License

This project is licensed under the [MIT License](./LICENSE).  
See the `LICENSE` file for full details.

![License](https://img.shields.io/badge/license-MIT-blue)




