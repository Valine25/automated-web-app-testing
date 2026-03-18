# Automated Healthcare Web Application Testing Framework

A structured Selenium-based automation testing framework built using Python.  
This project demonstrates automated UI testing with reusable components and the Page Object Model (POM) design pattern.

---

## Overview

This framework automates testing of web applications by simulating real user interactions such as login, form submission, and validation checks.  
It is designed to ensure reliability and correctness of web application workflows.

The project follows industry best practices like modular design and separation of concerns using Page Object Model.

---

## Features

- Automated UI testing using Selenium WebDriver
- Page Object Model (POM) implementation
- Reusable driver setup
- Multiple test cases (valid and invalid scenarios)
- Assertion-based validation
- Structured and maintainable codebase

---

## Tech Stack

- Python
- Selenium WebDriver
- Pytest

---

## Project Structure
automated-website-testing
│
├── tests
│ └── test_login.py
│
├── pages
│ └── login_page.py
│
├── utils
│ └── driver_setup.py
│
└── Readme.md


---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/automated-web-app-testing.git
cd automated-website-testing
```
### 2. Install dependencies
```bash
pip install selenium pytest
```
### 3. Run tests
```bash 
pytest 
```

---

### Test Cases

- Valid Login Test
- Invalid Login Test
- Each test verifies expected behavior using assertions.