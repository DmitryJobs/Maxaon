f=open('Perepis.txt','r+')
count=0
Monke=[]
with open('Perepis.txt') as f:


    for i in range(31):
        a=f.readline()
        res=a.split()
        date=res[3]
        fam=res[0]
        c=date[-4:]
        c1=int(c)

        if c1>1978:
            count+=1
            Monke.append(fam)

    print('Количество:',count)
    print('Фамилии:',Monke)