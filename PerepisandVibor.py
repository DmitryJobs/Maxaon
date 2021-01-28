f=open('Perepis.txt','r+')
count=0
Monke=[]
Vibor=int(input())
with open('Perepis.txt') as f:


    for i in range(31):
        a=f.readline()
        res=a.split()
        date=res[3]
        fam=res[0]
        im=res[1]
        ot=res[2]
        c=date[-4:]
        c1=int(c)

        if c1>Vibor:
            count+=1
            Monke.append(fam)
            Monke.append(im)
            Monke.append(ot)

    print('Количество:',count)
    print('ФИО:',Monke)

