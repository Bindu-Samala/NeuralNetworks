import numpy as np

x=np.array(
    [
        [1,1,-1,-1],
        [1,-1,1,-1]
    ])
t=np.array([1,1,1,-1])
print(x,t,sep='\n ')
# ---X1-----Z1
#      \    /  \
#       \  /    \
#        \/      Y
#        /\     /
#       /  \   /
#      /    \ /
# ---X2-----Z2



#initial wts
w11=0.05
w21=0.2
b1=0.3

w12=0.1
w22=0.2
b2=0.15

epochs = 3
alpha = 0.5

# fixed wts
v1=0.5
v2=0.5
b3=0.5

def act_fun(yin):
    if yin>=0:
        return 1
    else:
        return -1

while(epochs):
    mse=0
    for i in range(4):
        x1 = x[0][i]
        x2 = x[1][i]
        zin1 = b1 + w11*x1 + w21*x2
        zin2 = b2 + w12*x1 + w22*x2

        z1 = act_fun(zin1)
        z2 = act_fun(zin2)

        yin = b3 + v1*z1 + v2*z2
        y = act_fun(yin)

        if t[i]!=y:
            w11 = w11 + alpha*(t[i]-zin1)*x1
            w12 = w12 + alpha*(t[i]-zin2)*x1
            b1 = b1 + alpha*(t[i]-zin1)

            w21 = w21 + alpha*(t[i]-zin1)*x2
            w22 = w22 + alpha*(t[i]-zin2)*x2
            b2 = b2 + alpha*(t[i]-zin2)

        mse += (t[i]-yin)**2
        print(f'({zin1:2} {zin2:1}) , ({yin:2} , ({w11:2},{w21:2},{b1:2},{w12:2},{w22:2},{b2:2})')
    print("MSE = "+str(mse))
    epochs-=1
