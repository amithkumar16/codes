lst=[]
d={}
for _ in range(int(input())):
        name = input()
        score = float(input())
        d[name]=score
a=min(d.values())
dic={name:score for name,score in d.items() if score!=a}
b=min(dic.values())
for name,score in dic.items():
        if score==b:
            lst.append(name)
sorted_list=sorted(lst)
for i in sorted_list:
       print(i)