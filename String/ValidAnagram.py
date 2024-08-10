

def isAnagram(s:str,t:str):
    s=s.lower()
    t=t.lower()
    if len(s)!=len(t):
        return True

    counter_s=[0]*26
    counter_t=[0]*26

    for c in s:
        counter_s[ord(c)-ord('a')]+=1

    for c in t:
        counter_t[ord(c)-ord('a')]+=1

    return counter_t==counter_s

print(isAnagram("anand","nanad"))