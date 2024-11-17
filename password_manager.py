"""
In your terminal to install cryptography package type:
1. pip install cryptography  or
2.pip3 install cryptography  or
3.python -m pip install cryptography  or
4.python3 -m pip install cryptography
one of them should work
"""
from cryptography.fernet import Fernet 
#This(fernet) is a module which allows you to encrypt
# a key is needed ,without is you can not go back  to orginal password
# I am going to combine this key with master password
# key+password+text to encrypt=random text
#random text +key+password=text to encrypt


"""def write_key():
    key=Fernet.generate_key()
    # wb = write in bytes
    with open("key.key","wb") as key_file:
        key_file.write(key)
write_key() """
def load_key():
    file=open("key.key","rb")
    key=file.read()
    file.close()
    return key
#master_pwd=input("What is the master password? ")
#key=load_key() + master_pwd.bytes
key=load_key() 
fer=Fernet(key)

def add():
    name=input("Account Name: ")
    pwd=input("Password: ")
    """
    file=open('password.txt','a')
    file.close()....both line has to be used
    """
    with open('password.txt','a') as f: #automatically close the file.No need to close it manually
        #f.write(name + "|" + pwd+"\n")
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode()+"\n")

def view():
     with open('password.txt','r') as f: #automatically close the file.No need to close it manually
        for line in f.readlines():
            #print(line.rstrip())#strip off the character(space)
            #print(line)
            data=line.rstrip()
            user_name,password=data.split("|")
            print("User Name:",user_name,"| Password:",fer.decrypt(password.encode()).decode())
while True:

    mode=input("Would you like to add a new password or view existing ones (view,add) or press Q to quit: ").lower()
    if mode=="q":
        break
    if mode=="view":
        view()
    elif mode=="add":
        add()
    else:
        print("Invalid mode.")
        continue