from util.m3u8_util import load_m3u8_with_retry

BASE_URL = 'https://m3u.haiwaikan.com/xm3u8'


def modify_ts_url(file_name):
    m3u8_obj = load_m3u8_with_retry(f'{BASE_URL}/{file_name}')

    # 修改每个segment的URI,将广告标识全去掉
    for segment in m3u8_obj.segments:
        segment.uri = segment.uri.replace('cdnb.v82u1l.com', 'hv.118318.xyz')
        segment.uri = segment.uri.replace('cdn.v82u1l.com', 'h.118318.xyz')
        segment.uri = segment.uri.replace('cdn.kin6c1.com', 'v3.118318.xyz')
        segment.uri = segment.uri.replace('cdn.iz8qkg.com', 'v4.118318.xyz')
        segment.uri = segment.uri.replace('cdnb.kin6c1.com', 'v5.118318.xyz')
        segment.uri = segment.uri.replace('cdnb.iz8qkg.com', 'v6.118318.xyz')
        segment.discontinuity = False

    return m3u8_obj.dumps()

