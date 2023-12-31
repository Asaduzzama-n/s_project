# Fund-Future Crowdfunding Site Automated Testing with Selenium and Python

This repository contains automated tests for the Fund-Future crowdfunding site using Selenium and Python. The tests cover various functionalities of the site, including donation, registration, login, report generation, campaign creation, and success story creation.

## Prerequisites

Before you can run the automated tests, you need to have the following tools and dependencies set up:

- Python (>=3.6)
- Selenium library for Python
- Webdriver for your preferred browser (Chrome or Firefox)
- fund-future 
- fund-future frontend [https://github.com/Asaduzzama-n/fund-future]()
- fund-future backend [https://github.com/Asaduzzama-n/funde-future-server]()
- Follow the instruction to run the project in your local machine.

## IMPORTANT NOTE
- Some functionality may not work as some changes were made in the code during the test that are not updated in the given repository of the fund-future.
- Those changes were made just to identify component easily.

## Installation

You can install the necessary dependencies using the following steps:

1. Clone this repository to your local machine.
   
   ```
   git clone https://github.com/Asaduzzama-n/s_project.git
   ```

2. Navigate to the project directory.
   
   ```
   cd s_project
   ```

3. Create a virtual environment (optional but recommended).
   
   ```
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

4. Install the required Python packages.
   
   ```
   pip install  selenium
   ```

## Webdriver Setup

To run the tests using Selenium, you need to download the appropriate webdriver for your preferred browser (Chrome or Firefox). Follow the steps below to set up the webdriver:

### Chrome

1. Download the Chrome webdriver: https://sites.google.com/chromium.org/driver/
2. Place the downloaded executable in a directory accessible by your system's PATH.
3. Update the `config.py` file in the project directory with the correct webdriver path.

### Firefox

1. Download the Gecko webdriver: https://github.com/mozilla/geckodriver/releases
2. Place the downloaded executable in a directory accessible by your system's PATH.
3. Update the `config.py` file in the project directory with the correct webdriver path.

## Running the Tests

After setting up the dependencies and webdrivers, you can run the automated tests using the following command:

```
python run_tests.py
```

This will execute the test suite, and you'll see the test progress and results in the console.

## Test Cases

The automated tests cover the following scenarios:

- Donation process
- User registration
- User login
- Report generation
- Campaign creation
- Success story creation
- User authorization

You can find the test cases in the `s_project` directory. Each test case is a separate Python file containing the test logic.

## Reporting

The test results will be displayed in the console during and after the test execution. Additionally, you can explore the generated HTML reports located in the `reports` directory. These reports provide detailed information about the test runs, including passed and failed tests.

## Note

Make sure to replace base url with `localhost of fund future`, feel free to customize and extend the test cases according to your project's requirements.

For any questions or issues, please contact [asaduzzaman193146@gmail.com](mailto:your-email@example.com).