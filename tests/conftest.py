import os
import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from pytest_html import extras


# ------------------------------
# Command line option for browser
# ------------------------------
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Browser to run tests"
    )


# ------------------------------
# Cross-browser fixture
# ------------------------------
@pytest.fixture(scope="function")
def crossbrowser(request):
    browser_name = request.config.getoption("--browser_name")

    if browser_name.lower() == "chrome":
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

    elif browser_name.lower() == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),
                                   options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    # Attach driver to class if used in class tests
    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()


# ------------------------------
# Hook to capture screenshots on failure
# ------------------------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture screenshot and attach to HTML report on test failure"""
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" and report.failed:
        # Try to get driver from class or function argument
        driver = getattr(item.instance, "driver", None) or item.funcargs.get("crossbrowser", None)
        if driver:
            try:
                # Save screenshot to file
                screenshots_dir = "screenshots"
                os.makedirs(screenshots_dir, exist_ok=True)
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                file_path = os.path.join(screenshots_dir, f"{item.name}_{timestamp}.png")
                driver.save_screenshot(file_path)

                # Attach screenshot to HTML report
                extra.append(extras.image(file_path))
                print(f"[HOOK] Screenshot saved: {file_path}")
            except Exception as e:
                print(f"[HOOK ERROR] Could not capture screenshot: {e}")

    report.extra = extra

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, "extra", [])
#
#     if report.when == "call" and report.failed:
#         driver = getattr(item.instance, "driver", None) or item.funcargs.get("crossbrowser", None)
#         if driver:
#             try:
#                 screenshot_base64 = driver.get_screenshot_as_base64()
#                 extra.append(extras.image(
#                     screenshot_base64,
#                     mime_type="image/png",
#                     source_type="base64"   # ← important for pytest-html 4.x
#                 ))
#             except Exception as e:
#                 print(f"[HOOK ERROR] Could not capture screenshot: {e}")
#
#     report.extra = extra
