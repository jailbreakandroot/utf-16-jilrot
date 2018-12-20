import base64
import os

os.system("clear")
os.system("clear")

print ("\033[1;31m@@@@ @@@@ @@@   @@@@@ @@@   @@@   @@@@@\033[1;m")
print ("\033[1;31m@  @ @  @   @   @   @   @     @   @   @\033[1;m")
print ("\033[1;31m@@@@ @@@@ @@@@@ @@@@@ @@@@@ @@@@@ @@@@@\033[1;m")

print ("UTF-16,,,")
print ("     ")
print ("\033[1;31mcode by mehdi652\033[1;m")
print ("    ")
print ("       ")

print ("\033[1;32m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[1;m")
print ("\033[1;32msite: https://jailbreakandroot.tk\033[1;m")
print ("\033[1;32mchannel: https://t.me/jailbreakandroot\033[1;m")
print ("\033[1;32mgithub: https://github.com/jailbreakandroot\033[1;m")
print ("\033[1;32m<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\033[1;m")


print ("      ")
print ("      ")
print ("      ")
print ("      ")








def main():
    inp = input('Enter the text>>>  ')
    encoded = inp.encode('utf-16') 
    encoded1 = base64.b16encode(encoded)
    print(encoded1)
    print(base64.b16decode(encoded1).decode('utf-16'))

if __name__ == '__main__':
    main()

