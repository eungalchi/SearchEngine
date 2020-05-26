# 'ㅇㅇ'의 '시가'를 알려주세요. (완료, 사실상 ex7과 겹침!!!!)
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

for word in token:
    if code is None:  # code를 찾지 못했으면
        code = find_code(word)
    if fin is None:
        fin = find_fin(word)


sql = "select {} ans from PLAN_DB where SYMBOL='{}' order by ASOFDATE desc limit 1;".format(fin, code)
print(sql)
sys.stdout.flush()