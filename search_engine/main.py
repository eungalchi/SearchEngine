# -*- coding: utf-8 -*-

import json
from tensorflow.python.keras.preprocessing.text import Tokenizer
from tensorflow.python.keras.models import load_model
import numpy as np
import sys


def vectorize_sequences(sequences, dimension=16890):
    results = np.zeros((len(sequences), dimension)) # 크기가 들어온 리스트 (단어개수, 전체단어개수)이고, 모든 원소가 0인 행렬을 생성
    for i, sequence in enumerate(sequences):
        results[i, sequence] = 1.
    return results


model = load_model('search_engine/show_example.h5')

tokenizer = Tokenizer()

with open('search_engine/Word_Index.json', encoding='utf8') as json_file:
    word_index = json.load(json_file)
    tokenizer.word_index = word_index

Input = sys.argv[1]

text = []

text.append(Input)
text = tokenizer.texts_to_sequences(text)
text = vectorize_sequences(text)

predictions = model.predict(text)

result = np.argmax(predictions[0])

print(result)
sys.stdout.flush() #[0.01385196 0.00908347 0.09323713 0.8412105  0.00990491 0.03271199][0.016575   0.01922248 0.02787459 0.8444567  0.05447358 0.03739763]
