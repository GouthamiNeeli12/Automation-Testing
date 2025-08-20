import datetime
import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from pytest_html import extras

# @pytest.fixture(scope="class")
# def setup():
#     print("I will be executing first")
#     yield
#     print("I will be executing last")
#
# @pytest.fixture(scope="class")
# def dataLoad():
#     print("I will be executing from data load")
#     return ['siri','neeli','kuntala']
#
# @pytest.fixture(params=["chrome","firefox","IE"])
# def crossBrowser(request):
#     return request.param

#To handle command line options without any error, we need to register it using parser addoption

#as we need access the driver variable in get screenshot function, we need to declare it here and make it global inside the function


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Browser to run tests"
    )


@pytest.fixture(scope="function")
def crossbrowser(request):
    browser_name = request.config.getoption("--browser_name")

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        options.add_argument("--start-maximized")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--disable-notifications")
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.default_content_setting_values.notifications": 2
        })
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                  options=options)

    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--start-maximized")   # ✅ only valid args
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),
                                   options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" and report.failed:
        driver = getattr(item.instance, "driver", None) or item.funcargs.get("crossbrowser", None)
        if driver:
            screenshots_dir = "../screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)
            file_path = os.path.join(screenshots_dir, f"{item.name}.png")
            driver.save_screenshot(file_path)
            extra.append(extras.image(file_path))
    report.extra = extra