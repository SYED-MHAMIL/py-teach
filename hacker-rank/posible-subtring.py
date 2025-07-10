str= 'BANANA'
vowels ="AEIOU"
kevin_score = 0
suart_score = 0
for i in range(len(str)) :
    if str[i] in vowels:
       kevin_score+=len(str)-i        
    else:
       suart_score+=len(str)-i     
if kevin_score>suart_score:
   print(f'kevin {kevin_score}')
else:
    print(f'suart {suart_score}')

    
    




# =====================      SECOND SOLUTION     ===============================
string= 'BANANA'
vowels ="AEIOU"
kevin_score = 0
stuart_score = 0

n = len(string)
for i in range(n):
    for j in range(i+1,n+1):
        str =string[i:j]
        if str[0] in vowels:
           kevin_score+=1
        else:
            suart_score+=1

if kevin_score>suart_score:
    print("Kevin", kevin_score)
elif kevin_score<suart_score:
    print(f'Stuart {stuart_score}')
else:
    print(f'Stuart {stuart_score}')
    

    

    