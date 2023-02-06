# wap to print sum and count of even odd numbers

nums = []
totEven = 0
totOdd = 0
e_sum=0
o_sum=0

print("Enter 10 Numbers: ")
for i in range(10):
  nums.insert(i, int(input()))

for i in range(10):
  if nums[i]%2==0:
     totEven = totEven+1
     e_sum+=i
  else:
    totOdd = totOdd+1
    o_sum+=i
    
print("\nEven Number: ",totEven)
print("Odd Number: ",totOdd)
print("sum of even number",e_sum)
print("sum of odd number",o_sum)


