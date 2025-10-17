import os
import numpy as np  # 被导入的块命名为np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import yaml
import mplcyberpunk
from matplotlib.font_manager import FontProperties


def read_yaml(yaml_file):
    """to read a yaml file"""
    with open(yaml_file, 'rb') as f:
        all_data = list(yaml.safe_load_all(f))
    return all_data


def plot_edge_lane_dump_data_by(yaml_file):
    """从edge、lane traffic输出文件中读取数据"""
    dict_4_yaml = read_yaml(yaml_file=yaml_file)

    basic_info = dict_4_yaml[0]['basic_info']
    plot_contents = dict_4_yaml[0]['plot_contents']

    dt_lines = {}

    for key in plot_contents.keys():
        lines_info = plot_contents[key]
        xls_file = lines_info['name']
        time_tag = lines_info['time_tags']
        ylim = lines_info['ylim']
        xlim = lines_info['xlim']
        names = lines_info['lines']['names']

        df = pd.read_excel(xls_file, header=0)

        for n in names:
            id_label = lines_info['lines']['paras'][n][0]
            id_name = lines_info['lines']['paras'][n][1]
            attr_label = lines_info['lines']['paras'][n][2]
            data_col_specific = df[df[id_label] == id_name]
            data_timetag = data_col_specific[time_tag]
            data_line = pd.DataFrame(data_col_specific[attr_label])
            dt_lines[n] = (data_timetag, data_line)

    fig = plt.figure()

    plt.gca().set_xlim(xlim)
    plt.gca().set_ylim(ylim)
    plt.grid(True, color='silver', linewidth=0.5, linestyle='--', alpha=0.3, axis='both', which='major')
    #plt.style.use("cyberpunk")  # 赛博朋克


    markers = ['.',  '*', 's','x','o', 'v',  'p',  'd']
    marker_size = [7.5,6,5,3,3,3,3,3]
    line_styles = ['-', '--', '--','--', '--','--', '--','--']
    i = 0
    for key, value in dt_lines.items():
        plt.plot(value[0], value[1], label=key, marker=markers[i], markersize=marker_size[i], linestyle=line_styles[i])
        i += 1

    font_dict = dict(fontsize=10,
                     color='w',
                     family='kaiti',
                     weight='light',
                     style='normal',
                     )
    plt.xlabel(basic_info['xlabel'], color='black', fontdict=font_dict)
    plt.ylabel(basic_info['ylabel'], color='black', fontdict=font_dict)

    legend_labels = plt.legend().get_texts()
    [label.set_fontname('kaiti') for label in legend_labels]
    #    '''赛博朋克风格'''
    # mplcyberpunk.add_glow_effects()
    mplcyberpunk.make_lines_glow()
    # mplcyberpunk.add_underglow()
    # mplcyberpunk.make_lines_glow()

    plt.savefig(basic_info['save_pic'], dpi=600, bbox_inches='tight')
    # fig.tight_layout()
    plt.show()
    plt.close()


if __name__ == '__main__':

    os.chdir(os.path.dirname(__file__))

    plot_edge_lane_dump_data_by(yaml_file='yamls/queue_园林路西进口车辆排队长度.yaml')
'''
    plot_edge_lane_dump_data_by(yaml_file='yamls/E2_园林路西进口车辆平均延误.yaml')
    plot_edge_lane_dump_data_by(yaml_file='yamls/E2_园林路西进口车辆平均速度.yaml')
    plot_edge_lane_dump_data_by(yaml_file='yamls/E2_园林路西进口车辆平均占有率.yaml')
    plot_edge_lane_dump_data_by(yaml_file='yamls/E2_园林路东进口车辆平均延误.yaml')
    plot_edge_lane_dump_data_by(yaml_file='yamls/E2_兴民路北进口车辆平均延误.yaml')
    plot_edge_lane_dump_data_by(yaml_file='yamls/E2_兴民路南进口车辆平均延误.yaml')
    plot_edge_lane_dump_data_by(yaml_file='yamls/E3_主干路车辆平均延误.yaml')
    plot_edge_lane_dump_data_by(yaml_file='yamls/E3_主干路车辆平均速度.yaml')
    plot_edge_lane_dump_data_by(yaml_file='yamls/E3_主干路车辆平均旅行时间.yaml')
    plot_edge_lane_dump_data_by(yaml_file='yamls/queue-output_排队长度.yaml')
    plot_edge_lane_dump_data_by(yaml_file='yamls/queue-output_排队时间.yaml')
'''

