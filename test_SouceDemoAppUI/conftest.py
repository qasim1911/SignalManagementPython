#import os

import os

import pytest
from selenium import webdriver
driver = None

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store",default = "chrome", help="run slow")
    parser.addoption("--smoke", action="store", default="Qasim", help="run slow")

@pytest.fixture
def invokeBrowser():
    global driver
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html =item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail =hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join(os.path.dirname(__file__), 'Report')
            file_name = os.path.join(reports_dir,"screenshots", f"{item.name}.png") #os.path.join(reports_dir, report.nodeid.replace("::", "_") + ".png")
            print("test1 $%^&*()&*()****************")
            print(file_name)
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304;height:228px;"'\
                'onclick="window.open(this.src)" allign="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))

        report.extra = extra




def _capture_screenshot(file_name):
    driver.get_screenshot_as_file(file_name)
