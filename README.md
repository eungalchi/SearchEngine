# SearchEngine with Python
# 머니포트 '검색 엔진' 부분 패키지


The code will look like the following:
```
cd SearchEngine
npm install
npm start
```


## 소프트웨어 & 하드웨어 리스트

* Python 3.5
* TensorFlow-Gpu 2.0
* Cuda 10.0.13
* Cudnn 7.6.4 
* Selenium
* Windows

```buildoutcfg
conda create -n tf_gpu python=3.5
activate tf_gpu
pip install --ignore-installed --upgrade tensorflow-gpu==2.0
```
              
## 필요 Python 패키지

pip install pandas selenium numpy sklearn bs4 pymysql xlrd openpyxl lxml nltk

## Python file

아직 ex5까지밖에 없는 상태.
있는 시나리오도 추가할 데이터와 수정부분이 있음.

### ○ main.py

* 문장일 읽고 시나리오를 판정.

* Input : ./vendor/USA_stocks.xlsx \
[columns : ticker]
* Ouput : ./news_data/Yahoo_Finance_News_Link_생성날짜.csv \ 
[columns : ticker, news_link]

### ○ find_columns.py

* 파서 역할
* 칼럼 매칭