i=0
sum=0
print("Enter 5 non-negative integers")
for i in range(5):
      value=int(input("Enter value: "))
      if value<0:
            print("Invalid text")
            break
      sum+=value
      i+=1
if i==5:
      print("Average = ",round(sum/i,2))
