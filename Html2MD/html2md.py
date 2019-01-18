# -*- coding: utf-8 -*-
import codecs
import os

import tomd

load_file_path = "D:\\TEMP\\ori"

save_file_path = "D:\\TEMP\\md"

def getHtml(load_file_path):
    f = open(load_file_path,'r',encoding='utf-8')
    filename = os.path.basename(load_file_path).split('.')[0]
    print('正在读取：' + str(filename))
    return f,filename

def convertHtml(file):
    print('已读取：' + str(len(file.read())))
    content =  tomd.Tomd(file.read()).markdown
    print('已转换：' + str(len(content)))
    file.close()
    return content

def wrtMarkdown(file_content, file_name):
    depath = os.path.join(save_file_path, file_name + '.md')
    f = open(depath, 'w', encoding='utf-8')
    f.write(file_content)
    f.close()
    return None

if __name__ == '__main__':
    for parent, dirnames, filenames in os.walk(load_file_path, followlinks=True):
        for filename in filenames:
            full_path = os.path.join(parent, filename)
            temp_file, temp_name = getHtml(full_path)
            wrtMarkdown(convertHtml(temp_file),temp_name)





