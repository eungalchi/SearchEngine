# '시작날짜'부터 '끝날짜'까지 'AMD'의 '배당수익률'을 알려주세용 -django라는 가상환경 만들음!!!! ---------------------------------------> 계산이 필요
# -*- coding: utf-8 -*-

from nltk.tokenize import word_tokenize
import re
import pandas as pd
import sys
from find_columns import *
from input_processing import *


Input = sys.argv[1] #input()

Input_list = list(Input)
# Input 전처리 -> 부터, 까지, 이, 을, 에, 가지, 개 등등 stopwords 필터링

new_input = stop_word(Input_list)

token = word_tokenize(new_input) # 입력 문장의 토큰화
#print(token)


date_order = 0 # 날짜 순서 변수
start_date = None
end_date = None
fin = None
min_max = None
stock_code = None # 종목코드 -> 종목이라는 의미를 나타내는 것
code = None # 티커를 나타내는 것
count = None # 기본 다섯가지 보여줌
count_b = None

for word in token:
    #print("<" + word + ">")
    if count is None or count == 1:
        if count == 1:
            count_b = 1
        count = find_count(word)
    if fin is None:
        fin = find_fin(word)
    if min_max is None:
        min_max = find_min_max(word)
    if (start_date is None) or (end_date is None):
        if date_order == 0:
            start_date = find_date(word, date_order)
            if start_date is not None:
                date_order +=1
        else:
            end_date = find_date(word, date_order)
    if code is None:  # code를 찾지 못했으면
        code = find_code(word)
    if stock_code is None:
        stock_code = find_stock_code(word)


if count is None: # '가장'만 있을 때는 한 종목만, 가짓수가 있을 때는 그 개수만큼, 없을 때는 기본 5가지
    if count_b == 1:
        count = count_b
    else :
        count = 5


# 키워드 뽑기

# 키워드 부족한 부분 파악

# 다시 질문


sql = "select sum({}) ans from PLAN_DB where ASOFDATE > '{}' and ASOFDATE < '{}' and SYMBOL='{}' group by SYMBOL;".format(fin, start_date, end_date, code)
print(sql)
sys.stdout.flush()