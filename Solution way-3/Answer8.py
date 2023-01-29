# Question 8

nums1 = [1,2,2,1]
nums2 = [2,2]

# we can take input from urear also


intersection = []

for number in nums1:
    if number in nums2:
        intersection.append(number)



print("nums1 = ", nums1,", nums2 = ", nums2)
print("intersection = ", list(intersection))




#another way using set

'''
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
intersection = []
for num in nums1:

  if num in nums2:

    intersection.append(num)
intersection = list(set(intersection))

print("nums1 = ", nums1,", nums2 = ", nums2)
print(f"Output: {intersection}")

'''