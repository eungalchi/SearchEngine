import re
import pandas as pd
import sys


category = { '시가' : 'OPEN_PRICE', # '가'에 대한 처리, 시가 = 시 (동의어 처리)
             '고가' : 'HIGH_PRICE',
             '저가' : 'LOW_PRICE',
             '종가' : 'LAST_PRICE',
             '거래량' : 'VOLUME',
             '수정계수' : 'ADJUST_RATE',
             '수정주가' : 'ADJUST_PRICE',
             '상장주식수' : 'Num_Stock',
             '일반주식수' :'OrdinarySharesNumber',
             '발행자본재고' :'IssuanceOfCapitalStock',
             '장기부채' : 'LongDebt',
             '자본임대의무' : 'LongTermDebtAndCapitalLeaseObligation',
             '자본금' : 'Capital',
             '자본총계' : 'Total_Capital',
             '당기순이익' : 'Net_Income',
             '매출총이익' : 'Gross_Profit',
             '자산총계' : 'Total_Asset',
             '부채총계' : 'Total_liabilities',
             '투자자산' : 'Investments',
             '잉여현금흐름' : 'Free_Cash_Flow',
             '매출액' : 'Revenues',
             '이익잉여금' : 'RETAINEDEARNINGS',
             'EBIT' : 'EBIT',
             'EBITDA' : 'EBITDA',
             '부채비율' : 'Liabilities_Rate',
             '현금' : 'CASHANDCASHEQUIVAL', # +현금등가물
             '유동자산' : 'Current_Asset',
             '유동부채' : 'CURRENTDEBT',
             '현재부채' : 'CURRENTDEBTANDCAPITALLEASEOBLIGATION',
             '순부채' : 'Net_Loss',
             '영업활동현금흐름' : 'continuous_CFO', # 영업활동으로 인한 현금흐름
             '주당배당금' : 'DPS',
             '평균주식수' : 'BASICAVERAGESHARES',
             'EPS' : 'EPS',
             'ROIC' : 'ROIC',
             '영업이익률' : 'Operating_Income_Rate',
             '유동비율' : 'Current_Ratio',
             '배당성향' : 'PAYOUTRATIO',
             'PER' : 'PERRATIO',
             'PSR' : 'PSRRATIO',
             'PBR' : 'PBRRATIO',
             'PCF' : 'PCFRATIO',
             'PEG' : 'PEGRATIO',
             'EV/EBIT' : 'EVTOEBIT'
             }


Adj = {'최대' : 'desc', '큰' : 'desc', '많' : 'desc', '컸' : 'desc', '높' : 'desc', '최소' : 'asc', '낮' : 'asc', '작' : 'asc', '적' : 'asc'}

stocks = ['종목', '종목코드', '코드', '주식', '티커']

stock = pd.read_excel(r'USA_stocks.xlsx')

stock_name = stock['종목명'].tolist()
ticker = stock['종목코드'].tolist()


countReg = re.compile('[0-9]+(가지)?$')
dateReg = re.compile('^([12]\\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\\d|3[01]))')


def find_fin(word):
    if word in category.keys():
        #print(word) # 재무항목 fin 칼럼명 필요
        return category.get(word)


def find_min_max(word):
    if word in Adj.keys():
        #print(Adj.get(word))
        return Adj.get(word)


def find_count(word):
    if countReg.search(word):
        #print("count " + re.search('[0-9]+', word).group())
        return re.search('[0-9]+', word).group()
    elif word in ['가장', '제일']:
        return 1
        #print("count 1")


def find_code(word):
    if (word in ticker) or (word in stock_name): # 어느 종목인지 확인
        if word in stock_name:
            code_v = stock[stock['종목명'] == word].values
            #print("종목 : " + code[0][1])
            return code_v[0][1]
        else:
            #print("종목 : " + word)
            return word


def find_date(word, date_order):
    if dateReg.search(word) and date_order == 0: # 시작날짜가 보통 앞에 온다.
        return dateReg.search(word).group()
    elif dateReg.match(word) and date_order == 1:
        return dateReg.match(word).group()


def find_stock_code(word):
    if word in stocks:
        #print("SYMBOL")
        return 'SYMBOL'


def find_dur(word):
    if word.startswith("일주일") or word.startswith("1주"):
        return 'WEEK'
    elif word.startswith("한달") or word.startswith("1달"):
        return 'MONTH'



if __name__ == '__main__':
    print("This is find_columns.py")