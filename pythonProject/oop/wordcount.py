count={}
f1=open('wrdcnt','r')
for n in f1:
    data=n.split(' ')
    for word in data:
        if word not in count:
            count.update({word:1})
        else:
            val=int(count[word])
            val+=1
            count.update({word:val})
print(count)
