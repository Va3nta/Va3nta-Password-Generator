import random

print ("")
print ("")
print ("")

print (" █████   █████   █████████    ████████  ██████   █████ ███████████   █████████      ███████████    █████████    █████████   █████████ ")
print ("░░███   ░░███   ███░░░░░███  ███░░░░███░░██████ ░░███ ░█░░░███░░░█  ███░░░░░███    ░░███░░░░░███  ███░░░░░███  ███░░░░░███ ███░░░░░███")
print (" ░███    ░███  ░███    ░███ ░░░    ░███ ░███░███ ░███ ░   ░███  ░  ░███    ░███     ░███    ░███ ░███    ░███ ░███    ░░░ ░███    ░░░ ")
print (" ░███    ░███  ░███████████    ██████░  ░███░░███░███     ░███     ░███████████     ░██████████  ░███████████ ░░█████████ ░░█████████ ")
print (" ░░███   ███   ░███░░░░░███   ░░░░░░███ ░███ ░░██████     ░███     ░███░░░░░███     ░███░░░░░░   ░███░░░░░███  ░░░░░░░░███ ░░░░░░░░███")
print ("  ░░░█████░    ░███    ░███  ███   ░███ ░███  ░░█████     ░███     ░███    ░███     ░███         ░███    ░███  ███    ░███ ███    ░███")
print ("    ░░███      █████   █████░░████████  █████  ░░█████    █████    █████   █████    █████        █████   █████░░█████████ ░░█████████ ")
print ("     ░░░      ░░░░░   ░░░░░  ░░░░░░░░  ░░░░░    ░░░░░    ░░░░░    ░░░░░   ░░░░░    ░░░░░        ░░░░░   ░░░░░  ░░░░░░░░░   ░░░░░░░░░  ")
print ("--------------------------------------------------------------------------------------------------------------------------------------")

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz/*-+,!_='^%&()?"


passwordLenght = int(input("How long do you want your password to be? (Recommed Lenght is 16): "))

print ("")
print ("")
print ("")
print ("")


print ("Your password being generating <3")

print ("")
print ("")
print ("")

newPassword = []
for x in range(passwordLenght) : 

    newPassword.append(random.choice(characters))


finalPassword = ''.join(map(str, newPassword))

print ("Your new password is : " , finalPassword)

print ("")
print ("")
print ("")

print ("Thanks for choosing us ❤️")

print ("")
print ("")
print ("")


                                                                                                                  
                                                                                                                  
                                                                                                                                      
                                                                                                                                      
                                                                                                                                      