upper=0
lower=0
x=str(input("Enter a word with upper and lower case characters = "))
for i in x:
      if i.isupper():
            upper+=1
      elif i.islower():
            lower+=1
print("Lowercase = ",lower,"Uppercase = ",upper)
