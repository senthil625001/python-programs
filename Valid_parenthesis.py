def valid_parenthesis (str):
  stack = []
  elements = {')': '(', ']' : '[', '}', '{'}
  
  for item in string:
    if item in elements:
      # removing top element from the stack
      top_element = stack.pop() if stack else '#'
      
      if elements[item] != top_element:
        return False
    else:
      stack.append(item)
      
  return not stack      
 
 string = "([)]{}})"
