x=int(input("Enter the number of rows you wanna print: "))
y=int(input("Enter 0 or 1: "))
z=bool(y)
if z==True:
      for i in range(x+1):
            print(i*"*")
            i+=1
elif z==False:
      for j in range(x+1):
            print((x-j)*"*")
            j+=1
      
      
