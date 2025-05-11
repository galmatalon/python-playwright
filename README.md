
# Python Playwright Automation

![Python Playwright](https://automation.co.il/wp-content/uploads/2025/04/%D7%94%D7%9E%D7%9B%D7%9C%D7%9C%D7%94-%D7%9C%D7%90%D7%95%D7%98%D7%95%D7%9E%D7%A6%D7%99%D7%94-%D7%9C%D7%95%D7%92%D7%95.jpeg)  <!-- Link to the top image -->

## 🚀 Description
A Python automation project using Playwright for running automated tests on websites. The project includes scripts for automating browser actions with Playwright and generating Allure reports for test result analysis.

## 🛠️ Installation

### System Requirements:
- Python 3.7 or higher
- Playwright
- pytest
- Allure (for generating reports)

### Installing Dependencies:
Install the required dependencies using pip:
```bash
pip install -r requirements.txt
```

To install Playwright:
```bash
python -m playwright install
```

### Running the Code:
To run the tests with pytest:
```bash
pytest --alluredir=allure-results
```

After running, you can view the Allure report:
```bash
allure serve allure-results
```

## 🏃 Usage

To run the tests, simply execute the code as described in the installation section.

For example, to run all tests on the Chrome browser:
```bash
pytest --browser=chrome
```

## 📊 Allure Reports

To generate Allure reports, use the following command after running the tests:
```bash
pytest --alluredir=allure-results
```

Then, to view the report:
```bash
allure serve allure-results
```

## 📂 File Structure

The project contains the following files and directories:

```
python-playwright/
├── tests/                    # Test files
│   ├── test_example.py        # Example test
│   └── ...
├── requirements.txt           # List of dependencies
├── playwright_config.py       # Playwright configuration
├── allure-results/            # Allure test results
└── README.md                 # This file
```

## 🤝 Contribution

If you would like to contribute to the project, all contributions are welcome! You can add new features, fix bugs, or improve the documentation.

### Steps for Contribution:
1. Open a pull request with your fixes or feature.
2. Ensure your code passes the tests by running them.
3. We will review your contribution and get back to you.

## 📦 Dependencies

The project depends on the following libraries:
- `pytest` - for running automated tests.
- `playwright` - for browser automation.
- `allure-pytest` - for generating Allure reports.

## 🔗 Links
- [Playwright Documentation](https://playwright.dev/)
- [Allure Documentation](https://allure.qatools.ru/)
