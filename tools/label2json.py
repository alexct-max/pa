#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   label2json.py
@Time    :   2022/08/15 10:03:57
@Author  :   Alex Wong 
@Version :   1.0
@Desc    :   转为labelme可用的json文件
'''

import sys
import json
import csv

def get_label_name(paths):
    temp_label_name = []
    with open (paths) as f:
        data = csv.reader(f)
        # 删除表头，根据csv具体内容决定是否添加
        headers = next(data)
        for row in data:
            row = row[0].strip("[']").strip()
            temp_label_name.append(row)
    return temp_label_name

def labe2json(data_paths, label_path, output_dir,nums):
    """
    data_paths 数据存放目录;
    label_path 标签存放目录;
    output_dir 输出目录；
    nums 需要制作标签数量
    """
    temp_label_dic = {
        "version": "5.0.1",
        "flags": {
        },
        "shapes": [],
        "imagePath": "",
        "imageData": None
    }
    label_name_list = get_label_name(label_path)
    with open (data_paths) as f:
        data = csv.reader(f)
        headers = next(data)
        for i, row in enumerate(data):
            for labels, content in zip(label_name_list, row):
                # print(labels, content)
                if content == '0':
                    temp_label_dic["flags"][labels] = False
                else:
                    temp_label_dic["flags"][labels] = True

            temp_label_dic["imagePath"] = "{:0>6d}.jpg".format(i+1)

            with open(output_dir + r"\{:0>6d}.json".format(i+1), "w") as f:
                json.dump(temp_label_dic, f)
            if nums == i+1:
                print("all done")
                sys.exit(1)
            elif i%100 == 0 and i != 0:
                print(f"完成{i}次！")


if __name__ == "__main__":

    labe2json(r'tools\PA100K\train_label.csv', 
            r'tools\PA100K\attributes.csv', 
            r'D:\360MoveData\Users\bug\Desktop\out_put',
            100000)