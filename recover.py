from hashlib import sha1, sha224, sha256
from tqdm import tqdm
import getpass
import qrcode
import time
import sys
import csv

def gethash(s, encoding='utf-8', algo=""):
    if algo == "3" or algo == "3 " or algo == " 3" or algo == " 3 ":
        return sha256(s.encode(encoding)).hexdigest()
    if algo == "2" or algo == "2 " or algo == " 2" or algo == " 2 ":
        return sha224(s.encode(encoding)).hexdigest()  
    return sha1(s.encode(encoding)).hexdigest()

SIGNATURE = """


  ______  _____  _     _  _____  _     _ _______ __   __ _______
 |_____/ |     | |____/  |     | |____/  |______   \_/   |______
 |    \_ |_____| |    \_ |_____| |    \_ |______    |    ______|
                         RECOVER
                                                        by pluja.
 
 Donate ₿: bc1q5y3g907ju0pt40me7dr9fy5uhfhfgfv9k3kh3z                                                
"""
print(SIGNATURE)
print("❗ ATTENTION ❗ ")
print("Always read the code, disconnect your internet and preferably use a fresh OS \nwhich has never been connected to the internet before.")
print("\nℹ Welcome to the recovery tool for ROKOKEY backups. Please follow the steps.")

sk = "a"
tmp_sk = "b"
while sk != tmp_sk:
    print("\n\n➜ Type your secret...")
    sk = gethash(getpass.getpass(), "utf-8", "3")

    print("\n➜ Repeat your secret...")
    tmp_sk = gethash(getpass.getpass(), "utf-8", "3")

    if sk != tmp_sk:
        print("\n❌ ERROR: Secrets don't match!")

print("\n\nℹ Please, now choose the hashing algorithm you chose to build your backup")
print("[1]- SHA1 ⚏")
print("2- SHA224 ⚎")
print("3- SHA256 ⚌")
algo = input("\n➜ Hashing algorithm [Default SHA1]: ")

print("\nℹ Now we will take the file 'backup.txt' and give you your keys. Please, make sure your backup.txt file is in place.")

with open('backup.csv', newline='') as f:
    reader = csv.reader(f)
    hashlist = list(reader)[0]

wc = 1
for hsh in hashlist:
    with open("wordlist.txt") as f:
        found = False
        bipnum = 1
        for line in f:
            c_hsh = gethash(line.rstrip()+sk, encoding='utf-8', algo=algo)
            if (c_hsh == hsh) and not found:
                print("{n}. {bn} | {w}".format(n=wc, w=line.rstrip(), bn=bipnum))
                found = True
            bipnum = bipnum+1
        wc = wc+1