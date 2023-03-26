# hello.py


k= [ (1, {'x1':'z1', 'x2':'z2', 'x3':'z3'}), 
     (2, {'x1':'z21', 'x2':'z22', 'x3':'z23'}),
     (3, {'x1':'z31', 'x2':'z32', 'x3':'z33'}),
     (4, {'x1':'z41', 'x2':'z42', 'x3':'z43'}),
]
print(k)
input()
#rt = []
rt1 = []
rt2 = []
rt3 = []
tr4 = {'x1': [], 'x2': [], 'x3': []}

input()
for x in k:   #переход по (1, {'x1':'z1', 'x2':'z2', 'x3':'z3'})
    for g,h in x[1].items():
        if g =='x1':
            rt1.append(h)  
        if g =='x2':
            rt2.append(h)
        if g =='x3':
            rt3.append(h)         
    for z in x[1]:         #переход по 'x1', 'x2', 'x3'
        if z == 'x1':
            tr4[z] = rt1 
        if z == 'x2':
            tr4[z] = rt2 
        if z == 'x3':
            tr4[z] = rt3    

print ('конец ',tr4)

#изменения 



