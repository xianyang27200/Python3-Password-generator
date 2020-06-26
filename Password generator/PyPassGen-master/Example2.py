import random
count = 0 
password = []
#create a list of character(lower,UPPER,numbers,symbols)
lst_character = list("QWERTYUIOPASDFGHJKLZXCVBNM\
                      qwertyuiopasdfghjklzxcvbnm\
                      0123456789!@#$%^&*(){}[]?|")

#get the length of the password                      
Pswd_length = input("How long do you want you password: ")
length = int(Pswd_length)

#track the random choice of character
while count < length:
    rand = random.choice(lst_character)
    password.append(rand)
    count += 1


#convert the ACSII to character
word = "".join([c for c in password])


#print the result
print("*"*len(word))
print(word)
print("*"*len(word))

