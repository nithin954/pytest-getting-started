# Pytest Complete Learning Guide

A comprehensive guide to Pytest, Playwright integration, reporting, fixtures, parallel execution, and CI/CD best practices.

---

# Table of Contents

1. Introduction to Pytest
2. Test Discovery Rules
3. Running Tests
4. Assertions
5. Running Specific Tests
6. Fixtures
7. Fixture Scopes
8. Fixture Parameters
9. Parametrization
10. conftest.py
11. Markers
12. pytest.ini Configuration
13. Skip, SkipIf and XFail
14. Parallel Execution with pytest-xdist
15. HTML Reports
16. Playwright Integration
17. CI/CD Integration
18. Interview Questions

---

# 1. Introduction to Pytest

Pytest is a powerful Python testing framework used for:

* Unit Testing
* Functional Testing
* API Testing
* UI Automation Testing
* Playwright Automation
* Selenium Automation

## Advantages

* Simple syntax
* Rich plugin ecosystem
* Powerful fixtures
* Parametrization support
* Parallel execution
* HTML reporting
* CI/CD integration

---

# 2. Test Discovery Rules

Pytest automatically discovers tests based on naming conventions.

## Test File Naming

Valid:

```python
test_login.py
login_test.py
```

Invalid:

```python
login.py
sample.py
```

## Test Function Naming

```python
def test_login():
    pass
```

## Test Class Naming

```python
class TestLogin:
    pass
```

## Discovery Flow

```text
pytest
   ↓
Find Files
   ↓
Find Classes
   ↓
Find Functions
   ↓
Execute Tests
```

---

# 3. Running Tests

Run all tests:

```bash
pytest
```

Run specific file:

```bash
pytest test_login.py
```

Verbose mode:

```bash
pytest -v
```

Verbose + Print Statements:

```bash
pytest -vs
```

Common options:

| Option | Description           |
| ------ | --------------------- |
| -v     | Verbose output        |
| -s     | Show print statements |
| -k     | Run tests by keyword  |
| -m     | Run tests by marker   |
| -n     | Run tests in parallel |

---

# 4. Assertions

Assertions validate expected outcomes.

```python
def test_addition():
    assert 1 + 1 == 2
```

Custom message:

```python
assert a == b, "Values are not equal"
```

Result indicators:

```text
.  -> Pass
F  -> Fail
```

Example:

```text
..F..
```

---

# 5. Running Specific Tests

Run a function:

```bash
pytest test_sample.py::test_login
```

Run a class:

```bash
pytest test_sample.py::TestLogin
```

Run a method:

```bash
pytest test_sample.py::TestLogin::test_valid_login
```

Run using keyword:

```bash
pytest -k "login"
```

Run multiple conditions:

```bash
pytest -k "login and not logout"
```

---

# 6. Fixtures

## What is a Fixture?

A fixture provides reusable setup and teardown functionality.

Example:

```python
import pytest

@pytest.fixture
def setup():

    print("Before Test")

    yield

    print("After Test")
```

## Yield Lifecycle

```text
Setup
   ↓
yield
   ↓
Test Execution
   ↓
Cleanup
```

## Autouse Fixture

```python
@pytest.fixture(autouse=True)
def setup():
    print("Runs Automatically")
```

---

# 7. Fixture Scopes

| Scope    | Lifetime         |
| -------- | ---------------- |
| function | Per test         |
| class    | Per class        |
| module   | Per module       |
| package  | Per package      |
| session  | Entire execution |

Example:

```python
@pytest.fixture(scope="session")
def browser():
    pass
```

---

# 8. Fixture Parameters

```python
@pytest.fixture(params=["Chrome", "Edge"])
def browser(request):
    return request.param
```

Example:

```python
def test_browser(browser):
    print(browser)
```

---

# 9. Parametrization

```python
import pytest

@pytest.mark.parametrize(
    "num,result",
    [
        (1,1),
        (2,4),
        (3,9)
    ]
)
def test_square(num, result):
    assert num**2 == result
```

Benefits:

* Less duplicate code
* Data-driven testing
* Better maintainability

---

# 10. conftest.py

## What is conftest.py?

A special pytest file used for:

* Shared fixtures
* Hooks
* Global configuration

Example:

```python
# conftest.py

import pytest

@pytest.fixture
def browser():
    yield "Chrome"
```

Usage:

```python
def test_login(browser):
    print(browser)
```

No import required.

---

# 11. Markers

Markers help group tests.

## Smoke Tests

```python
@pytest.mark.smoke
def test_login():
    pass
```

Execute:

```bash
pytest -m smoke
```

## Regression Tests

```python
@pytest.mark.regression
def test_checkout():
    pass
```

Execute:

```bash
pytest -m regression
```

## Smoke vs Regression

| Smoke Testing          | Regression Testing |
| ---------------------- | ------------------ |
| Critical functionality | Full validation    |
| Fast execution         | Longer execution   |
| Small subset           | Complete suite     |
| Every build            | Release/Nightly    |

---

# 12. pytest.ini Configuration

## What is pytest.ini?

A project-level configuration file that controls default pytest behavior.

Project Structure:

```text
project/
│
├── pytest.ini
├── conftest.py
├── tests/
└── src/
```

## Recommended Configuration

```ini
[pytest]

addopts =
    -vs
    --tb=short
    --html=reports/report.html
    --self-contained-html

markers =
    smoke: Smoke test cases
    regression: Regression test cases

python_files =
    test_*.py
    *_test.py

python_classes = Test*

python_functions = test_*
```

## Explanation

### addopts

Default pytest arguments.

```ini
addopts = -vs
```

Equivalent to:

```bash
pytest -vs
```

### markers

Registers custom markers.

```ini
markers =
    smoke: Smoke test cases
    regression: Regression test cases
```

### python_files

Controls file discovery.

```ini
python_files =
    test_*.py
    *_test.py
```

### python_classes

Controls class discovery.

```ini
python_classes = Test*
```

### python_functions

Controls function discovery.

```ini
python_functions = test_*
```

### HTML Report Settings

```ini
--html=reports/report.html
--self-contained-html
```

Automatically generates:

```text
reports/
└── report.html
```

---

# 13. Skip, SkipIf and XFail

## Skip

```python
@pytest.mark.skip(reason="Feature not ready")
```

## SkipIf

```python
import sys

@pytest.mark.skipif(sys.platform == "win32")
```

## XFail

```python
@pytest.mark.xfail(reason="Known Defect")
```

---

# 14. Parallel Execution with pytest-xdist

Install:

```bash
pip install pytest-xdist
```

Run with 4 workers:

```bash
pytest -n 4
```

Auto-detect CPUs:

```bash
pytest -n auto
```

Example:

```text
Worker 1 -> Test A
Worker 2 -> Test B
Worker 3 -> Test C
Worker 4 -> Test D
```

Benefits:

* Faster execution
* Reduced CI runtime

---

# 15. HTML Reports

Install:

```bash
pip install pytest-html
```

Generate report:

```bash
pytest --html=reports/report.html --self-contained-html
```

Benefits:

* Detailed execution summary
* Pass/Fail statistics
* Easy sharing

---

# 16. Playwright Integration

Install:

```bash
pip install pytest-playwright
playwright install
```

## Fixture Example

```python
from playwright.sync_api import Playwright, expect
import pytest

@pytest.fixture
def setup(playwright: Playwright):

    browser = playwright.chromium.launch()

    context = browser.new_context()

    page = context.new_page()

    page.goto("https://google.com")

    yield page

    browser.close()
```

Usage:

```python
def test_title(setup):
    expect(setup).to_have_title("Google")
```

## Built-in Page Fixture

```python
def test_google(page):
    page.goto("https://google.com")
```

No custom fixture required.

## Class Fixture Example

```python
@pytest.fixture(scope="class")
def init_browser(request, playwright):

    browser = playwright.chromium.launch()

    page = browser.new_page()

    request.cls.page = page

    yield

    browser.close()
```

## usefixtures Example

```python
@pytest.fixture
def init():
    yield

@pytest.mark.usefixtures("init")
def test_login():
    pass
```

## assert vs expect

Pytest:

```python
assert title == "Google"
```

Playwright:

```python
expect(page).to_have_title("Google")
```

| assert               | expect                |
| -------------------- | --------------------- |
| Immediate validation | Auto-wait validation  |
| Python assertion     | Playwright assertion  |
| No waiting           | Retries until timeout |

---

# 17. CI/CD Integration

## Pull Request Pipeline

Run smoke tests:

```bash
pytest -m smoke \
       --html=reports/smoke_report.html \
       --self-contained-html
```

Flow:

```text
Pull Request
      ↓
Smoke Tests
```

## Main Branch Pipeline

Run regression tests:

```bash
pytest -m regression \
       --html=reports/regression_report.html \
       --self-contained-html
```

Flow:

```text
Push to Main
      ↓
Regression Tests
```

Benefits:

* Faster feedback
* Reduced execution time
* Better pipeline efficiency

---

# 18. Interview Questions

## What is a Fixture?

A reusable setup and teardown mechanism.

## What is conftest.py?

A special pytest file used for shared fixtures and hooks.

## What is yield?

Code before yield is setup, code after yield is teardown.

## What is Parametrization?

Running the same test multiple times with different data.

## What is pytest.ini?

A configuration file used to define project-wide pytest settings.

## Difference between skip and xfail?

* skip → Test is not executed.
* xfail → Failure is expected.

## What is pytest-xdist?

A plugin used for parallel execution.

## Difference between assert and expect?

* assert → Immediate validation.
* expect → Auto-wait validation.

## Smoke vs Regression Testing

Smoke:

* Critical functionality
* Fast execution

Regression:

* Full validation
* Complete test suite

## Why use HTML Reports?

* Share execution results
* Better debugging
* Historical tracking
