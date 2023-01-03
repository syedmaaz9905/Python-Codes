table=list()
for i in range(3):
      print("Enter values for row",i,"of the table, separated by space: ",end='')
      values=input()
      lvalues=values.split()
      table.append(lvalues)
print(table)
