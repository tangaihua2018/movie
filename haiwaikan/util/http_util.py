import requests
import time


def request_with_retry(url, max_retries=3, delay=1):
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url, timeout=5)  # 设置超时时间
            if response.status_code == 200:  # 检查是否收到了有效的响应
                return response.text
            else:
                print(f"Received unexpected status code: {response.status_code}")
        except (requests.RequestException, IOError) as e:
            print(f"Request failed: {e}")
        retries += 1
        if retries < max_retries:
            print(f"Retrying in {delay} seconds...")
            time.sleep(delay)
    raise Exception("Max retries exceeded")
