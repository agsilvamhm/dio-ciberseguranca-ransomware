# Importa os módulos necessários
import os         # Módulo para manipulação de arquivos e sistema operacional
import pyaes      # Biblioteca para criptografia/descriptografia AES

# Etapa 1: Abrir o arquivo criptografado
file_name = "teste.txt.ransomwaretroll"  # Nome do arquivo criptografado
file = open(file_name, "rb")            # Abre o arquivo no modo de leitura binária
file_data = file.read()                 # Lê o conteúdo do arquivo criptografado
file.close()                            # Fecha o arquivo após a leitura

# Etapa 2: Configurar a chave de descriptografia
key = b"testeransomwares"               # Define a chave AES usada para descriptografia
aes = pyaes.AESModeOfOperationCTR(key)  # Configura o AES no modo CTR com a chave
decrypt_data = aes.decrypt(file_data)   # Descriptografa os dados do arquivo

# Etapa 3: Remover o arquivo criptografado
os.remove(file_name)                    # Exclui o arquivo original criptografado

# Etapa 4: Criar um novo arquivo descriptografado
new_file = "teste.txt"                  # Nome do novo arquivo descriptografado
new_file = open(f'{new_file}', "wb")    # Abre (ou cria) o arquivo no modo de escrita binária
new_file.write(decrypt_data)            # Escreve os dados descriptografados no novo arquivo
new_file.close()                        # Fecha o novo arquivo após a escrita
