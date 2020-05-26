# [최근/오늘/어제] 'ㅇㅇ'의 '시가'를 알려주세요.
# -*- coding: utf-8 -*-

from nltk.tokenize import word_tokenize
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
stock_code = None # 종목코드 -> 종목이라는 의미를 나타내는 것
code = None # 티커를 나타내는 것
day = None # 1일짜리 변수

for word in token: # 혹시 모르게 토큰이 잡힐 수 있으므로 sql문에 맞는 if문만 넣기!
    #print("<" + word + ">")
    if code is None: # code를 찾지 못했으면
        code = find_code(word)
    if fin is None:
        fin = find_fin(word)
    if day is None:
        day = find_day(word)



# 키워드 뽑기

# 키워드 부족한 부분 파악

# 다시 질문
# CURDATE() 변경해야 함!
sql = "select {} ans from PLAN_DB where ASOFDATE = ('2019-12-31' - INTERVAL {} DAY) and SYMBOL='{}';".format(fin, day, code)
print(sql)
sys.stdout.flush()