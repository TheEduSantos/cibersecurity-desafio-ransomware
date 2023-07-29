# cybersecurity-ransomware-challenge
A ransomware challenge from DIO

A code whose purpose is to encrypt and decrypt files using a fixed encryption key and then allows decrypting the file if the correct key is provided. It's worth noting that this program is not secure and should not be used for malicious purposes or to protect important data, as the encryption key is embedded in the code and easily accessible.

How to use:

# encrypter.py:

1 - Requests the user to input the name of the file they want to encrypt.

2 - Opens the file in binary read mode ("rb") and reads its entire content, storing it in file_data.

3 - Closes the original file and removes it from the system.

4 - Defines an encryption key called key. In this case, the key is a sequence of bytes represented by "0123456789abcdef".

5 - Creates an Advanced Encryption Standard (AES) object using Counter (CTR) mode from the pyaes library.

6 - Encrypts the content of the file using the defined key, resulting in crypto_data.

7 - Creates a new file with the extension ".ransomwaretroll" added to the original file's name and saves the encrypted content in it.


# decrypter.py:

1 - Requests the user to input the name of the encrypted file they want to decrypt (the encrypted file should have the ".ransomwaretroll" extension).

2 - Opens the encrypted file in binary read mode ("rb") and reads its entire content, storing it in file_data.

3 - Closes the encrypted file and removes it from the system.

4 - Defines the same encryption key used in the encryption step in key.

5 - Creates an AES object in Counter (CTR) mode from the pyaes library.

6 - Decrypts the content of the file using the defined key, resulting in decrypt_data.

7 - Removes the ".ransomwaretroll" extension from the encrypted file's name to obtain the original name.

8 - Creates a new file with the original name and saves the decrypted content in it.


# cibersecurity-desafio-ransomware
Resolução de um desafio de ransomware da DIO

Um código com a função de criptografar e descriptografar arquivos com uma chave de criptografia fixa e depois permite descriptografar o arquivo se a chave correta for fornecida. Vale ressaltar que esse programa não é seguro e não deve ser usado para fins maliciosos, ou para proteger dados importantes, pois a chave de criptografia está embutida no código e é facilmente acessível.

Modo de usar:

# encrypter.py:

1 - Solicita ao usuário o nome do arquivo que deseja criptografar.

2 - Abre o arquivo em modo leitura binária ("rb") e lê todo o seu conteúdo, armazenando-o em file_data.

3 - Fecha o arquivo original e remove-o do sistema.

4 - Define uma chave de criptografia chamada key. Neste caso, a chave é uma sequência de bytes representada por "0123456789abcdef".

5 - Cria um objeto AES (Advanced Encryption Standard) usando o modo de operação CTR (Counter) a partir da biblioteca pyaes.

6 - Criptografa o conteúdo do arquivo utilizando a chave definida, resultando em crypto_data.

7 - Cria um novo arquivo com a extensão ".ransomwaretroll" adicionada ao nome do arquivo original e salva nele o conteúdo criptografado.


# decrypter.py:

1 - Solicita ao usuário o nome do arquivo criptografado que deseja descriptografar (o nome do arquivo criptografado deve ter a extensão ".ransomwaretroll").

2 - Abre o arquivo criptografado em modo leitura binária ("rb") e lê todo o seu conteúdo, armazenando-o em file_data.

3 - Fecha o arquivo criptografado e remove-o do sistema.

4 - Define a mesma chave de criptografia usada na etapa de criptografia em key.

5 - Cria um objeto AES no modo de operação CTR a partir da biblioteca pyaes.

6 - Descriptografa o conteúdo do arquivo utilizando a chave definida, resultando em decrypt_data.

7 - Remove a extensão ".ransomwaretroll" do nome do arquivo criptografado para obter o nome original.

8 - Cria um novo arquivo com o nome original e salva nele o conteúdo descriptografado.

