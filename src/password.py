import hashlib, uuid

def main(password: str):    
    # Con uuid creamos una identificación única, uuid4() crea un UUID aleatorio.
    # Convertir un UUID en una cadena hexadecimal de 32 caracteres
    salt = uuid.uuid4().hex
    print("Salt > ", salt)
    # encode (): convierte la cadena en bytes para que sea aceptable mediante la función hash.
    print((password + salt).encode("utf-8"))
    # hexdigest (): devuelve los datos codificados en formato hexadecimal.
    hashed = hashlib.md5((password + salt).encode("utf-8")).hexdigest()
    print("Password hash is > %s " % hashed)

if __name__ == '__main__':
    password: str = input("Password > ")
    main(password)


