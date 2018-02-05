import matplotlib.pyplot as plt
import pickle
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import jieba

import codecs

# fin = codecs.open('text.txt',mode = 'r', encoding = 'utf-8')
# print(fin.read())
#
# # 第一次运行程序时将分好的词存入文件
# text = ''
# with open('text.txt', encoding='utf-8') as fin:
#     for line in fin.readlines():
#         line = line.strip('\n')
#         text += ' '.join(jieba.cut(line))
#         text += ' '
# fout = open('cut_text.txt','wb')
# pickle.dump(text,fout)
# fout.close()

# 直接从文件读取数据
fr = open('cut_text.txt', 'rb')
text = pickle.load(fr)

backgroud_Image = plt.imread('timg.jpg')
wc = WordCloud( background_color = 'white',    # 设置背景颜色
                mask = backgroud_Image,        # 设置背景图片
                max_words = 20000,            # 设置最大现实的字数
                stopwords = STOPWORDS,        # 设置停用词
                font_path = 'C:/Users/Windows/fonts/msyh.ttf',# 设置字体格式，如不设置显示不了中文
                max_font_size = 100,            # 设置字体最大值
                random_state = 20,            # 设置有多少种随机生成状态，即有多少种配色方案
                )
wc.generate(text)
image_colors = ImageColorGenerator(backgroud_Image)
wc.recolor(color_func = image_colors)
plt.imshow(wc)
plt.axis('off')
plt.show()