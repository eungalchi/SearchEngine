# -*- coding: utf-8 -*-

from nltk.tokenize import word_tokenize
import re
import pandas as pd
import sys
from find_columns import *
from input_processing import *

# find_code, find_count, find_date, find_fin, find_min_max, find_stock_code

class Examples:

    def __init__(self):

        #self.Input = sys.argv[1]
        self.date_order = 0  # 날짜 순서 변수
        self.start_date = None
        self.end_date = None
        self.fin = None
        self.min_max = None
        self.stock_code = None  # 종목코드 -> 종목이라는 의미를 나타내는 것
        self.code = None  # 티커를 나타내는 것
        self.count = 5  # 기본 다섯가지 보여줌
        self.dateReg = re.compile('^([12]\\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\\d|3[01]))$')
        self.day = None  # 일자 변수
        self.date = '2020'
        self.dur = None

        #self.token = in_preprocess(self.Input)
        '''
        #Input_list = list(Input)
        # Input 전처리 -> 부터, 까지, 이, 을, 에, 가지, 개 등등 stopwords 필터링
        
        okt = Okt()
        Input_list = okt.morphs(Input, stem=True)
        print(Input_list)
        
        token = stop_word(Input_list)
        #token = word_tokenize(new_input) # 입력 문장의 토큰화
        print(token)
        '''

    def ex1(self, text):
        # '시작날짜' 부터 '끝날짜' 까지 가장 '수익률'이 '큰' '3'가지 '종목'을 보여주세요 ---------------------------------> 계산이 필요!, 기간이 있으면 계산이 필요하다!
        # 시작날짜 부터 끝날짜 까지 가장 주가수익률 큰 3가지 종목을 보여주세요

        token = in_preprocess(text)

        date_order = self.date_order  # 날짜 순서 변수
        start_date = self.start_date
        end_date = self.end_date
        fin = self.fin
        min_max = self.min_max
        stock_code = self.stock_code  # 종목코드 -> 종목이라는 의미를 나타내는 것
        code = self.code  # 티커를 나타내는 것
        count = self.count  # 기본 다섯가지 보여줌

        for word in token: # 혹시 모르게 토큰이 잡힐 수 있으므로 sql문에 맞는 if문만 넣기!
            #print("<" + word + ">")
            if code is None: # code를 찾지 못했으면
                code = find_code(word)
            if fin is None:
                fin = find_fin(word)
            if min_max is None:
                min_max = find_min_max(word)
            if (start_date is None) or (end_date is None):
                if date_order == 0: # 첫번째 날짜를 찾음
                    start_date = find_date(word, date_order)
                    if start_date is not None: # 첫번째 날짜를 찾았을 때 순서를 다음으로 넘김
                        date_order += 1
                else: # 첫번째 날짜를 이미 찾은 상태
                    if find_date(word, date_order) is not None: # 두번째 날짜가 있으면
                        end_date = find_date(word, date_order) # 두번째 날짜 변수 저장
            if stock_code is None:
                stock_code = find_stock_code(word)
            if find_count(word) is not None:
                count = find_count(word)

        sql = "select distinct({}) ans from PLAN_DB where ASOFDATE > '{}' and ASOFDATE < '{}' order by {} {} limit {};".format(stock_code, start_date, end_date, fin, min_max, count)
        return sql


    def ex2(self, text):
        # (최근에/오늘/어제/날짜) 가장 '수익률'이 '큰' '3'가지 '종목'을 보여주세요 (완료)
        # 최근만 학습했지만 오늘, 어제도 다 인식했음 (20.05.27기준)

        token = in_preprocess(text)

        dateReg = self.dateReg
        date_order = self.dateReg  # 날짜 순서 변수
        start_date = self.start_date
        fin = self.fin
        min_max = self.min_max
        stock_code = self.stock_code  # 종목코드 -> 종목이라는 의미를 나타내는 것
        code = self.code  # 티커를 나타내는 것
        count = self.count  # 기본 다섯가지 보여줌
        day = self.day  # 일자 변수
        date = self.date

        for word in token:
            # print("<" + word + ">")
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
            if day is None:
                day = find_day(word)
            if start_date is None:
                start_date = find_date(word, date_order)
            if find_date2(word) is not None:  # not dateReg.search(date):
                date += str(find_date2(word))

        if start_date is None and dateReg.search(date):
            start_date = date

        # CURDATE() 변경해야 함!
        if start_date is None:  # 날짜가 없으면
            if day is None:  # 일자도 없으면
                day = '0'  # 기본이 당일
            sql = 'select distinct({}) ans from PLAN_DB where ASOFDATE = ("2019-12-31" - INTERVAL {} DAY) order by {} {} limit {};'.format(
                stock_code, day, fin, min_max, count)
        else:
            sql = "select distinct({}) ans from PLAN_DB where ASOFDATE = '{}' order by {} {} limit {};".format(
                stock_code, start_date, fin, min_max, count)
        return sql


    def ex3(self, text):
        # (최근에/오늘/어제/날짜) 'ㅇㅇ'의 '시가'를 알려주세요.

        token = in_preprocess(text)

        dateReg = self.dateReg
        date_order = self.date_order  # 날짜 순서 변수
        start_date = self.start_date
        fin = self.fin
        code = self.code  # 티커를 나타내는 것
        day = self.day
        date = self.date

        for word in token:
            if code is None:  # code를 찾지 못했으면
                code = find_code(word)
            if fin is None:
                fin = find_fin(word)
            if day is None:
                day = find_day(word)
            if start_date is None:
                start_date = find_date(word, date_order)
            if not dateReg.search(date):
                date += str(find_date2(word))

        if start_date is None and dateReg.search(date):
            start_date = date

        # CURDATE() 변경해야 함!
        if start_date is None:  # 날짜가 없으면
            if day is None:  # 일자도 없으면
                day = '0'  # 기본이 당일
            sql = "select {} ans from PLAN_DB where ASOFDATE = ('2019-12-31' - INTERVAL {} DAY) and SYMBOL='{}';".format(
                fin, day, code)
        else:
            sql = "select {} ans from PLAN_DB where ASOFDATE = '{}' and SYMBOL = '{}';".format(fin, start_date, code)
        return sql


    def ex4(self, text):
        # '최근 일주일동안' '거래량'(총액)이 가장 '많'았던 '종목'을 '4'가지 알려주세요. (완료) -----------------------------------------------------> 계산이 필요
        # 최근 한달동안

        token = in_preprocess(text)

        fin = self.fin
        min_max = self.min_max
        stock_code = self.stock_code  # 종목코드 -> 종목이라는 의미를 나타내는 것
        code = self.code  # 티커를 나타내는 것
        count = self.count  # 기본 다섯가지 보여줌
        dur = self.dur

        for word in token:
            # print("<" + word + ">")
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
        sql = 'select {} ans from PLAN_DB where ASOFDATE BETWEEN DATE_ADD("2019-12-31",INTERVAL -1 {} ) AND NOW() group by {} order by sum({}) {} limit {};'.format(
            stock_code, dur, stock_code, fin, min_max, count)
        return sql


    def ex5(self, text):
        # '시작날짜'부터 '끝날짜'까지 'AMD'의 '배당수익률'을 알려주세용 -django라는 가상환경 만들음!!!! ---------------------------------------> 계산이 필요

        token = in_preprocess(text)

        date_order = self.date_order
        start_date = self.start_date
        end_date = self.end_date
        fin = self.fin
        min_max = self.min_max
        stock_code = self.stock_code  # 종목코드 -> 종목이라는 의미를 나타내는 것
        code = self.code  # 티커를 나타내는 것

        for word in token:
            # print("<" + word + ">")
            if fin is None:
                fin = find_fin(word)
            if min_max is None:
                min_max = find_min_max(word)
            if (start_date is None) or (end_date is None):
                if date_order == 0:
                    start_date = find_date(word, date_order)
                    if start_date is not None:
                        date_order += 1
                else:
                    if find_date(word, date_order) is not None:
                        end_date = find_date(word, date_order)
            if code is None:  # code를 찾지 못했으면
                code = find_code(word)
            if stock_code is None:
                stock_code = find_stock_code(word)

        sql = "select sum({}) ans from PLAN_DB where ASOFDATE > '{}' and ASOFDATE < '{}' and SYMBOL='{}' group by SYMBOL;".format(
            fin, start_date, end_date, code)
        return sql


    def ex6(self, text):
        ## '최근 일주일동안' '록히드마틴'의 '시가''(총액)'을 알려주세요. (완료) ------------------------------------------------------------> 계산이 필요!
        # 최근 한달동안

        token = in_preprocess(text)

        fin = self.fin
        code = self.code  # 티커를 나타내는 것
        dur = self.dur

        for word in token:  # 혹시 모르게 토큰이 잡힐 수 있으므로 sql문에 맞는 if문만 넣기!
            # print("<" + word + ">")
            if code is None:  # code를 찾지 못했으면
                code = find_code(word)
            if fin is None:
                fin = find_fin(word)
            if dur is None:
                dur = find_dur(word)

        # NOW() 변경해야 함!!
        sql = "select sum({}) ans from PLAN_DB where ASOFDATE BETWEEN DATE_ADD('2019-12-31', INTERVAL -1 {} ) AND NOW() and SYMBOL='{}';".format(
            fin, dur, code)
        return sql


