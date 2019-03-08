ch = input("Please Enter the input = ")


if (ch >= 'A' and ch <= 'Z'): 
    print("The given input is in upper case and", ch, "is an Alphabet")
elif(ch >= 'a' and ch <= 'z'):
    print("The given input is in  lower case and" , ch , "is a alphabet")
elif(ch >= '0' and ch <= '9'):
    print("The given input ", ch, "is a Digit")
