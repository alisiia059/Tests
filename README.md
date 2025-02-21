# Selenium Test Automation Suite

## Overview
This project is a Selenium-based test automation suite designed to validate various functionalities of an online bookstore. The test cases cover base page interactions, product purchases, user registration, and checkout processes.

## Features
- Automated UI testing with Selenium and pytest
- Language selection and search functionality
- Product selection and review submission
- User registration with random email and password generation
- Order placement and checkout testing

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- Google Chrome / Firefox (for web automation)
- ChromeDriver / GeckoDriver
- pytest
- Selenium

## Installation
Clone this repository:
```bash
git clone https://github.com/yourusername/selenium-test-suite.git
cd selenium-test-suite
```

Install dependencies:
```bash
pip install -r requirements.txt
```

## Test Cases
### Base Page Test
```bash
pytest -m basepage
```
Opens the website, selects a language, and searches for a term.

### Main Page Test
```bash
pytest -m mainpage
```
Verifies main page buttons and selects the second book.

### Product Page Test
```bash
pytest -m productpage
```
Adds a book to the basket and writes a review.

### User Registration Test
```bash
pytest -m loginpage
```
Creates a new user with a randomly generated email and password.

### Order Placement Test
```bash
pytest -m busketpage
```
Adds a book to the basket and proceeds to checkout.

## Running All Tests
Run all test cases with:
```bash
pytest
```

## Contributing
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`
3. Commit your changes: `git commit -m 'Add new feature'`
4. Push to the branch: `git push origin feature-branch`
5. Open a Pull Request.

## License
This project is licensed under the MIT License.

## Contact
For any inquiries, reach out to 4sssilia@gmail.com or create an issue in the repository.

