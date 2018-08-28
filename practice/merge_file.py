# !/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import time
import shutil
import hashlib

# 计算文件md5的值
def get_file_md5(filename):
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    f = open(filename,"rb")
    while True:
        b = f.read(8096)
        print (b)
        if not b:
            break
        myhash.update(b)
        f.close()
        return myhash.hexdigest()

# 判断两个文件是否相同，如果不同表示修改过
def is_modify(file1, file2):
    # 参数是绝对路径
    return get_file_md5(file1) != get_file_md5(file2)

# 将时间戳换成时间显示格式
def stamp2_time(stamp):
    time_array = time.local(stamp)
    Time = time.strftime("%Y年%m月%D日 %H时%M分%S秒 旧文件副本", time_array)
    return Time

# 合并两个目录
def merge(A_path,B_path):
    B_paths = os.listdir(B_path)
    for fp in os.listdir(A_path):
        A_new_path = os.path.join(A_path,fp)
        B_new_path = os.path.join(B_path,fp)
        if os.path.isdir(A_new_path):
            if os.path.exists(B_new_path):
                merge(A_new_path,B_new_path)
            else:
                print("[目录]\t%s ===> %s"%(A_new_path,B_new_path))
                shutil.copytree(A_new_path,B_new_path)

        elif os.path.isfile(A_new_path):
            if os.path.exists(B_new_path):
                s = os.stat(B_new_path)
                if is_modify(A_new_path,B_new_path) == True:
                    # 创建副本
                    suffix = B_new_path.split(".")[-1]
                    # 将B中原文件创建副本
                    B_copy_path = B_new_path[:len(suffix)-1]+"%s."%(stamp2_time(s.st_mtime))+suffix
                    print("[副本]\t%s ===> %s" % (B_new_path, B_copy_path))
                    shutil.copy2(B_new_path,B_copy_path)
                    # 将A中的文件复制过来
                    print("[文件]\t%s ===> %s" % (B_new_path, B_copy_path))
                    shutil.copy2(A_new_path, B_new_path)
                else:
                    pass

            else:
                print ('[文件]\t%s ===> %s' % (A_new_path, B_new_path))
                shutil.copy2(A_new_path, B_new_path)

# 运行模式
if __name__ == '__main__':
    print ("""
         欢迎使用PathMerge！
         本程序将会把目录A合并到目录B，即 A ===> B
         将A目录中修改的内容在B目录中更新
         合并规则具体见 PathMerge.Help()
         """)
    if len(sys.argv) == 1:
        path1 = input('请输入A目录：').strip()
        path2 = input('请输入B目录：').strip()
    elif len(sys.argv) == 2:
        path1 = sys.argv[1].strip()
        print ('A目录为：%s\n' % (path1))
        path2 = input('请输入B目录：').strip()
    elif len(sys.argv) == 3:
        path1 = sys.argv[1].strip()
        print ('A目录为：%s\n' % (path1))
        path2 = sys.argv[2].strip()
        print ('B目录为：%s\n' % (path2))
    else:
        print ('ERROR：参数错误!\n参数最多有三个!\n')
        input('\n请按回车键(Enter)退出……')
        sys.exit(0)
        # 去除目录的引号
    if path1[0] == '\"':
        path1 = path1[1:-1]
    if path2[0] == '\"':
        path2 = path2[1:-1]

    print( """
            开始合并目录 %s到目录 %s%s ===> %s
            """ % (path1, path2, path1, path2))

    try:
        print ('合并中……')
        merge(path1, path2)
    except (Exception) as e:
        print ('合并失败！')
        print ('失败原因：\n',e)
    else:
        print ('合并成功！')

    input('\n请按回车键(Enter)退出……')
