def gettime():
      import datetime
      return datetime.datetime.now()
while True:
      print('''Press:\n'1' For Harry\n'2' For Ronaldo\n'3' For Hammad''')
      x=int(input("Enter Here: "))
      if x==1:
            print('''Press:\n'1' For Locing Harry's Exercise\n'2' For Locking Harry's Diet\n'3' For Retreiving Harry's Exercise\n'4' For Retreiving Harry's Diet''')
            y=int(input("Enter Here: "))
            if y==1:
                  while True:
                        value=input("Enter your exercises here:\n ")
                        with open("Harry's-Exercise.txt","a") as f:
                              f.write(str([str(gettime())])+':'+value+'\n')
                        print("Successfully Written\nWant to write more?\nPress 'Y' for Yes and 'N' for No")
                        z=input("Enter Here: ")
                        if z=='y' or z=='Y':
                              continue
                        elif z=='n' or z=='N':
                              print("Okay")
                              break
                        else:
                              print("Wrong Input")
                              break
            elif y==2:
                  while True:
                        value=input("Enter your diet here:\n ")
                        with open("Harry's-Diet.txt","a") as f:
                              f.write(str([str(gettime())])+':'+value+'\n')
                        print("Successfully Written\nWant to write more?\nPress 'Y' for Yes and 'N' for NO")
                        z=input("Enter Here: ")
                        if z=='y' or z=='Y':
                              continue
                        elif z=='n' or z=='N':
                              print("Okay Bye")
                              break
                        else:
                              print("Wrong Input")
                              break
            elif y==3:
                  with open("Harry's-Exercise.txt","rt") as f:
                        content=f.read()
                        print(content)
            elif y==4:
                  with open("Harry's-Diet.txt","rt") as f:
                        content=f.read()
                        print(content)
      elif x==2:
            print('''Press:\n'1' For Locing Ronaldo's Exercise\n'2' For Locking Ronaldo's Diet\n'3' For Retreiving Ronaldo's Exercise\n'4' For Retreiving Ronaldo's Diet''')
            y=int(input("Enter Here: "))
            if y==1:
                  while True:
                        value=input("Enter your exercises here:\n ")
                        with open("Ronaldo's-Exercise.txt","a") as f:
                              f.write(str([str(gettime())])+':'+value+'\n')
                        print("Successfully Written\nWant to write more?\nPress 'Y' for Yes and 'N' for No")
                        z=input("Enter Here: ")
                        if z=='y' or z=='Y':
                              continue
                        elif z=='n' or z=='N':
                              print("Okay")
                              break
                        else:
                              print("Wrong Input")
                              break
            elif y==2:
                  while True:
                        value=input("Enter your diet here:\n ")
                        with open("Ronaldo's-Diet.txt","a") as f:
                              f.write(str([str(gettime())])+':'+value+'\n')
                        print("Successfully Written\nWant to write more?\nPress 'Y' for Yes and 'N' for NO")
                        z=input("Enter Here: ")
                        if z=='y' or z=='Y':
                              continue
                        elif z=='n' or z=='N':
                              print("Okay Bye")
                              break
                        else:
                              print("Wrong Input")
                              break
            elif y==3:
                  with open("Ronaldo's-Exercise.txt","rt") as f:
                        content=f.read()
                        print(content)
            elif y==4:
                  with open("Ronaldo's-Diet.txt","rt") as f:
                        content=f.read()
                        print(content)
      elif x==3:
            print('''Press:\n'1' For Locing Hammad's Exercise\n'2' For Locking Hammad's Diet\n'3' For Retreiving Hammad's Exercise\n'4' For Retreiving Hammad's Diet''')
            y=int(input("Enter Here: "))
            if y==1:
                  while True:
                        value=input("Enter your exercises here:\n ")
                        with open("Hammad's-Exercise.txt","a") as f:
                              f.write(str([str(gettime())])+':'+value+'\n')
                        print("Successfully Written\nWant to write more?\nPress 'Y' for Yes and 'N' for No")
                        z=input("Enter Here: ")
                        if z=='y' or z=='Y':
                              continue
                        elif z=='n' or z=='N':
                              print("Okay")
                              break
                        else:
                              print("Wrong Input")
                              break
            elif y==2:
                  while True:
                        value=input("Enter your diet here:\n ")
                        with open("Hammad's-Diet.txt","a") as f:
                              f.write(str([str(gettime())])+':'+value+'\n')
                        print("Successfully Written\nWant to write more?\nPress 'Y' for Yes and 'N' for NO")
                        z=input("Enter Here: ")
                        if z=='y' or z=='Y':
                              continue
                        elif z=='n' or z=='N':
                              print("Okay Bye")
                              break
                        else:
                              print("Wrong Input")
                              break
            elif y==3:
                  with open("Hammad's-Exercise.txt","rt") as f:
                        content=f.read()
                        print(content)
            elif y==4:
                  with open("Hammad's-Diet.txt","rt") as f:
                        content=f.read()
                        print(content)
            
            
            
                  
                  
      
