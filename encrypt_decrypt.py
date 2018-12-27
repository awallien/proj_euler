import pyAesCrypt
from os.path import getsize

cmd = input("encrypt/decrypt? (e or d): ")
fname = input("File: ")
password = input("Password: ")
buffer = getsize(fname)*1024

if cmd == 'e':
    pyAesCrypt.encryptFile(fname,fname+".e",password,buffer)
elif cmd == 'd':
    pyAesCrypt.decryptFile(fname,fname[:len(fname)-2],password,buffer)
else:
    print("Invalid command.")
