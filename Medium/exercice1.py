def findThreeNumbersWithSumZero(input):
    result = []
    for i in range(len(input)):
        for j in range(i + 1, len(input)):
            for k in range(j + 1, len(input)):
                if input[i] + input[j] + input[k] == 0:
                    triplet = sorted([input[i], input[j], input[k]])
                    if triplet not in result:
                        result.append(triplet)
    return result

input = [-1,0,1,2,-1,-4]

print(findThreeNumbersWithSumZero(input))
