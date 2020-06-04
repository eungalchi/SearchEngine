# '시작날짜'부터 '끝날짜'까지 'AMD'의 '배당수익률'을 알려주세용 -django라는 가상환경 만들음!!!! ---------------------------------------> 계산이 필요
# -*- coding: utf-8 -*-

from nltk.tokenize import word_tokenize
import re
import pandas as pd
import sys
from find_columns import *
from input_processing import *


Input = sys.argv[1] #input()

token = in_preprocess(Input)


date_order = 0 # 날짜 순서 변수
start_date = None
end_date = None
fin = None
min_max = None
stock_code = None # 종목코드 -> 종목이라는 의미를 나타내는 것
code = None # 티커를 나타내는 것
count = 5 # 기본 다섯가지 보여줌

for word in token:
    #print("<" + word + ">")
    if find_count(word) is not None:
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


# 키워드 뽑기

# 키워드 부족한 부분 파악

# 다시 질문


sql = "select sum({}) ans from PLAN_DB where ASOFDATE > '{}' and ASOFDATE < '{}' and SYMBOL='{}' group by SYMBOL;".format(fin, start_date, end_date, code)
print(sql)
sys.stdout.flush()