# API Test Framework for User Service

## Overview

This project is a robust automated API testing framework developed in Python to validate the functionality, reliability, and data integrity of RESTful API endpoints related to user management. It ensures the API meets expected behavior by verifying response status codes, data structure, and content validation, such as email formats.

The framework is built with best practices for maintainability, scalability, and ease of extension, making it suitable for real-world QA automation needs.

---

## Key Features

- Comprehensive testing of REST API endpoints including status codes and response payload validation
- Validation of critical data fields and formats (e.g., email addresses)
- Modular design separating API request logic and validation utilities
- Uses `pytest` for expressive and concise test definitions without boilerplate code
- Easily extensible to add new endpoints, test cases, and validators
- Designed for integration into CI/CD pipelines and automated testing workflows

---

## Skills Demonstrated

This project showcases proficiency in:

- **Python programming**: Writing clear, maintainable test code and utility modules
- **API testing**: Using `requests` to interact with RESTful services and validate responses
- **Test automation frameworks**: Implementing test cases using `pytest` including assertions and fixtures
- **Data validation**: Creating and using custom validators such as email format checking
- **Code organization**: Modularizing code for separation of concerns and reusability
- **Version control & collaboration**: Organizing project structure and documentation for team use
- **Continuous Integration**: Ready to integrate with CI pipelines for automated regression testing

---

## Prerequisites

- Python 3.10 or higher
- `requests` library for HTTP calls
- `pytest` for running tests

Dependencies can be installed via:

```bash
pip install -r requirements.txt
```
## Setup and Configuration
1. Clone the repository
```bash
git clone https://github.com/yourusername/api-test-framework.git

cd api-test-framework
```
2. Install dependencies

```bash
pip install -r requirements.txt
```

## Configure your environment

Modify the settings.py file to specify:

* BASE_URL: The base URL of the API under test (e.g., https://jsonplaceholder.typicode.com)

* Any authentication tokens or headers if required by your API

Example:

python
```bash
BASE_URL = "https://jsonplaceholder.typicode.com"
```

## Running the Tests
Run all tests with:

```bash
pytest
```
Run tests from a specific file:
```bash
pytest tests/test_users.py
```
Verbose output can be enabled with:

```bash
pytest -v
```

Project Structure
```bash
api-test-framework/
│
├── tests/                    # Test files organized by resource or feature
│   ├── test_users.py         # Tests related to User API endpoints
│   └── ...                  
│
├── utils/                    # Utility modules
│   ├── api_helpers.py        # Functions to call API endpoints (e.g., get_users)
│   └── validators.py         # Custom validation functions (e.g., is_valid_email)
│
├── settings.py               # Configuration file for API base URLs and tokens
├── requirements.txt          # Python dependencies list
└── README.md                 # Project documentation
```
Example Test Case
```bash
def test_all_user_emails_are_valid():
    response = get_users()
    users = response.json()
    for user in users:
        assert is_valid_email(user['email']), f"Invalid email found: {user['email']}"      
```
Extending the Framework

* Add new API tests: Create new test files or functions in the tests directory targeting additional endpoints or edge cases.

* Enhance validators: Implement more comprehensive validation utilities (e.g., JSON schema validation).

* Implement fixtures: Use pytest fixtures to manage test setup and teardown, e.g., for authentication tokens or test data preparation.

* Integrate CI/CD: Connect the framework with CI tools like GitHub Actions, Jenkins, or Travis CI for automated test runs on each commit.

* Add reporting: Incorporate test reporting tools or plugins for enhanced test result visualization.

### Terminal Usage

To run the automated tests from the command line, follow these steps:

Open your terminal or command prompt.

Navigate to the root folder of the project where run_testcli.py is located. For example:

```bash
cd path/to/your/project/root
```

Run the test CLI script using Python:

```bash
python run_testcli.py
```
This will execute all the tests in the project and display the results directly in your terminal.
## Contributing
Contributions and improvements are welcome! Please fork the repo and submit pull requests for review.

## Contact
Byron McDowell  
Email: [bgroot2021@gmail.com](mailto:bgroot2021@gmail.com)  
GitHub: [github.com/blmcdowe](https://github.com/blmcdowe)  
LinkedIn: [linkedin.com/in/byronmcdowell](https://linkedin.com/in/byronmcdowell)


## License

This project is licensed under the MIT License:

MIT License

Copyright (c) 2025 Byron McDowell

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.




---





