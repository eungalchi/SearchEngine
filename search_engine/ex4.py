# '최근 일주일동안' '거래량'(총액)이 가장 '많'았던 '종목'을 '4'가지 알려주세요. (완료) -----------------------------------------------------> 계산이 필요
# 최근 한달동안

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
dur = None

for word in token:
    #print("<" + word + ">")
    if code is None:  # code를 찾지 못했으면
        code = find_code(word)
    if fin is None:
        fin = find_fin(word)
    if min_max is None:
        min_max = find_min_max(word)
    if find_count(word) is not None:
        count = find_count(word)
    if stock_code is None:
        stock_code = find_stock_code(word)
    if dur is None:
        dur = find_dur(word)


# 후에 NOW() 변경
sql = 'select {} ans from PLAN_DB where ASOFDATE BETWEEN DATE_ADD("2019-12-31",INTERVAL -1 {} ) AND NOW() group by {} order by sum({}) {} limit {};'.format(stock_code, dur, stock_code, fin, min_max, count)
print(sql)
sys.stdout.flush()