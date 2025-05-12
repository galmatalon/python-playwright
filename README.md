
![Project Banner](https://github.com/galmatalon/python-playwright/assets/project-banner.png)

# Python Playwright Automation Framework

![Build Status](https://github.com/galmatalon/python-playwright/actions/workflows/tests.yml/badge.svg)
![Allure Report](https://img.shields.io/badge/Allure-Report-blueviolet)
![Python Version](https://img.shields.io/badge/python-3.11-blue)
![License](https://img.shields.io/github/license/galmatalon/python-playwright)

## 🚀 Overview

This project is a robust, scalable, and beginner-friendly end-to-end testing framework using [Playwright](https://playwright.dev/python/) with Python.
It is designed to automate web application testing with modern tools, clear structure, and continuous integration support.

## 🎯 Project Goals

- Provide a clean and modular automation framework using Python + Playwright
- Enable fast and reliable cross-browser testing
- Demonstrate best practices in test structure, reporting, and CI/CD integration
- Be beginner-friendly for QA engineers transitioning into automation

## 🛠️ Technologies Used

- [Python 3.11](https://www.python.org/)
- [Playwright](https://playwright.dev/python/)
- [Pytest](https://docs.pytest.org/)
- [Allure Reports](https://docs.qameta.io/allure/)
- [GitHub Actions](https://github.com/features/actions)
- [HTML Test Report](https://pypi.org/project/pytest-html/)

## 🧰 Installation & Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/galmatalon/python-playwright.git
   cd python-playwright
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers:**

   ```bash
   playwright install
   ```

5. **Run tests:**

   ```bash
   pytest --alluredir=allure-results
   ```

6. **Generate Allure report:**

   ```bash
   allure serve allure-results
   ```

## 📁 Project Structure

```plaintext
.
├── .github/workflows/    # CI/CD workflows
├── data/                 # Test data files
├── pages/                # Page Object Models
├── tests/                # Test cases
├── utils/                # Utility functions
├── config.ini            # Configuration file
├── pytest.ini            # Pytest configuration
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## ✅ Test Coverage

- Cross-browser testing (Chromium, Firefox, WebKit)
- Functional UI tests
- Form validations
- Navigation flows
- Error handling scenarios

## 📊 Reports

- **Allure Report:** [View Report](https://galmatalon.github.io/python-playwright/allure-report/index.html)
- **GitHub Actions Workflow:** [View Workflow](https://github.com/galmatalon/python-playwright/actions/workflows/tests.yml)

![Allure Report Screenshot](https://github.com/galmatalon/python-playwright/assets/allure-report-screenshot.png)

## 🏷️ Badges

- ![Build Status](https://github.com/galmatalon/python-playwright/actions/workflows/tests.yml/badge.svg)
- ![Allure Report](https://img.shields.io/badge/Allure-Report-blueviolet)
- ![Python Version](https://img.shields.io/badge/python-3.11-blue)
- ![License](https://img.shields.io/github/license/galmatalon/python-playwright)

## 📸 Screenshots

![Test Execution](https://github.com/galmatalon/python-playwright/assets/test-execution.png)
![Allure Dashboard](https://github.com/galmatalon/python-playwright/assets/allure-dashboard.png)

## 🙌 Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or suggestions.

## 📣 Call to Action

If you find this project helpful:

- ⭐ Star this repository
- 🐛 Report issues
- 📢 Share with others

## 🔗 Connect with Me

- [LinkedIn - Gal Matalon](https://www.linkedin.com/in/gal-matalon/)
- [Automation College](https://automation.co.il/)

---

*This project is maintained by Gal Matalon and is part of the Automation College initiative.*
