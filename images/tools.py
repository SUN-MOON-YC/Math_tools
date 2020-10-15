#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：yangchao  albert time:2020/9/13

# _*_ coding:utf-8   _*_
# 开发团队：明日科技
# 开发人员：Administrator
# 开发时间：2019/4/9 17:46
# 文件名称：tools.py.py
# 开发工具：PyCharm

import base64


def handle_jpg_to_py(picture_name):
    """
    将JPG图像文件转换为.py文件
    :param picture_name:图片名称 images/YC_icon.png
    """
    open_jpg = open("C:/Users/Administrator/PycharmProjects/Math Tools/images/%s.png" % picture_name, 'rb')# 后缀为png的图片
    b64str = base64.b64encode(open_jpg.read())
    open_jpg.close()
    # 注意b64str一定要加上.decode()
    write_data = 'img = "%s"' % b64str.decode()
    f = open('%s.py' % picture_name, 'w+')
    f.write(write_data)
    f.close()

if __name__ == '__main__':
    picture = ['YC_icon']
    for pictrue_position in picture:
        handle_jpg_to_py(pictrue_position)
