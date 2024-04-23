import numpy as np

x=np.array(
    [
    [-1,-1,1,1],
    [-1,1,-1,1]
    ])
t=np.array([-1,1,1,1])
print(x,t,sep='\n ')


w1=0.5
w2=0.5
b=0.1
epochs = 5
alpha = 0.1

def act_fun(yin):
    if yin>=0:
        return 1
    else:
        return -1

# err_tolerance = 0.1
for j in range(epochs):
    print("epoch :",j+1)
    mse = 0
    for i in range(x.shape[0]):
        x1 = x[0][i]
        x2 = x[1][i]
        yin = b + w1*x1 + w2*x2
        error = (t[i]-yin)
        mse += error*error
        print("error =",error)

        w1 = w1 + alpha*error*x1
        w2 = w2 + alpha*error*x2
        b = b + alpha*error

        print(f'({x1:2},{x2:2} {t[i]:2}) , {yin:2} , ({w1:2},{w2:2},{b:2})')
    print("mse =",mse/4,"\n")
