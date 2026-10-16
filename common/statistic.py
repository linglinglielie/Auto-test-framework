"""
statistic.py
作用：测试执行完成后，用 pandas 统计结果，
再用 matplotlib 画饼图，直观展示通过/失败比例。
"""
import os
import pandas as pd
import matplotlib
# 使用 Agg 无界面后端，只保存图片、不弹窗，适合自动化环境
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def count_test_result(csv_path):
    """
    读取结果 csv，统计成功、失败数量
    :param csv_path: 结果文件路径，里面需要有 result 列
    :return: 每个结果出现次数的 Series
    """
    df = pd.read_csv(csv_path)
    result_count = df["result"].value_counts()
    return result_count


def draw_pie(result_count, save_path):
    """
    根据统计结果绘制饼图并保存
    :param result_count: count_test_result 的统计结果
    :param save_path: 图片保存路径
    """
    # 解决中文和负号乱码
    plt.rcParams["font.sans-serif"] = ["SimHei"]
    plt.rcParams["axes.unicode_minus"] = False

    plt.figure(figsize=(6, 6))
    plt.pie(result_count.values, labels=result_count.index, autopct="%1.1f%%")
    plt.title("接口测试结果分布")
    plt.savefig(save_path)
    plt.close()


if __name__ == "__main__":
    # 直接运行本文件时，读取 reports 下的结果并出图
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    result_file = os.path.join(base_dir, "reports", "result.csv")
    image_file = os.path.join(base_dir, "reports", "test_result.png")
    count = count_test_result(result_file)
    draw_pie(count, image_file)
    print("统计图表已生成：", image_file)
