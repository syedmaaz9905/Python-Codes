class String(str):
    def word_count(self):
        x=input("Enter Word ")
        if "a"<=x<="z" or "A"<=x<="Z" :
            print(len(x))
        else:
            print("invalid input")
a=String()
a.word_count()
    
