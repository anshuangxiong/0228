import sys
import os
import jieba


# reload(sys)
# sys.setdefaultencoding('utf-8')

seg_list = jieba.cut("小明1995年毕业于北京清华大学", cut_all=False)
print(" ".join(seg_list))

seg_list = jieba.cut("小明1995年毕业于北京清华大学")
print(" ".join(seg_list))

seg_list = jieba.cut("小明1995年毕业于北京清华大学", cut_all=True)
print("/ ".join(seg_list))

seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")
print("/ ".join(seg_list))


def savefile(savepath, content):
    fp = open(savepath, 'wb')
    fp.write(content)
    fp.close()


def readfile(path):
    fp = open(path, 'rb')
    content = fp.read()
    fp.close()
    return content
