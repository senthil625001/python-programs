word = "internationalization"
abbr = "i12iz4n"

# Two pointers approach
i = 0
j = 0

while i< len(word) and j < len(abbr):
    if word[i] == abbr[j]:
        i+=1
        j+=1
        continue
        
    elif abbr[j].isalpha() or abbr[j] == '0':
        print (False)
    
        
    curr_number = 0 # to get the numbers from abbrevation
        
    while j < len(abbr) and abbr[j].isdigit():
        curr_number = curr_number *10 + int(abbr[j])
        j+=1
    
    i+=curr_number

print (i == len(word) and j == len(abbr))
