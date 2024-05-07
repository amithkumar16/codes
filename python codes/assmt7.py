str='BANANANAAAS'
vowels='AEIOU'
cnt1=0
cnt2=0
for i in range(len(str)):
    if str[i] not in vowels:
        cnt1+=len(str)-i
    else:
        cnt2+=len(str)-i
if cnt1>cnt2:
    print("stuart",cnt1)
elif cnt2>cnt1:
    print("kelvin",cnt2)
else:
    print("Draw")
