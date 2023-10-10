
'''
리스트 안에 있으면 plot하기 쉬움. 랜덤 수 생성해서 x**2 + y**2 < 1이면 
inside 리스트 안에, >1이면 outside 리스트 안에 넣어주기
'''

import random
import matplotlib.pyplot as plt
import math

n = [1000, 10000, 100000]
x_lst = []
y_lst = []
x_inside = []
y_inside = []

for _ in range(n[2]):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    x_lst.append(x)
    y_lst.append(y)
    
    if (x**2 + y**2 <= 1):
        x_inside.append(x)
        y_inside.append(y)

print(f'points that are inside the circle: {len(x_lst)}')
print(f'approximation: {(4*len(x_inside)/n[2])}')
print(f'math.pi: {math.pi}')

plt.scatter(x_lst, y_lst, c='b')
plt.scatter(x_inside, y_inside, c='r')
plt.show()