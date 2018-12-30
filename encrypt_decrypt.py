import pyAesCrypt
import sys
from os.path import getsize


if len(sys.argv) != 4:
    print("Usage: python3 encrypt_decrypt.py e/d <filename> <password file>")
    exit(1)

cmd = sys.argv[1]
fname = sys.argv[2]
password = open(sys.argv[3]).readline()
buffer = getsize(fname)*1024

if cmd == 'e':
    pyAesCrypt.encryptFile(fname,fname+".e",password,buffer)
    print("File encrypted successfully.")
elif cmd == 'd':
    pyAesCrypt.decryptFile(fname,fname[:len(fname)-2],password,buffer)
    print("File decrypted successfully.")
else:
    print("Invalid command.")
