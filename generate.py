from hashlib import sha1, sha224, sha256
from tqdm import tqdm
import getpass
import qrcode
import time
import sys

SIGNATURE = """


  ______  _____  _     _  _____  _     _ _______ __   __
 |_____/ |     | |____/  |     | |____/  |______   \_/  
 |    \_ |_____| |    \_ |_____| |    \_ |______    |   
                        GENERATOR
                                              by pluja.
 
 Donate ₿:                                                 
"""

def gethash(s, encoding='utf-8'):
    if algo == "3" or algo == "3 " or algo == " 3" or algo == " 3 ":
        return sha256(s.encode(encoding)).hexdigest()
    if algo == "2" or algo == "2 " or algo == " 2" or algo == " 2 ":
        return sha224(s.encode(encoding)).hexdigest()  
    return sha1(s.encode(encoding)).hexdigest()


print(SIGNATURE)
print("❗ ATTENTION ❗ ")
print("Always read the code, disconnect your internet and preferably use a fresh OS \nwhich has never been connected to the internet before.")
print("\nℹ Rokokey uses a hashing algorithm to encrypt your keys with a secret. This secret will determine the security of your keys. Please use a secure secret.")

print("\n\nℹ Please, now choose a hashing algorithm ")
print("[1]- SHA1 ⚏ Lightweight and moderatelly secure")
print("2- SHA224 ⚎ Very strong but very big QR")
print("3- SHA256 ⚌ Strongest but largest QR")
algo = input("\n➜ Hashing algorithm [Default SHA1]: ")

sk = "a"
tmp_sk = "b"
while sk != tmp_sk:
    print("\n\n➜ Type your secret...")
    sk = getpass.getpass()

    print("\n➜ Repeat your secret...")
    tmp_sk = getpass.getpass()

    if sk != tmp_sk:
        print("\n❌ ERROR: Secrets don't match!")

n = input("\n\n➜ How many words you want to backup? ")
try:
    n=int(n)
    intn = True
except:
    intn = False

while not intn:
    try:
        n=int(n)
        intn = True
    except:
        print("❌ ERROR: Please type a valid number!")
        n = input("\n➜ How many words you want to backup? ")
        intn = False

print("ℹ Will backup {n} words...\n\n".format(n=n))
print("ℹ Please type your words one by one in order...\n")
hashlist = []
tn = 1
while tn < n+1:
    hwd = gethash(input("➜ Input the {} word: ".format(tn))+sk, encoding='utf-8')
    hashlist.append(hwd)
    tn = tn+1

print("\nℹ {} total words.\n".format(len(hashlist)))
tn = 1
correct = True
while tn < n+1:
    th = gethash(input("➜ Verify the {} word: ".format(tn))+sk, encoding='utf-8')
    correct = (th == hashlist[tn-1])
    if not correct:
        print("\n❌ ERROR: Word {} didn't match!".format(tn))
        print("\n❗ Please repeat the process.")
        sys.exit()
    else:
        tn = tn+1

print("ℹ All words ok.")
filename = "backup.png"
img = qrcode.make(",".join(hashlist))
img.save(filename)
text_file = open("backup.csv", "w")
text_file.write(",".join(hashlist))
text_file.close()