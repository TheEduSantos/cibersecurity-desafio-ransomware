import os
import pyaes

## abrir o arquivo criptografado

file_name = input("Digite o nome do arquivo: ")
file_name += ".ransomwaretroll"
file = open(file_name, 'rb')
file_data = file.read()
file.close()


## chave de descriptografia

key = b'0123456789abcdef'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

##remover o arquivo criptografado
os.remove(file_name)

## criar um novo arquivo descriptografado

new_file_name = file_name[:-len(".ransomwaretroll")]  # Removendo a extensão para obter o nome original
new_file = open(new_file_name, 'wb')
new_file.write(decrypt_data)
new_file.close()
