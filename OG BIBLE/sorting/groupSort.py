def groupSort(arr):
    output = {}
    result = []
    # Write your code here
    for number in arr:
        if number not in output:
            output[number] = 1
        else:
            output[number] = output[number] + 1
            
    for key in output:
        result.append([key, output[key]])
    
    sorted_arr = descending(result)
    sorted_arr = sortByValue(sorted_arr)
    return sorted_arr


def descending(output):
    for i in range(len(output)):
        min_idx = i
        
        for keyj in range(i+1, len(output)):
            if output[min_idx][1] < output[keyj][1]:
                min_idx = keyj
                
        output[i], output[min_idx] = output[min_idx], output[i]
    return output

def sortByValue(output):
    for i in range(len(output)):
        min_idx = i
        
        for keyj in range(i+1, len(output)):
            if output[i][0] > output[keyj][0] and output[i][1] == output[keyj][1]:
                min_idx = keyj
                
        output[i], output[min_idx] = output[min_idx], output[i]     
    return output
   
arr = [7,12,3]
print(groupSort(arr))