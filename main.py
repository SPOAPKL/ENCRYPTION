import os
texto = input("Texto: ").encode()
llave = list(os.urandom(len(texto)))
print(f"Llave: {''.join(format(k, '08b') for k in llave)}")
encriptado = bytes([b ^ k for b, k in zip(texto, llave)])
print(f"Encriptado: {''.join(format(e, '08b') for e in encriptado)}")
desencriptado = bytes([b ^ k for b, k in zip(encriptado, llave)])
print(f"Desencriptado: {desencriptado.decode()}")