# Extração de Texto de Imagens com OCR (Tesseract)

Este script realiza a extração de texto de imagens utilizando OCR (Reconhecimento Óptico de Caracteres) com a biblioteca [Tesseract](https://github.com/tesseract-ocr/tesseract). As imagens devem estar no formato `.jpeg`, `.jpg` ou `.png` e devem estar localizadas em uma pasta específica. O texto extraído das imagens é salvo em um arquivo Excel, junto com informações extraídas do nome dos arquivos de imagem.

## Requisitos

Antes de executar o script, certifique-se de que as seguintes dependências estão instaladas:

- Python 3.x
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- Bibliotecas Python:
  - `pytesseract`
  - `pillow` (PIL)
  - `pandas`

Você pode instalar as dependências Python utilizando o seguinte comando:

```bash
pip install pytesseract pillow pandas openpyxl



### Explicação do `README.md`:

- **Requisitos**: Instruções sobre as bibliotecas necessárias e a instalação do Tesseract.
- **Como Funciona**: Explicação sobre o que o código faz, como ele processa as imagens e como extrai as informações.
- **Configuração**: Instruções para configurar o caminho do Tesseract no arquivo `config.py`.
- **Como Executar**: Passos detalhados para executar o script, desde a instalação até a execução do código.
- **Exemplo de Saída**: Descrição das colunas que estarão presentes no arquivo Excel gerado.
# gerador-planilha-importacao
