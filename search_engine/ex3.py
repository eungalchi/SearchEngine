# 'ㅇㅇ'의 '시가총액'을 알려주세요. (완료)
# -*- coding: utf-8 -*-

from nltk.tokenize import word_tokenize
import re
import pandas as pd
import sys
from find_columns import *


Input = sys.argv[1] #input()

Input_list = list(Input)
# Input 전처리 -> 부터, 까지, 이, 을, 에, 가지, 개 등등 stopwords 필터링

stop = ['이', '을', '에', '가가', '개', '의', '던', '았', '었', '은', '를', '는', '인', '데']

new_input = ''
for inp in Input_list:
    if inp not in stop:
        new_input += inp

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