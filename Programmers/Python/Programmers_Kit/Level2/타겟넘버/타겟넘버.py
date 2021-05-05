def dfs(numbers,result,i,target):
    answer = 0
    if i == len(numbers):
        if target == result:
            return 1
        else:
            return 0
    answer += dfs(numbers, result + numbers[i], i + 1, target)
    answer += dfs(numbers, result - numbers[i], i + 1, target)
    
    return answer
def solution(numbers, target):
    answer = dfs(numbers,0,0,target)
    return answer