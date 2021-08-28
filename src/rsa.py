"""
Uso: RSA (Asimétrico)
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 28 Agosto 2021
"""

from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
import binascii
import ast

# pip install -r requirements.txt

def main():
	
	key = RSA.generate(3072)
	
	public_key  = key.publickey()
	print(f"Public key:  (n={hex(public_key.n)}, e={hex(public_key.e)})")
	pub_key = public_key.exportKey()
	print(pub_key.decode('ascii'))
	
	print(f"Private key: (n={hex(public_key.n)}, d={hex(key.d)})")
	private_key = key.exportKey()
	print(private_key.decode('ascii'))
	
	#encrypt
	message = input("Enter message > ")
	encryptor = PKCS1_OAEP.new(public_key)
	encrypted = encryptor.encrypt(message.encode())
	print("Encrypted: ", binascii.hexlify(encrypted))

	#decoded
	decryptor = PKCS1_OAEP.new(key)
	decrypted = decryptor.decrypt(ast.literal_eval(str(encrypted)))
	print("Decrypted: ",  decrypted.decode())


if __name__ == '__main__':
    main()