def solution(numbers):
    answer = ''
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])

    numbers.sort(key = lambda x: x* 3, reverse=True)
    answer = str(int("".join(numbers)))
    
    return answer