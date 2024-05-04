from flask import Flask, jsonify
import pandas as pd
import numpy as np

# 서버 만들기

app=Flask(__name__)

np.random.seed(77)
names=['홍길동', '김철수', '이영희', '김민수']
data=np.random.randint(0, 101, 12).reshape(4, 3) # 원하는 행 열로 만들기
df = pd.DataFrame(data, columns=['국어', '영어', '수학'])
df.insert(0, '이름', names)

@app.route('/home')
def home():
    return jsonify(df.to_dict(orient='records'))
app.run(host='0.0.0.0', port=7888, debug=True)