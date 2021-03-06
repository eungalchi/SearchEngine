# (날짜에) 가장 '수익률'이 '큰' '3'가지 '종목'을 보여주세요 (완료)xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# -*- coding: utf-8 -*-

from nltk.tokenize import word_tokenize
from find_columns import *
from input_processing import *


Input = sys.argv[1]

Input_list = list(Input)
# Input 전처리 -> 부터, 까지, 이, 을, 에, 가지, 개 등등 stopwords 필터링

new_input = stop_word(Input_list)

token = word_tokenize(new_input) # 입력 문장의 토큰화
print(token)


date_order = 0 # 날짜 순서 변수
start_date = None
fin = None
min_max = None
stock_code = None # 종목코드 -> 종목이라는 의미를 나타내는 것
code = None # 티커를 나타내는 것
count = None # 기본 다섯가지 보여줌
count_b = None

#print(list(filter(find_fin, token)))

for word in token:
    #print("<" + word + ">")
    if fin is None:
        fin = find_fin(word)
    if min_max is None:
        min_max = find_min_max(word)
    if start_date is None:
        start_date = find_date(word, date_order)
    if count is None or count == 1:
        if count == 1:
            count_b = 1
        count = find_count(word)
    if stock_code is None:
        stock_code = find_stock_code(word)


if count is None: # '가장'만 있을 때는 한 종목만, 가짓수가 있을 때는 그 개수만큼, 없을 때는 기본 5가지
    if count_b == 1:
        count = count_b
    else :
        count = 5



sql = "select distinct({}) ans from PLAN_DB where ASOFDATE = '{}' order by {} {} limit {};".format(stock_code, start_date, fin, min_max, count)
print(sql)
sys.stdout.flush()