import hashlib 

h = hashlib.sha256()
file = "./rufus-3.20.exe"

file_hash = open("hash.txt","r").read()


with open(file,"rb") as f:
    content = f.read()
    h.update(content)


if(file_hash == h.hexdigest()):
    print("Software Authentic")

else:
    print("Software Not Authentic!")