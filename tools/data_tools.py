#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   data_tools.py
@Time    :   2022/08/09 15:17:17
@Author  :   Alex Wong 
@Version :   1.0
@Desc    :   PA100K数据集查看
'''




from scipy.io import loadmat
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(f"BASE_DIR: {BASE_DIR}")

def make_dir(dir_name):
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)

def mat2txt(data, key, dirname):
    subdata = data[key]
    df = pd.DataFrame(subdata)
    dirname = os.path.join(BASE_DIR, dirname)
    make_dir(dirname)
    df.to_csv(f'{dirname}/{key}.csv', index=False)
    print(f'{key}.csv, done!')

def main(paths, dirname):
    data = loadmat(paths)
    key_list = [key for key in data.keys() if not (key.startswith('__') and key.endswith("__"))]
    print(f'key_list: {key_list}')
    for key in key_list:
        mat2txt(data=data, key=key, dirname=dirname)

if __name__ == "__main__":
    path = r"E:\第4章\PA100K\annotation\annotation.mat"
    main(path, 'PA100K')
    print("ALL DONE!")
