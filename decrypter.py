import pyaes
import os

## abrir arquivo que será descriptografado
nome_do_arquivo = "teste.txt.ransomwaretroll"
arquivo = open(nome_do_arquivo, "rb")
arquivo_data = arquivo.read()
arquivo.close()

## chave para descriptografar arquivo/
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## remover o arquivo criptografado
os.remove(file_name)

## criar novo arquivo descriptografado
arquivo_novo = "teste.txt"
arquivo_novo = open(f'{arquivo_novo}', "wb")
arquivo_novo.write(decrypt_data)
arquivo_novo.close()
