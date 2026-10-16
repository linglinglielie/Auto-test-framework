# 接口自动化测试框架（auto-test-framework）

基于 **Python + pytest + requests** 实现的接口自动化测试框架。
使用 **pandas** 管理测试用例与结果数据，使用 **matplotlib** 生成测试结果统计图表。

## 一、技术栈

- Python 3
- pytest：测试用例组织、参数化、断言
- requests：发送 HTTP 请求
- pandas：读取 CSV 用例、统计测试结果
- matplotlib：绘制测试结果饼图
- allure-pytest：生成可视化测试报告（可选）

## 二、目录结构

```
Auto-test-framework/
├── common/                # 公共工具模块
│   ├── __init__.py
│   ├── request_util.py    # requests 请求统一封装
│   └── statistic.py       # pandas 统计 + matplotlib 画图
├── testcases/             # 测试用例
│   ├── __init__.py
│   └── test_api.py        # 参数化接口测试用例
├── data/                  # 测试用例数据
│   └── case_data.csv
├── reports/               # 测试结果、图表输出
├── pytest.ini             # pytest 配置
└── requirements.txt       # 依赖清单
```

## 三、环境准备

```bash
# 安装依赖
pip install -r requirements.txt
```

## 四、运行测试

```bash
# 在项目根目录执行，自动运行 testcases 下所有用例
pytest
```

## 五、新增用例

在 `data/case_data.csv` 中按下面格式追加一行即可：

```csv
method,url,expect_code
GET,https://httpbin.org/get,200
```

- method：请求方法（GET/POST 等）
- url：接口地址
- expect_code：预期 HTTP 状态码

## 六、生成结果统计图

```bash
python common/statistic.py
```

运行后在 `reports/` 目录生成 `test_result.png`。

## 七、后续优化方向

- [ ] 用 conftest.py 统一管理 fixture（登录 token、公共请求头）
- [ ] 用 allure 生成 HTML 测试报告
- [ ] 支持 POST 请求体、接口依赖、数据库断言
- [ ] 接入 Jenkins 实现持续集成
