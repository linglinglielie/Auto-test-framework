"""
test_api.py
作用：读取 data/case_data.csv 中的接口用例，
用 pytest 参数化批量执行，并断言状态码。
"""
import os
import sys
import pandas as pd
import pytest

# 把项目根目录加入搜索路径，保证能 import common
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from common.request_util import req_client


def get_case_data():
    """读取 csv 用例，转成字典列表，供参数化使用"""
    case_file = os.path.join(BASE_DIR, "data", "case_data.csv")
    df = pd.read_csv(case_file)
    case_list = df.to_dict("records")
    return case_list


@pytest.mark.parametrize("case", get_case_data())
def test_api_demo(case):
    """参数化执行接口测试用例"""
    method = case["method"]
    url = case["url"]
    expect_code = int(case["expect_code"])

    response = req_client.send_request(method=method, url=url)

    # 断言：实际状态码应等于预期状态码
    assert response.status_code == expect_code
