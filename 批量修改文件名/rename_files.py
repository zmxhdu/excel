# coding=utf-8
import os
import re


def rename_files():
    path = os.getcwd()
    filelist = os.listdir(path)
    for file in filelist:
        if file[-2:] == 'py':
            continue
        filename,extension = file.split('.')
        new_name = re.findall(r'[0-9]{4}年[0-9]{2}月[0-9]{2}', filename)
        if new_name is null:
            continue
        new_name = new_name[-1:][0].replace('年', '-')
        new_name = new_name.replace('月', '-')
        newname = new_name+'.'+extension
        os.rename(file, newname)


if __name__ == '__main__':
    rename_files()
