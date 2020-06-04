## '최근 일주일동안' '록히드마틴'의 '시가''(총액)'을 알려주세요. (완료) ------------------------------------------------------------> 계산이 필요!
# 최근 한달동안
# -*- coding: utf-8 -*-

from nltk.tokenize import word_tokenize
from find_columns import *
from input_processing import *


Input = sys.argv[1] #input()

token = in_preprocess(Input)


date_order = 0 # 날짜 순서 변수
fin = None
code = None # 티커를 나타내는 것
dur = None


for word in token: # 혹시 모르게 토큰이 잡힐 수 있으므로 sql문에 맞는 if문만 넣기!
    #print("<" + word + ">")
    if code is None: # code를 찾지 못했으면
        code = find_code(word)
    if fin is None:
        fin = find_fin(word)
    if dur is None:
        dur = find_dur(word)


# 키워드 뽑기

# 키워드 부족한 부분 파악

# 다시 질문
# NOW() 변경해야 함!!
sql = "select sum({}) ans from PLAN_DB where ASOFDATE BETWEEN DATE_ADD('2019-12-31', INTERVAL -1 {} ) AND NOW() and SYMBOL='{}';".format(fin, dur, code)
print(sql)
sys.stdout.flush()