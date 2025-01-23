
def sliding_window(num_list, k):
    size = len(num_list)
    if k > size or k < 1:
        return []
    # list ketqua
    result =  []
    
    #solution 
    for i in range(size-k+1):
        result.append(max(num_list[i:i+k]))
    return result
    
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(sliding_window(num_list, k))