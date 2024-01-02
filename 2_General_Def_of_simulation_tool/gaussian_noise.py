import random

def awgn(idata,qdata,attn):
    irand = []
    qrand = []
    for i in range(0,len(idata)):
        ni = random.random()
        irand.append(ni * attn)
    
    for i in range(0,len(qdata)):
        nq = random.random()
        qrand.append(nq * attn)

    iout = irand + idata
    print(iout)
    qout = qrand * attn + qdata
    print(qout)
    print(qrand)

idata = [1.0, 1.0, 0.0, 0.0, 1.0]
qdata = [0.0, 1.0, 0.0, 1.0, 0.0]
attn = 0.1
awgn(idata,qdata,attn)



