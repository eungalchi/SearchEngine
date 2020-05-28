# (최근에/오늘/어제/날짜) 'ㅇㅇ'의 '시가'를 알려주세요.
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
fin = None
code = None # 티커를 나타내는 것
day = None

for word in token:
    if code is None:  # code를 찾지 못했으면
        code = find_code(word)
    if fin is None:
        fin = find_fin(word)
    if day is None:
        day = find_day(word)
    if start_date is None:
        start_date = find_date(word, date_order)


if start_date is None: # 날짜가 없으면
    if day is None: # 일자도 없으면
        day = '0' # 기본이 당일
    sql = "select {} ans from PLAN_DB where ASOFDATE = ('2019-12-31' - INTERVAL {} DAY) and SYMBOL='{}';".format(fin, day, code)
else:
    sql = "select {} ans from PLAN_DB where ASOFDATE = '{}' and SYMBOL = '{}';".format(fin, start_date, code)
print(sql)
sys.stdout.flush()


# sql = "select {} ans from PLAN_DB where SYMBOL='{}' order by ASOFDATE desc limit 1;".format(fin, code)