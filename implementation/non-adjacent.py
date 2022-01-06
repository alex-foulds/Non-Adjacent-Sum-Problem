#Non-adjacent Sum problem

def main():
    inputArr = [1,3,14,3,9,18,52];
    print(largestSum(inputArr));

def largestSum(array):
    #set initial empty subset values
    includeSum = 0;
    excludeSum = 0;

    for i in array:
        tempExcludeSum = max(includeSum,excludeSum);

        includeSum = excludeSum + i;
        excludeSum = tempExcludeSum;

    return max(includeSum,excludeSum);

main();