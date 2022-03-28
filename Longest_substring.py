# Longest Substring Without Repeating Characters

s= 'abcacbad'

ans = 0
sub = ''
for char in s:
    print( char)
    if char not in sub:
        sub += char
        ans = max(ans, len(sub))
    else:
        cut = sub.index(char)
        sub = sub[cut+1:] + char
    print ("sub is",sub)
    print ("answer is", ans)
    print ("cut is", cut)
print (ans)
