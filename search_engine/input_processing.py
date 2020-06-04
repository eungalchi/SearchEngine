from nltk.tokenize import word_tokenize
from konlpy.tag import *
import re

okt = Okt()
dateReg = re.compile('^([12]\\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\\d|3[01]))')

stopwords = ['을', '에', '가', '개', '의', '던', '았', '었', '은', '를', '는', '인', '데', '이', '?', '부터', '까지', '만']


def in_preprocess(input):

    input_token = word_tokenize(input)
    #print(input_token)
    Input_list = []  # list(Input)
    for i in input_token:
        if not dateReg.match(i):
            a = okt.morphs(i, stem=True)
            Input_list += a
        else:
            Input_list.append(dateReg.match(i).group())

    #print(Input_list)
    #token = stop_word(Input_list)
    new_input = [i for i in Input_list if not i in stopwords]
    #print(new_input)

    return new_input
