#Non-adjacent Sum problem

def main():
    inputArr = [1,3,14,3,9,18,52];
    print(largestSum(inputArr));

def largestSum(array):
    #Set initial empty subset values
    includeSum = 0;
    excludeSum = 0;

    for i in array:
        
        print("---")
        print("i:",i);
        #Maximum sum of previous subset
        tempExcludeSum = max(includeSum,excludeSum);
        
        #Maximum of current subset - cant include indexof(i-1)/adjacent value
        includeSum = excludeSum + i;
        #Maximum of current subset if i is not included
        excludeSum = tempExcludeSum;

        print("includeSum:",includeSum);
        print("excludeSum:",excludeSum);

    return max(includeSum,excludeSum);

main();