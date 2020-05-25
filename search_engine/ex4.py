# '최근 일주일동안' '거래량'이 가장 '많'았던 '종목'을 '4'가지 알려주세요. (완료)
# 최근 한달동안
#

# -*- coding: utf-8 -*-

from nltk.tokenize import word_tokenize
import re
import pandas as pd
import sys
from find_columns import *


Input = input() #sys.argv[1] #input()

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
count_b = None
dur = None

for word in token:
    #print("<" + word + ">")
    if code is None:  # code를 찾지 못했으면
        code = find_code(word)
    if fin is None:
        fin = find_fin(word)
    if min_max is None:
        min_max = find_min_max(word)
    if count is None or count == 1:
        if count == 1:
            count_b = 1
        count = find_count(word)
    if stock_code is None:
        stock_code = find_stock_code(word)
    if dur is None:
        dur = find_dur(word)

if count is None: # '가장'만 있을 때는 한 종목만, 가짓수가 있을 때는 그 개수만큼, 없을 때는 기본 5가지
    if count_b == 1:
        count = count_b
    else :
        count = 5

sql = 'select {} ans from PLAN_DB where ASOFDATE BETWEEN DATE_ADD(NOW(),INTERVAL -21 {} ) AND NOW() group by {} order by sum({}) {} limit {};'.format(stock_code, dur, stock_code, fin, min_max, count)
print(sql)
sys.stdout.flush()