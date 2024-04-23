
import numpy as np

x1=np.array([1,1,-1,-1])
x2=np.array([1,-1,1,-1])
t=np.array([1,-1,-1,-1])


def act_fun(yin):
    if yin>=0:
        return 1
    elif yin<0:
        return -1
    else:
        return 0
epochs = 5
alpha = 1
w1=0
w2=0
b=0

while(epochs):
    for i in range(4):
        yin = b + w1*x1[i] + w2*x2[i]
        y = act_fun(yin)
        if y!=t[i]:
            w1 = w1 + alpha*x1[i]*t[i]
            w2 = w2 + alpha*x2[i]*t[i]
            b = b + t[i]
        print(f'({x1[i]:2},{x2[i]:2} {t[i]:2}) , ({yin:2},{y:2}) , ({w1:2},{w2:2},{b:2})')
    epochs-=1
    print()
