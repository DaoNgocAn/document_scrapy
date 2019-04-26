from retry import retry
from timeout_decorator import TimeoutError, timeout

@retry(TimeoutError, tries=30)
@timeout(30)
def get_with_retry(driver, url):
    driver.get(url)
