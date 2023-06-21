import rsa 

public_key,private_key = rsa.newkeys(2048)

class RsaEncryptor:
    def __init__(self,**kwargs):
        
        if (self.save_keys()):
            pass 

        else:
            self.create_new_keys()

    def create_new_keys(self):
        open("public.pem","wb").write(public_key.save_pkcs1("PEM"))
        open("private.pem","wb").write(private_key.save_pkcs1("PEM"))   
    
    def save_keys(self):
        
        try:
            self.saved_public_key = rsa.PublicKey.load_pkcs1(open("public.pem","rb").read())
            self.saved_private_key = rsa.PrivateKey.load_pkcs1(open("private.pem","rb").read())

            if (self.saved_public_key)  and  (self.saved_private_key):
                return True 
            
            else:
                return False
          
        except Exception as e:
            print(e)
            print("Creating new keys")
            self.create_new_keys()
     
    def encrypt_message(self,msg):
        try:
            encrypted_msg = rsa.encrypt(msg.encode(),self.saved_public_key)
            return encrypted_msg

        except ValueError as e:
            print(e)
            
    def decrypt_message(self,msg):
        try:
            decrypted_msg = rsa.decrypt(msg,self.saved_private_key)
            return decrypted_msg

        except ValueError as e:
            print(e)
            
            
