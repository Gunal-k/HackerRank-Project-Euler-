def name_scores(actual,find):
    sorted_names = sorted(actual)
    result = []
    for val in find:
        if val not in sorted_names:
            result.append(0)
            continue
        res = sum((ord(char)-ord('A')+1) for char in val)
        res *= (sorted_names.index(val)+1)
        result.append(res)
    return result
    
if __name__ == "__main__":
    arr = []
    fnd = []
    for _ in range(int(input())):
        arr.append(input())
        
    for _ in range(int(input())):
        fnd.append(input())
    result = name_scores(arr,fnd)
    print("\n".join(map(str,result)))