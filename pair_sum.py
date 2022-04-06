arr = [1,1,1,1]
n = len(arr)
sum = 2

unordered_map = {}
count = 0
for i in range(n):
    result = sum - arr[i]
    if result in unordered_map:
        count += unordered_map[result]
        
    if arr[i] in unordered_map:
        unordered_map[arr[i]] += 1
        
    else:
        unordered_map[arr[i]] = 1
print(count)
print(unordered_map) #{1: 4}
