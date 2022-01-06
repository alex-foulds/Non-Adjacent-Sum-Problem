# Non-Adjacent-Sum-Problem

## Introduction
Repo for implementation of non-adjacenet sum problem.

Given an array of numbers, find the highest possible sum given that no selected numbers are adjacent.
E.g. [1,4,5] would return 6 rather than 9.


## Pseudo code and thoughts
### Initial Thoughts
- Conceptual use of subsets
- Could use recursion


Given arrayNum=[1,4,5]

Start from arrayNum[0] and expand subset until whole array is covered.

Maximum of subset (arrayNum[0]) is 1.

Maximum of subset (arrayNum[0] and arrayNum[1]) is 4.

Maximum of subset (arrayNum[0], arrayNum[1] and arrayNum[2]) is 6.

Store the sum values when arrayNum[i] *is* and *isn't* part of the subset

### Pseudo Code
Recursion is less time efficient.
```
#Maximum sum when array[i] is in subset
includeSum = 0

#Maximum sum when array[i] is not in subset
excludeSum = 0

loop over arrayNum(

    #Maximum sum of previous subset
    tempExcludeSum = max (includeSum, excludeSum)

    #Ignore the includeSum of the previous i value as it would be adjacent 
    includeSum = excludeSum + i

    #Set maximum sum should current i value not be included
    excludeSum = tempExcludeSum

)

print max (includeSum, excludeSum)
```