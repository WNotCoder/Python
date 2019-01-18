# -*- coding: utf-8 -*-
import codecs
import sys

import tomd

reload(sys)
#sys.setdefaultencoding('utf8')  # 设置默认编码格式为'utf-8'

save_file = 'D:\\TEMP\\md'


def run():
    html = getHtml()
    print
    html
    mdTxt = tomd.Tomd(html).markdown
    print
    'markdown :{}'.format(mdTxt)
    createFile(mdTxt)


def createFile(mdTxt):

    print('准备写入文件：{}'.format(save_file))
    # r+ 打开一个文件用于读写。文件指针将会放在文件的开头。
    # w+ 打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
    # a+ 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
    f = codecs.open(save_file, 'w+', 'utf-8')
    # f.write('###{}\n'.format(url))
    f.write(mdTxt)
    # f.write(mdTxt)
    f.close()
    print
    '写入文件结束：{}'.format(f.name)


