import hashlib 
import time

h = hashlib.sha256()

hash_value = "9c906cf6ba6f4649f0041436e9ab710b2b963c14513ccdfccf805ff843c620da"

options = [
    "tom\n","hardy\n","isaac\n","maquire123\n","foxriver\n"
]

# h.update(b'foxriver\n')
# print(h.hexdigest())
# with open("wordlist.txt","wb") as f:
#     # for name in options:
#     f.writelines([option.encode() for option in options])
#     f.close()

with open("wordlist.txt","rb") as f:
    password = f.readlines()
    
    for line in password:
        h.update(line)
        print(h.hexdigest())

        if(h.hexdigest() == hash_value):
            print(f"MATCH FOUND...{line.decode()}..")
        
        else:
            print("No match found!...trying next option.")

            



