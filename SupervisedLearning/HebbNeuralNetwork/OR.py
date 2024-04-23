import numpy as np

x1 = np.array([-1,-1,1,1])
x2 = np.array([-1,1,-1,1])
y  = np.array([-1,1,1,1])

w1 = 0
w2 = 0
b = 0

for i in range(4):
    print(f"Before update :{i,w1,w2,b}")
    w1 = w1 + x1[i]* y[i]
    w2 = w2 + x2[i] * y[i]
    b = b + y[i]
    print(f"After update :{i,w1,w2,b}")

y_predict = np.array( [0,0,0,0] )
for i in range(4):
    y_in = w1*x1[i] + w2 * x2[i] + b
    if y_in > 0 :
        y_predict[i] = 1
    else :
        y_predict[i] = -1

print(y_predict)
