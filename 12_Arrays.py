import numpy as np
a=np.array([1,2,3,4])
print(a,type(a))

#Element wise operations
print(a*2)

#Multi-Dimensional arrray
b=np.array([[1,2,3],[3,4,5]])
print(b)

#Appending elements
new=np.append(b,[2,3])
print(new)

arr1=np.array([1,2,3,4])
for i in range(len(arr1)):
    print(arr1[i],end=" ")

arr2=np.array([1,2,3,4,5])
ab=np.insert(arr2,4,7)
print(ab)

# 3. Pop() Method
import array
 
# initializing array with array values
arr= array.array('i',[1, 2, 3, 1, 5])
 
# printing original array
print ("The new created array is : ",end="")
for i in range (0,5):
    print (arr[i],end=" ")
 
print("\r")
 
# using pop() to remove element at 2nd position
print ("The popped element is : ",end="")
print (arr.pop(2))
 
# printing array after popping
print ("The array after popping is : ",end="")
for i in range (len(arr)):
    print (arr[i],end=" ")



# 4. Remove() Method
import array
 
arr= array.array('i',[1, 2, 3, 1, 5])
 
# printing original array
print ("The new created array is : ",end="")
for i in range (0,5):
    print (arr[i],end=" ")
 
print("\r")
 
# using remove() to remove 1st occurrence of 1
arr.remove(1)
 
# printing array after removing
print ("The array after removing is : ",end="")
for i in range (len(arr)):
    print (arr[i],end=" ")



# 5. Index() Method
import array
  
# initializing array with array values
arr= array.array('i',[1, 2, 3, 1, 2, 5])
 
# printing original array
print ("The new created array is : ",end="")
for i in range (0,6):
    print (arr[i],end=" ")
 
print("\r")
 
# using index() to print index of 1st occurrence of 2
print ("The index of 1st occurrence of 2 is : ",end="")
print (arr.index(2))



# 6. Reverse() Method
import array
  
# initializing array with array values
arr= array.array('i',[1, 2, 3, 1, 2, 5])
 
# printing original array
print ("The new created array is : ",end="")
for i in range (0,6):
    print (arr[i],end=" ")
 
print("\r")
 
#using reverse() to reverse the array
arr.reverse()
 
# printing array after reversing
print ("The array after reversing is : ",end="")
for i in range(len(arr)):
    print (arr[i],end=" ")



    print("version",np.__version__)
