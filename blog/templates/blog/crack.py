import hashlib
pass_hash = input("Enter md5 hash: ")
wordlist = input("Enter filename: ")

try:
    pass_file = open (wordlist, "r")
except:
    print("No file founs")
    quit()
for word in pass_file:
    enc_wrd = word.encode("utf-8")
    digest = hashlib.md5(enc_wrd.strip()).hexdigest()

    if digest ==pass_hash:
        print("the password is : ")

