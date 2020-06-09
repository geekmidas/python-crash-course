def sort(original):
    numbers = list(original)
    size = len(numbers)
    for i in range(size - 1):
        smallest = i
        for j in range(i+1, size): # size - i - 1
            if numbers[j] < numbers[smallest]:
                smallest = j
        # swap
        temp = numbers[smallest]
        numbers[smallest] = numbers[i]
        numbers[i] = temp

    return numbers

marks = [9,8,7,6,5,4,3,2,1]
marks = sort(marks)
print(marks)