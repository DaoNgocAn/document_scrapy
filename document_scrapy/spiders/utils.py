from retry import retry
from timeout_decorator import TimeoutError, timeout

@retry
@timeout(10)
def get_with_retry(driver, url):
    driver.get(url)
