x= []
data = {}
aval = []
bol = True
out = 0
pout = {}
for i in range(10):
    x.append(int(input()))

for j in x :
    for h in range(2,j):
        for z in range(2,h):        
            if h % z == 0:
                bol = False
        if bol :
            aval.append(h)
        bol = True
    aval_s = set(aval)

    for k in aval_s :
        if j % k == 0 :
            data.setdefault(j,0)
            data[j]+=1

for i in data :
    if (data[i] > out) :
        out = data[i]
        i_save = i
    elif data[i] == out :
        if i > i_save :
            out = data[i]
            i_save = i
print (i_save , out)
        
        