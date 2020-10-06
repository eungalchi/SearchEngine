# SearchEngine with Python
# Q & A
URL : http://3.34.174.254:3000/
# AIY 음성인식 


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

pip install ,,,

## Python file

아직 ex6까지밖에 없는 상태.
질문과 대답에 대한 추가적인 검토 후, 살을 붙일 예정.
재무 항목에 대하여 구분 방법 모색중. (동의어, 의미 처리)
율 / 양에 대한 기간 계산 단계 나누어야함.

### ○ main.py

* 문장을 읽고 시나리오를 판정.

### ○ find_columns.py

* SQL 칼럼에 대해 매칭.

### ○ input_processing.py

* 토큰 -> 형태소 분석 -> 불용어 삭제.
