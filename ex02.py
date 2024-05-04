import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(77)
names=['홍길동', '김철수', '이영희', '김민수']
data=np.random.randint(0, 101, 12).reshape(4, 3) # 원하는 행 열로 만들기
df = pd.DataFrame(data, columns=['국어', '영어', '수학'])
df.insert(0, '이름', names)
print(df)

plt.rc('font', family='Malgun Gothic')
df = df.set_index('이름')
df.plot.bar()

plt.title('성적')
plt.xlabel('이름')
plt.ylabel('점수')
plt.xticks(rotation=0)
plt.grid()
plt.show()

print(df)
