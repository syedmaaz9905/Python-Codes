
# Q 2(C)

# a = int(input("Enter the number: "))
# num = bin(a)
# binary = "000"+str(num)[2:]
# print(binary)
# final_number = ""
# for i in range(len(binary)):
#     if i%2==0 and i!=len(binary)-1:
#         final_number+=binary[i+1]
#     elif i==len(binary)-1 and i%2==0:
#         final_number+="0"
#     elif i==len(binary)-1 and i%2!=0:
#         final_number+=binary[i]
    
#     else:
#         final_number+="0"
# print(final_number)


# Q 8

# for i in range(1, 501):
    
#     if i%3==0 and i%5==0 and i%7==0:
#         print("FizzBuzzBazz")
#     elif i%3==0 and i%5==0:
#         print("FizzBuzz")
#     elif i%3==0 and i%7 == 0:
#         print("FizzBazz")
#     elif i%5==0 and i%7==0:
#         print("BuzzBazz")
#     elif i%3==0:
#         print("Fizz")
#     elif i%5==0:
#         print("buzz")
#     elif i%7==0:
#         print("Bazz")
#     else:
#         print(i)
        

# Q 10

# def mult(a, b):
#     if a == 0 or b==0:
#         return 0
    
#     else:
#         return a+mult(a, b-1)

# print(mult(5, 5))
        
        
# Q11

# def fact(num):
#     if num == 0 or num == 1:
#         print("Factorial is:", 1)
#     else:
#         number = 1
#         for i in range(2, num+1):
#             number*=i
#         print("Factorial is:", number)


# Q7


# def count_alpha(string: str):
#     a = list(set(string))
#     counter_dict = {}
#     for i in a:
#         counter_dict[i] = string.count(i)
#     return counter_dict

# def permutation(a, b):
    
#     string1 = count_alpha(a)
#     string2 = count_alpha(b)
#     if string1 == string2:
#         return "It is permutation of another"
#     else:
#         return "it is not"

# print(permutation("abcd", "dbca"))