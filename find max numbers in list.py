lst=[89,92,56,78,98]
big=lst[0]
for item in lst:
   if big < item :
      big = item
print("the max number in this list is: ",big)
