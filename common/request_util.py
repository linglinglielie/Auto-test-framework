"""
request_util.py
作用：对 requests 发送 HTTP 请求做统一封装。
后续所有测试用例都通过 req_client 发送请求，
方便统一加请求头、超时、异常处理等。
"""
import requests


class RequestUtil:
    def __init__(self):
        # 使用 Session 可以自动保持 cookie，模拟同一个客户端
        self.session = requests.Session()

    def send_request(self, method, url, params=None, data=None,
                     json=None, headers=None, timeout=10):
        """
        统一发送 HTTP 请求
        :param method: 请求方法，如 GET / POST
        :param url: 请求地址
        :param params: url 查询参数
        :param data: 表单数据
        :param json: json 请求体
        :param headers: 请求头
        :param timeout: 超时时间（秒）
        :return: 响应对象 response
        """
        response = self.session.request(
            method=method,
            url=url,
            params=params,
            data=data,
            json=json,
            headers=headers,
            timeout=timeout
        )
        return response


# 全局请求实例，所有用例共用同一个 session
req_client = RequestUtil()
