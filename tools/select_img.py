#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   select_img.py
@Time    :   2022/08/17 15:57:32
@Author  :   Alex Wong 
@Version :   1.0
@Desc    :   None
'''


import random, os, shutil, cv2, re


def make_my_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def check_img(img_path, height=128, width=64, file_size=5120):
    """
    过滤尺寸不合格的图片，与大小不合格的图片
    img_path: 图片地址
    height: 图片最小高度
    width: 图片最小宽度
    file_size: 图片占用的存储空间
    """
    img = cv2.imread(img_path, flags=cv2.IMREAD_COLOR)
    # img info
    img_size = os.path.getsize(img_path)
    img_height, img_width = img.shape[:2]
    # 判断是不是图片
    file_suffix = "jpeg|jpg|png"
    if re.search(file_suffix, img_path) is None:
        return False
    
    if img_height > height and img_width > width and img_size > file_size:
        return True
    
    return False

def copy_img(input_file, output_file, num=10000, rate=0):
    """
    input_file: 输入文件夹
    output_file: 输出文件夹
    num: 抽取图片数量
    rate: 按照rate比例从文件夹中取一定数量图片；当rate=0时，只抽取第一张图片
    """
    i = 0
    make_my_dir(output_file)
    for dir_path, _, file_names in os.walk(input_file):
        print(dir_path)
        if file_names != []:
            file_number=len(file_names)
            if rate < 0 or rate > 1:
                print("Rate error! \n Automatic setting rate=0")
                rate = 0
            if rate == 0:
                sample = random.sample(file_names, 1)
            else:
                pick_number=int(file_number*rate)
                sample = random.sample(file_names, pick_number)
            for name in sample:
                if check_img(str(dir_path + '\\' + name)):
                    i += 1
                    shutil.copy(dir_path + '\\' + name, output_file + '\\' + str(i) + name)
                if i%1000==0 and i>0:
                    print(f"完成了{i}次！")
        if i >= num:
            break
    print("完成")


if __name__ == '__main__':
    copy_img(r'D:\wangwei\dataset\self_PAR_dataset\all_5union_datasets', r"D:\wangwei\dataset\test_data\out_put", num=100)    

