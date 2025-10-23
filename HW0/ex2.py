def ispalindrome(arr):
    # Base case 1:
    # An empty array is always palindrome -> return True
    if (len(arr)  == 0): 
        return True

    # Base case 2:
    # An array of a single element is always palindrome -> return True
    if (len(arr) == 1):
        return True
    
    # Base case 3:
    # If the first and last elements of arr are not identical ,
    # the array is not palindrome -> return False
    if(arr[0] != arr[-1]):
        return False
    
    # If we get here it 's because the first and last
    # elements are identical , therefore :
    # Recursive call:
    # Call ispalindrome () dropping the first and last
    # elements of arr
    return ispalindrome(arr[1:-1])

# # Test
# print(ispalindrome([]))
# print(ispalindrome([1]))
# print(ispalindrome([1,2,3,2,1]))
# print(ispalindrome([1,2,3,3,2,1]))
# print(ispalindrome([1,3,2,1]))