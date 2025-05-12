# 🔥 Python Playwright Automation Project

Welcome to the **Python Playwright Automation Framework** – a robust, scalable and beginner-friendly end-to-end testing setup using Playwright with Python.

This project is designed to automate web application testing with modern tools, clear structure, and continuous integration support.

---

## 🎯 Project Goals

- Provide a clean and modular automation framework using Python + Playwright
- Enable fast and reliable cross-browser testing
- Demonstrate good practices in test structure, reporting, and CI/CD integration
- Be beginner-friendly for QA engineers looking to transition into automation

---

## 🧰 Technologies Used

- [Python 3.11](https://www.python.org/)
- [Playwright](https://playwright.dev/python/)
- [Pytest](https://docs.pytest.org/)
- [Allure Reports](https://docs.qameta.io/allure/)
- [GitHub Actions](https://github.com/features/actions)
- [HTML Test Report](https://pypi.org/project/pytest-html/)

---

## 🚀 Installation & Running the Tests

1. **Clone the repository**:

```bash
git clone https://github.com/galmatalon/python-playwright.git
cd python-playwright
```

2. **Install dependencies** (preferably in a virtual environment):

```bash
pip install -r requirements.txt
```

3. **Run Playwright install**:

```bash
playwright install
```

4. **Run tests**:

```bash
pytest --html=reports/report.html
```

5. **Run tests with Allure**:

```bash
pytest --alluredir=allure-results
allure serve allure-results
```

---

## 📁 Project Structure

```
python-playwright/
│
├── tests/               # Test cases organized by feature
├── pages/               # Page Object Model classes
├── utils/               # Utility functions and helpers
├── reports/             # HTML reports output folder
├── conftest.py          # Fixtures and test setup
├── requirements.txt     # Python dependencies
└── .github/workflows/   # CI configuration
```

---

## ✅ What’s Tested

- User login & logout flows
- UI validations and error handling
- Browser compatibility
- Form interactions and assertions

---

## 📊 GitHub Actions Reports

👉 [Click here to view test workflow runs](https://github.com/galmatalon/python-playwright/actions)

If you've configured `pytest-html` or `Allure`, reports are automatically generated and can be added to GitHub Pages or sent via email in CI.

---

## 📛 Badges

![Build Status](https://github.com/galmatalon/python-playwright/actions/workflows/python-app.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.11-blue)
![License](https://img.shields.io/github/license/galmatalon/python-playwright)

---

## 🖼️ Screenshots

<img src="https://github.com/galmatalon/python-playwright/blob/main/assets/screenshot-report.png" width="700"/>

> Add your report screenshots or test case illustrations here.

---

## 🙌 Contribute / Feedback

If you find this project useful:

⭐ **Star the repository** to support the work!  
💬 **Send feedback** or suggestions in the issues section.  
📩 Reach out to [Gal Matalon](https://www.linkedin.com/in/galmatalon) for collaborations or questions.

---

## 📘 License

This project is licensed under the MIT License.

---

**Automation College | by Gal Matalon**
