import random
print("WELCOME TO PASSWORD GENERATOR")

passcodes='qwertyuioplkjhgfdsazxcvbnmm@#$%^&*()_+{}":>?<'
numofpass=int(input("ENTER NO OF PASSWORDS YOU NEED :"))
lenofpass=int(input("ENTER LENGTH OF PASSWORD :"))
print("HERE IS YOUR PASSWORD ! / THANK YOU" )
for i in range(numofpass):
    word=""
    for j in range(lenofpass):
        word=word + random.choice(passcodes)
    print(word)
