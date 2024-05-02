import m3u8
from retrying import retry


# 定义一个简单的重试装饰器
@retry(stop_max_attempt_number=3, wait_fixed=2000)  # 最多重试3次，每次间隔2秒
def load_m3u8_with_retry(url, timeout=5):
    return m3u8.load(url, timeout)
