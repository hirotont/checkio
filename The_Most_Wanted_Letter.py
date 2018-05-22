from collections import Counter
def checkio(text: str) -> str:
    
    str = text.lower()
    c = Counter(str)
    
    removes = []
    #アルファベット以外削除
    for num, cnt in c.most_common():
        if num.isalpha() == False :
            del c[num]

    for num, cnt in c.most_common():
        if cnt == c.most_common()[0][1]:
            removes.append(num)
    #最大頻度のlistのみremoves
    
    num2 = c.most_common()[0][0]
    for num in removes:
        if(num < num2):
            num2 = num
    
    return num2
