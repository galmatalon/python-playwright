# 🎭 Python Playwright Automation Project

[![Build Status](https://github.com/galmatalon/python-playwright/actions/workflows/python-app.yml/badge.svg)](https://github.com/galmatalon/python-playwright/actions)
[![Coverage](https://img.shields.io/badge/Coverage-90%25-brightgreen)](https://github.com/galmatalon/python-playwright)
[![License](https://img.shields.io/github/license/galmatalon/python-playwright)](https://github.com/galmatalon/python-playwright/blob/main/LICENSE)
[![Stars](https://img.shields.io/github/stars/galmatalon/python-playwright?style=social)](https://github.com/galmatalon/python-playwright)

---

## 📌 Project Description

An advanced end-to-end test automation project using Python and Playwright. Designed to ensure web application stability and reliability with clear structure, modularity, and maintainability.

---

## 🎯 Project Goals

- Demonstrate best practices in UI automation using Playwright.
- Provide a real-world structure for scalable and readable test code.
- Help QA engineers transition into automation roles.

---

## 🛠️ Technologies Used

- Python 3.11+ 🐍
- Playwright 🎭
- Pytest ✅
- GitHub Actions ⚙️
- HTML Reporting 📊

---

## 🚀 Getting Started

### Prerequisites

```bash
pip install -r requirements.txt
```

### Run the tests

```bash
pytest
```

### Run with HTML report

```bash
pytest --html=report.html --self-contained-html
```

---

## 📁 Project Structure

```
python-playwright/
│
├── tests/                  # Test cases
│   ├── test_login.py
│   └── ...
│
├── pages/                  # Page Object classes
│   ├── base_page.py
│   ├── login_page.py
│   └── ...
│
├── utils/                  # Utilities and helpers
│   └── ...
│
├── conftest.py             # Pytest configuration & fixtures
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## ✅ What is Being Tested

- Login and authentication flows 🔐
- Form validations ✅
- Navigation and UI elements 🧭
- Custom JavaScript actions ⚙️

---

## 📊 GitHub Actions Reports

- [Latest Test Report](https://github.com/galmatalon/python-playwright/actions)

> Automatically generated for each push & pull request.

---

## 📸 Screenshots & Examples

_TODO: Add screenshots or videos here_

---

## 🙌 Contribute or Connect

If you like this project:
- ⭐ Star this repository
- 📬 [Send me feedback or connect on LinkedIn](https://www.linkedin.com/in/gal-matalon)

---

> Created with ❤️ by Gal Matalon — [The Automation College](https://www.linkedin.com/company/automation-college)
