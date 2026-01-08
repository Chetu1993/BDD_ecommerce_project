# 🌐 Selenium Automation Framework (Python | BDD | POM | Allure)

This project is a **Python-based Selenium automation testing framework** designed using **BDD (Behavior Driven Development)** principles.  
It follows the **Page Object Model (POM)** architecture, supports **cross-browser testing**, includes **logging**, and generates **Allure reports** for test execution analysis.

---

## 📁 Project Structure

📁 Project Structure

selenium_automation_framework/

features/ — BDD feature files written in Gherkin syntax

login.feature

steps/ — Step definition files

login_steps.py

pages/ — Page Object Model (POM) classes

login_page.py

utils/ — Utility and helper modules

logger.py

logs/ — Execution logs

automation.log

allure-results/ — Raw Allure test result files

allure-report/ — Generated Allure HTML report


---

## 🛠️ Technologies Used

- Python 3.x
- Selenium WebDriver
- Behave (BDD Framework)
- Page Object Model (POM)
- Allure Reporting
- Logging Module
- Pytest / Behave Runner
- Cross-Browser Testing (Chrome, Firefox, Edge)

---

## ⚙️ Framework Features

- ✅ BDD implementation using **Gherkin syntax**
- ✅ **Page Object Model (POM)** for maintainability
- ✅ Cross-browser execution support
- ✅ Centralized browser management
- ✅ Detailed logging for debugging
- ✅ Allure HTML test reports
- ✅ Reusable and scalable framework structure

---

## 📦 Installation & Setup

### 1️⃣ Create Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate

🧱 Page Object Model (POM)

Each web page has a separate class

Locators and actions are encapsulated

Improves reusability and maintainability

Reduces code duplication

🌍 Cross Browser Testing

Supported browsers:

Chrome

Firefox

Microsoft Edge

Browser selection is configurable via:

Config file

Command line argument

Example:

behave -D browser=chrome

📝 Logging

Implemented using Python logging module

Logs include:

Test start/end

Browser actions

Errors and exceptions

Log files stored in logs/automation.log

📊 Allure Report Generation

Step 1: Run Tests with Allure

behave -f allure_behave.formatter:AllureFormatter -o allure-results

Step 2: Generate HTML Report

allure serve allure-results

Allure Report Includes:

Feature-wise execution

Scenario status

Execution time

Logs and failure details

📌 Best Practices Followed

BDD for better collaboration

POM for clean architecture

Explicit waits for stability

Centralized configuration

Proper exception handling

Scalable folder structure

🚀 Future Enhancements

Parallel execution

Docker integration

CI/CD pipeline integration

Screenshot capture on failure

Data-driven testing

👤 Author

Chetan Kumar
Python | Selenium | BDD | POM | Allure | Automation Testing
