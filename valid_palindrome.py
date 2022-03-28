s = "A man, a plan, a canal: Panama"

left,right = 0, len(s)-1

while left < right:
    if not s[left].isalnum():
        left += 1
        continue
    
    if not s[right].isalnum():
        right -= 1
        continue
    
    if s[left].lower() != s[right].lower():
        print(False)
    
    left += 1
    right -= 1

print (True)

Time complexity: O(n)
Space Complexity: O(1)

# Shorter Version

new_str = ''.join(filter(str.isalnum,s))
new_str.lower()

new_str =''.join (char for char in s.lower() if s.isalnum())
