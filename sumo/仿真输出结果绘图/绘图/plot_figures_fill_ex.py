# coding=utf-8
import xml.dom.minidom as minidom
import os
import yaml
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from numpy import loadtxt
from pandas.core.frame import DataFrame
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing, SimpleExpSmoothing, Holt
import ast


def plot_loss_data_agg_by(yamlfile):
    # 读取yaml

    with open(yamlfile, 'r', encoding='utf-8') as f:
        data_all = yaml.load(f.read(), Loader=yaml.FullLoader)

    basic_info = data_all['basic_info']
    data_info = data_all['data_from_files']
    x_label = basic_info['xlabel']
    y_label = basic_info['ylabel']
    x_ticks = basic_info['xticks']
    x_show_ticks = basic_info['xticklabels']
    x_lim = basic_info['xlim']
    y_lim = basic_info['ylim']
    palette = basic_info['palette']
    markers = basic_info['markers']
    marker_size = basic_info['marker_size']
    line_styles = basic_info['line_styles']
    save_path_png = basic_info['save_path_png']
    save_path_pdf = basic_info['save_path_pdf']
    legend_name = []
    # 绘图 初始化

    fig = plt.figure()
    sns.set_style(style='darkgrid')
    sns.set(font='kaiti')
    # sns.set_theme(style="ticks")
    plt.rcParams['font.sans-serif'] = ['Simhei']

    # 初始化df
    df = DataFrame()
    # 读取数据并绘图
    for d in data_info.values():
        # 数据的基本信息
        data_name = d['name']
        file_path = d['path']
        data_type = d['type']
        tls_id = d['id']
        legend_name.append(data_name)
        # 读取数据
        loss_df = pd.read_csv(file_path)
        # dataframe合并前两列相同的数据，第三列求平均
        # 从dataframe中筛选第二列为J0
        # loss_df=loss_df[loss_df['id']==tls_id].groupby(['episode']).agg(['mean'])
        loss_df = loss_df[loss_df['id'] == tls_id].drop('id', axis=1).groupby(['episode']).agg(['mean'])
        
        #
        loss_list = loss_df['loss']['mean'].tolist()
        ep = loss_df.index.tolist()


        # 平滑数据
        smoothed = []
        last1 = 0
        last2 = loss_list[0]
        smoothed_weight = 0.48
        for p in loss_list:
            smoothed_val = 0.5 * (last1 + last2) * smoothed_weight + (1 - smoothed_weight) * p
            smoothed.append(smoothed_val)
            last1 = last2
            last2 = smoothed_val
        # 构造DataFrame
        # df1 = pd.concat([DataFrame(loss_mean), DataFrame(smoothed)])
        df1 = DataFrame(smoothed)
        # 二次指数平滑
        results = Holt(endog=df1, initialization_method='estimated').fit()
        df_smoothed = results.fittedvalues
        # df_smoothed = df_smoothed[~df_smoothed.index.duplicated()]
        df[data_name] = df_smoothed
        df['episode'] = DataFrame(ep)
    min_value_y = df.min().min()
    max_value_y = df.max().max()
    sns.set_palette(palette)
    ## 绘曲线
    for i, column in enumerate(df.drop('episode', axis=1).columns):
        error = df[column] * 0.22
        line_color = palette[i % len(palette)]  # 将变量名改为 line_color 避免冲突
        plt.plot(df['episode'], df[column], color=line_color, linestyle=line_styles[i], marker=markers[i],
                 markersize=marker_size[i], label=legend_name[i])
        plt.fill_between(df['episode'], df[column] - error, df[column] + error,
                         alpha=0.11, edgecolor=line_color, facecolor=line_color,
                         linewidth=.1, linestyle='', antialiased=True)

    plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    # sns.set_theme(style="ticks")  # 设置刻度
    plt.rcParams['font.sans-serif'] = ['Simhei']
    plt.gca().set_xlim(x_lim)
    plt.gca().set_ylim(y_lim)
    plt.legend(loc='upper right', labelcolor='dimgrey')
    plt.xticks(x_ticks, x_show_ticks)
    fig = plt.gcf()
    fig.savefig(save_path_png)
    fig.savefig(save_path_pdf)

def plot_loss_data_zgr_by(yamlfile):
    # 读取yaml

    with open(yamlfile, 'r', encoding='utf-8') as f:
        data_all = yaml.load(f.read(), Loader=yaml.FullLoader)

    basic_info = data_all['basic_info']
    data_info = data_all['data_from_files']
    x_label = basic_info['xlabel']
    y_label = basic_info['ylabel']
    x_ticks = basic_info['xticks']
    x_show_ticks = basic_info['xticklabels']
    x_lim = basic_info['xlim']
    y_lim = basic_info['ylim']
    palette = basic_info['palette']
    markers = basic_info['markers']
    marker_size = basic_info['marker_size']
    line_styles = basic_info['line_styles']
    save_path_png = basic_info['save_path_png']
    save_path_pdf = basic_info['save_path_pdf']
    legend_name = []
    # 绘图 初始化

    fig = plt.figure()
    sns.set_style(style='darkgrid')
    sns.set(font='kaiti')
    # sns.set_theme(style="ticks")
    plt.rcParams['font.sans-serif'] = ['Simhei']

    # 初始化df
    df = DataFrame()
    # 读取数据并绘图
    smoothed_data = {}
    for d in data_info.values():
        # 数据的基本信息
        data_name = d['name']
        file_path = d['path']
        data_type = d['type']
        tls_id = d['id']
        legend_name.append(data_name)
        # 读取数据
        loss_df = pd.read_csv(file_path)
        # 求平均值
        loss_df=loss_df.groupby(['episode', 'id']).mean().reset_index()
        # 获取唯一的id值
        unique_ids = loss_df['id'].unique()

        id_data = loss_df[loss_df['id'] == tls_id]
        loss_list = id_data['loss'].tolist()
        ep = ep = id_data['episode'].tolist()
        id = id_data['id'].tolist()

        # 平滑数据
        smoothed = []
        last1 = 0
        last2 = loss_list[0]
        smoothed_weight = 0.48
        for p in loss_list:
            smoothed_val = 0.5 * (last1 + last2) * smoothed_weight + (1 - smoothed_weight) * p
            smoothed.append(smoothed_val)
            last1 = last2
            last2 = smoothed_val
        # 构造DataFrame
        # df1 = pd.concat([DataFrame(loss_mean), DataFrame(smoothed)])
        df1 = DataFrame(smoothed)
        # 二次指数平滑
        results = Holt(endog=df1, initialization_method='estimated').fit()
        df_smoothed = results.fittedvalues
        # 将平滑后的数据存储到结果中
        df[data_name] = df_smoothed
        df['episode'] = DataFrame(ep)
        smoothed_data[tls_id] = smoothed
    sns.set_palette(palette)
    ## 绘曲线

    sns.set_palette(palette)
    for unique_id, smoothed_values in smoothed_data.items():
        i=0
        line_color = palette[unique_ids.tolist().index(unique_id) % len(palette)]
        error = np.array(smoothed_values) * 0.22

        plt.plot(loss_df[loss_df['id'] == unique_id]['episode'], smoothed_values,
                 color=line_color, linestyle=line_styles[i], marker=markers[i],
                 markersize=marker_size[i], label=unique_id)

        plt.fill_between(loss_df[loss_df['id'] == unique_id]['episode'],
                         np.array(smoothed_values) - error,
                         np.array(smoothed_values) + error,
                         alpha=0.11, edgecolor=line_color, facecolor=line_color,
                         linewidth=.1, linestyle='', antialiased=True)
        i+=1

    plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    # sns.set_theme(style="ticks")  # 设置刻度
    plt.rcParams['font.sans-serif'] = ['Simhei']
    plt.gca().set_xlim(x_lim)
    plt.gca().set_ylim(y_lim)
    plt.legend(loc='upper right', labelcolor='dimgrey')

    plt.xticks(x_ticks, x_show_ticks)

    fig = plt.gcf()
    fig.savefig(save_path_png)
    fig.savefig(save_path_pdf)

def plot_rewards_data_by(yamlfile):
    # 读取yaml

    with open(yamlfile, 'r', encoding='utf-8') as f:
        data_all = yaml.load(f.read(), Loader=yaml.FullLoader)

    basic_info = data_all['basic_info']
    data_info = data_all['data_from_files']
    x_label = basic_info['xlabel']
    y_label = basic_info['ylabel']
    x_ticks = basic_info['xticks']
    x_show_ticks = basic_info['xticklabels']
    x_lim = basic_info['xlim']
    y_lim = basic_info['ylim']
    palette = basic_info['palette']
    markers = basic_info['markers']
    marker_size = basic_info['marker_size']
    line_styles = basic_info['line_styles']
    save_path_png = basic_info['save_path_png']
    save_path_pdf = basic_info['save_path_pdf']
    legend_name = []
    # 绘图 初始化

    fig = plt.figure()
    sns.set_style(style='darkgrid')
    sns.set(font='kaiti')
    # sns.set_theme(style="ticks")
    plt.rcParams['font.sans-serif'] = ['Simhei']

    # 初始化df
    df = DataFrame()
    # 读取数据并绘图
    for d in data_info.values():
        # 数据的基本信息
        data_name = d['name']
        file_path = d['path']
        data_type = d['type']
        tls_id = d['id']
        legend_name.append(data_name)
        # 读取数据
        rewards_df = pd.read_csv(file_path)
        # rewards_df = rewards_df[rewards_df['id'] == tls_id].groupby(['episode']).agg(['mean'])
        rewards_df = rewards_df[rewards_df['id'] == tls_id].drop('id', axis=1).groupby(['episode']).agg(['mean'])
        # rewards_df = rewards_df[rewards_df['id'] == tls_id].drop('id', axis=1).groupby(['episode']).agg(
        #     ['mean']).reset_index()

        #
        rewards_list = rewards_df['rewards']['mean'].tolist()
        ep = rewards_df.index.tolist()


        # 平滑数据
        smoothed = []
        last1 = 0
        last2 = rewards_list[0]
        smoothed_weight = 0.8
        for p in rewards_list:
            smoothed_val = 0.5*(last1+last2)*smoothed_weight + (1-smoothed_weight)*p
            smoothed.append(smoothed_val)
            last1 = last2
            last2 = smoothed_val
        # 构造DataFrame
        # df1 = pd.concat([DataFrame(rewards_mean), DataFrame(smoothed)])
        df1 = DataFrame(smoothed)
        # 二次指数平滑
        results = Holt(endog=df1, initialization_method='estimated').fit()
        df_smoothed = results.fittedvalues
        df[data_name] = df_smoothed
        df['episode'] = DataFrame(ep)
    min_value_y = df.min().min()
    max_value_y = df.max().max()
    sns.set_palette(palette)
    # 绘制曲线
    for i, column in enumerate(df.drop('episode', axis=1).columns):
        error = df[column] * 0.2
        line_color = palette[i % len(palette)]  # 将变量名改为 line_color 避免冲突
        plt.plot(df['episode'], df[column], color=line_color, linestyle=line_styles[i], marker=markers[i], markersize=marker_size[i], label=legend_name[i])
        plt.fill_between(df['episode'], df[column] - error, df[column] + error,
                             alpha=0.10, edgecolor=line_color, facecolor=line_color,
                             linewidth=.1, linestyle='', antialiased=True)

    plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    # sns.set_theme(style="ticks")  # 设置刻度
    plt.rcParams['font.sans-serif'] = ['Simhei']
    plt.gca().set_xlim(x_lim)
    plt.gca().set_ylim(y_lim)
    plt.legend(loc='upper left', labelcolor='dimgrey')
    plt.xticks(x_ticks, x_show_ticks)
    fig = plt.gcf()
    fig.savefig(save_path_png)
    fig.savefig(save_path_pdf)

def plot_sumo_output_data_by(yamlfile):
    # 读取yaml
    with open(yamlfile, 'r', encoding='utf-8') as f:
        data_all = yaml.load(f.read(), Loader=yaml.FullLoader)
    basic_info = data_all['basic_info']
    data_info = data_all['data_from_files']

    # 参数读取
    x_label = basic_info['xlabel']
    y_label = basic_info['ylabel']
    x_lim = basic_info['xlim']
    y_lim = basic_info['ylim']
    x_ticks = basic_info['xticks']
    x_show_ticks = basic_info['xticklabels']
    palette = basic_info['palette']
    markers = basic_info['markers']
    marker_size = basic_info['marker_size']
    line_styles = basic_info['line_styles']
    save_path_png = basic_info['save_path_png']
    save_path_pdf = basic_info['save_path_pdf']
    legend_name = []

    # 绘图 初始化
    fig = plt.figure()
    sns.set_style(style='darkgrid')
    plt.rcParams['font.sans-serif'] = ['Simhei']

    # 初始化df
    df = DataFrame()

    # 读取数据并绘图
    for d in data_info.values():
        # 数据的基本信息
        data_name = d['name']
        legend_name.append(data_name)
        file_path = d['path']
        data_type = d['type']
        tag_name = d['tag_name']
        locating_col = d['locating_cols']
        time_col = d['time_col']
        attr_col = d['attr_col']
        # 读取数据
        data_time = []
        data_attr = []
        # 打开xml文档
        dom = minidom.parse(file_path)
        # 得到文档元素对象
        root = dom.documentElement
        # 所有数据
        data = dom.getElementsByTagName(tag_name)

        # 定位数据
        for dt in data:
            if_is = True
            for key, val in locating_col.items():
                # pass
                if dt.getAttribute(key) != val:
                    if_is = False
                    break
            if if_is:
                data_time.append(dt.getAttribute(time_col))
                data_attr.append(dt.getAttribute(attr_col))
        # 转换格式
        data_time = [int(float(i)) for i in data_time]
        data_attr = [float(i) for i in data_attr]
        # 平滑数据
        smoothed = []
        last1 = 0
        last2 = data_attr[0]
        smoothed_weight = 0.48
        for p in data_attr:
            smoothed_val = 0.5 * (last1 + last2) * smoothed_weight + (1 - smoothed_weight) * p
            smoothed.append(smoothed_val)
            last1 = last2
            last2 = smoothed_val
        # 中心线
        coefficients = np.polyfit(data_time, data_attr, 2)  # 二次多项式拟合
        data_attr_fit = np.polyval(coefficients, data_time)
        # 构造DataFrame
        df1 = DataFrame(smoothed)
        # 二次指数平滑
        results = Holt(endog=df1, initialization_method='estimated').fit()
        df_smoothed = results.fittedvalues
        df[data_name] = df_smoothed
        df['Simulation Time'] = DataFrame(data_time)
    # error = np.random.rand(len(df[0, :])) * 0.5
    sns.set_palette(palette)

    for i, column in enumerate(df.drop('Simulation Time', axis=1).columns):
        error = df[column] * 0.175
        line_color = palette[i % len(palette)]  # 将变量名改为 line_color 避免冲突
        plt.plot(df['Simulation Time'], df[column], color=line_color, linestyle=line_styles[i], marker=markers[i], markersize=marker_size[i], label=legend_name[i])
        plt.fill_between(df['Simulation Time'], df[column] - error, df[column] + error,
                             alpha=0.1, edgecolor=line_color, facecolor=line_color,
                             linewidth=.1, linestyle='', antialiased=True)

    # 绘曲线
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    sns.set_theme(style="ticks")  # 设置刻度
    plt.rcParams['font.sans-serif'] = ['Simhei']
    plt.gca().set_xlim(x_lim)
    plt.gca().set_ylim(y_lim)
    plt.legend(loc='upper left', labelcolor='dimgrey')

    plt.xticks(x_ticks, x_show_ticks)
    fig = plt.gcf()
    fig.savefig(save_path_png)
    fig.savefig(save_path_pdf)

