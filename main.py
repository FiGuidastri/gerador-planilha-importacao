import os
import re
from PIL import Image
import pytesseract
import pandas as pd
import time
from config import *

# Caminho do executável do Tesseract
pytesseract.pytesseract.tesseract_cmd = caminho_pasta
# Defina a variável de ambiente TESSDATA_PREFIX para apontar para o diretório 'tessdata'
os.environ["TESSDATA_PREFIX"] = os_environ

# Função para extrair texto das imagens e separar o nome do arquivo
def extract_text_from_images(image_folder, output_excel):
    # Lista para armazenar os dados
    data = []
    print('Iniciando processamento de imagens!')
    # Percorre todos os arquivos na pasta de imagens
    for file_name in os.listdir(image_folder):
        if file_name.lower().endswith(('.jpeg', '.jpg', '.png')):  # Filtra arquivos de imagem
            file_path = os.path.join(image_folder, file_name)
            
            try:
                # Abre a imagem
                img = Image.open(file_path)
                
                # Extrai o texto da imagem
                text = pytesseract.image_to_string(img, lang='por')  # Use 'eng' para inglês ou 'por' para português
                
                # Separando o nome do arquivo (dividindo pelo caractere '_')
                file_parts = file_name.split('_')
                #print(f"Nome do arquivo dividido: {file_parts}")  # Depuração

                # Verificando se a parte com 'Km' está presente
                km_type = file_parts[1] if len(file_parts) > 1 else ''
                #print(f"Valor de 'Km Type': {km_type}")  # Depuração
                tipo_servico = file_parts[4] if len(file_parts) > 4 else ''
                tipo_servico = tipo_servico[:-4]
                # Separando a coluna do tipo "Km 338+900 CENTRAL" com regex
                km_match = re.match(r'Km (\d+\+\d+)\s*(\w+)', km_type)  # Regex para extrair o número e o texto
                if km_match:
                    km_number = km_match.group(1)  # Números, como "338+900"
                    km_text = km_match.group(2)    # Texto, como "CENTRAL"
                else:
                    km_number = ''
                    km_text = ''
                
                # Adiciona os dados à lista
                data.append({
                    'Rodovia': file_parts[0] if len(file_parts) > 0 else '',
                    'Km': file_parts[1] if len(file_parts) > 1 else '',
                    'Data': file_parts[2] if len(file_parts) > 2 else '',
                    'Hora': file_parts[3] if len(file_parts) > 3 else '',
                    'Tipo de Serviço': tipo_servico,
                    'Km Número': km_number,  # Números extraídos
                    'Km Texto': km_text,    # Texto extraído
                    'Arquivo': file_name
                })
            except Exception as e:
                print(f"Erro ao processar {file_name}: {e}")
    
    # Cria um DataFrame e salva em uma planilha Excel
    df = pd.DataFrame(data)
    df.to_excel(output_excel, index=False, engine='openpyxl')
    print(f"Processamento concluído com sucesso! Dados salvos em {output_excel}")

# Configurações
image_folder = './data'  # Substitua pelo caminho da sua pasta
output_excel = 'resultados.xlsx'  # Nome do arquivo de saída

# Executa o script
extract_text_from_images(image_folder, output_excel)
