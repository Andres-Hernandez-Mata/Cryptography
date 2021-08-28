"""
Uso: Vigenere (Simétrico)
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 28 Agosto 2021
"""

def main():
  message = input("Enter message > ")
  keyword = input("Enter keyword > ")
  key = generate_key(message, keyword) 
  encrypt_text = encryption(message, key) 
  print("Encrypted > ", encrypt_text) 
  print("Decrypted > ", decryption(encrypt_text, key)) 

def generate_key(message, key): 
  key = list(key) 
  if len(message) == len(key): 
    return(key) 
  else: 
    for i in range(len(message) - len(key)): 
      key.append(key[i % len(key)]) 
  return("".join(key)) 
  
def encryption(message, key): 
  encrypt_text = [] 
  for i in range(len(message)): 
    x = (ord(message[i]) + ord(key[i])) % 26
    x += ord('A') 
    encrypt_text.append(chr(x)) 
  return("".join(encrypt_text)) 

def decryption(encrypt_text, key): 
  orig_text = [] 
  for i in range(len(encrypt_text)): 
    x = (ord(encrypt_text[i]) - ord(key[i]) + 26) % 26
    x += ord('A') 
    orig_text.append(chr(x)) 
  return("".join(orig_text)) 


if __name__ == "__main__": 
  main()


