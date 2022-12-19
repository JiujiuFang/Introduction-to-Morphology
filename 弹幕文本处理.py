import numpy as np
import pandas as pd
data = pd.read_csv(r'D:/pycharm/NaturalLanguageProcessing/弹幕合集.csv',sep=',',header=None)
data1=data.iloc[:,[1]]
data11=np.array(data1)
list1=data11.tolist()
list1
sent_list=[]
for sent in list1:
    for st in sent:
        sent_list.append(st)
sent_list
import re
pattern='[^\u4e00-\u9fa5\w]+'
tidy_list=[]
for sent in sent_list:
    if type(sent)==type('114514'):
        tidy_list.append(re.sub(pattern,'',sent))
tidy_list
import pkuseg
seg = pkuseg.pkuseg(user_dict="D:/pycharm/NaturalLanguageProcessing/dict_file.txt")
words=[]
for sent in tidy_list:
    word=seg.cut(sent)
    for ws in word:
        words.append(ws)
print(type(words))
dayu2dedanci=[]
for word in words:
    if len(word) >1:
        dayu2dedanci.append(word)
print(len(dayu2dedanci))


from nltk.probability import FreqDist
frequency_dist = FreqDist(dayu2dedanci)
frequency_dist
frequency_dist.most_common(1000)
top1000phrases=pd.DataFrame(frequency_dist.most_common(300),columns=['phrase','frequency'])
top1000phrases
top1000phrases.to_csv("D:/pycharm/NaturalLanguageProcessing/频率前300的弹幕.csv",encoding = 'utf_8_sig')
phrases=pd.DataFrame(frequency_dist.items(),columns=['phrase','frequency'])
phrases.to_csv("D:/pycharm/NaturalLanguageProcessing/弹幕分词.csv",encoding = 'utf_8_sig')


