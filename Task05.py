#sonar counter
#a depth measurement of the nearby sea floor(increased or decreased
s=[299,399,599,199,146]
p=s[0]
increase=0
decrease=0
print(f"{p} no previous value")
for i in range(1,len(s)):
    if s[i]>p:
        print(f"{s[i]} increased")
        increase+=1
    elif s[i] == p:
        print(f"{s[i]} no change")
    else:
        print(f"{s[i]} decreased")
        decrease+=1
        p=s[i]
print(f"increased {increase} times")    
print(f"decreased {decrease} times")    
