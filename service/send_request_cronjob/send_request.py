import urllib.request
import json


# 构造请求头和请求体

def send_request():
    token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyTmFtZSI6IjIwNDA4MDMwMjIxIiwiZXhwIjoxNjc2ODEyMzE0fQ' \
            '.W6dwU5BNlZnkPeZgQ_i0bQqk_ke7gf7fs9dsr_BE9cA'
    uid = 'N0JCMDNGRkUwNEVFNTQ5OEZCMzBBMEY3OTM3MUI2OEU%3D'

    # 登录
    login(uid)

    # 打卡
    check(token)


def login(uid):
    url = 'https://jkjc.xust.edu.cn/healthCheck/weChatLogin?uid=' + uid
    # 创建一个请求对象
    req = urllib.request.Request(url)

    # 发送请求并获取响应
    with urllib.request.urlopen(req) as response:
        response_data = response.read().decode('utf-8')
        print(response_data)


def check(token):
    url = 'https://jkjc.xust.edu.cn/healthCheck/UserHealthCheck/update'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    data = {"isTeaching": 0, "isFever": 0, "isIllness": 0, "infectionCondition": 1, "infectionConditionOthres": "",
            "vaccineCondition": 3, "gh": "20408030221", "clockDate": "2023-02-20"}

    # 将数据编码为 JSON 格式
    data_bytes = json.dumps(data).encode('utf-8')

    # 创建一个请求对象
    req = urllib.request.Request(url, data_bytes, headers)

    # 发送请求并获取响应
    with urllib.request.urlopen(req) as response:
        response_data = response.read().decode('utf-8')
        print(response_data)