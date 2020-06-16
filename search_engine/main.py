# -*- coding: utf-8 -*-

import json
from tensorflow.python.keras.preprocessing.text import Tokenizer
from tensorflow.python.keras.models import load_model
import numpy as np
import sys
import Examples


def vectorize_sequences(sequences, dimension=10000):
    results = np.zeros((len(sequences), dimension)) # 크기가 들어온 리스트 (단어개수, 전체단어개수)이고, 모든 원소가 0인 행렬을 생성
    for i, sequence in enumerate(sequences):
        results[i, sequence] = 1.
    return results


def predict(Input):
    text = []

    text.append(Input)
    text = tokenizer.texts_to_sequences(text)
    text = vectorize_sequences(text)

    predictions = model.predict(text)

    num = np.argmax(predictions[0])

    return num


model = load_model('search_engine/show_example.h5') #

tokenizer = Tokenizer()

with open('search_engine/Word_Index.json', encoding='utf8') as json_file: #
    word_index = json.load(json_file)
    tokenizer.word_index = word_index

Input = sys.argv[1]

num = predict(Input)

#print(num)
examples = Examples.Examples()


if num == 1:
    sql = examples.ex1(Input)
elif num == 2:
    sql = examples.ex2(Input)
elif num == 3:
    sql = examples.ex3(Input)
elif num == 4:
    sql = examples.ex4(Input)
elif num == 5:
    sql = examples.ex5(Input)
elif num == 6:
    sql = examples.ex6(Input)


print(sql)
sys.stdout.flush() #[0.01385196 0.00908347 0.