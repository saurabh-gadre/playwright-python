> Playwright Test Project with Python

- Chromium headed test run
  * pytest -v --headed --browser=chromium

- Stop on first failure
   * pytest -x

- Run specific marked test
   * pytest -m smoke

- Rerun last failed tests only
   * pytest --lf

- Rerun all tests, starting with last failed
   * pytest --ff

- Run with all CLI options together
   * pytest --ff -x -v

- Running Pytest with Reports
   * pytest --template=html1/index.html --report=report.html