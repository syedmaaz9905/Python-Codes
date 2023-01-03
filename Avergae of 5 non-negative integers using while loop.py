counter=0
sum=0
print("Enter 5 non-negative integers")
while counter<5:
      value=int(input("Enter value: "))
      if value<0:
            print("Invalid text")
            break
      sum+=value
      counter+=1
if counter == 5:
      print("Average = ", round(sum/counter,2))
