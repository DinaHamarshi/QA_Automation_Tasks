# QA Automation Tasks

This repository contains basic QA automation tests developed using Python, Selenium WebDriver, and Pytest.  
The tests target the demo e-commerce website [Magento](https://magento.softwaretestingboard.com/).

## Tools and Technologies
- Python
- Selenium
- Pytest
- Pytest-html

## Project Structure
- `baseclass.py` — Contains common methods such as navigation, element handling, account creation, and sign-in.
- `conftest.py` — WebDriver setup and teardown using pytest fixtures.
- `pytest.ini` — Configuration file for pytest.
- `test_create_account.py` — Tests for user account creation (positive and negative scenarios).
- `test_sign_in.py` — Tests for user sign-in with different credential cases.
- `QAProjectReport.html` — HTML report generated from test execution.
