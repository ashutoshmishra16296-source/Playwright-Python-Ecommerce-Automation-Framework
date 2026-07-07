import os
from datetime import datetime
import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        page = item.funcargs.get("page")

        if page:

            os.makedirs("screenshots", exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            screenshot = f"screenshots/{item.name}_{timestamp}.png"

            page.screenshot(path=screenshot)

            print(f"\nScreenshot saved at {screenshot}")