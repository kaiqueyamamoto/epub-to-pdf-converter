import ebooklib
from ebooklib import epub
from reportlab.pdfgen import canvas
from lxml import etree
import os

def epub_to_pdf(epub_path, pdf_path):
    # Carrega o arquivo EPUB
    book = epub.read_epub(epub_path)
    
    # Cria um PDF usando ReportLab
    c = canvas.Canvas(pdf_path)
    width, height = c._pagesize  # Obtém as dimensões da página do PDF
    
    margin = 72  # Define uma margem de uma polegada
    x = margin  # A posição x onde o texto começará
    y = height - margin  # A posição y inicial para o texto
    
    font_size = 12  # Define o tamanho da fonte
    c.setFont("Helvetica", font_size)
    
    line_height = font_size * 1.5  # Define a altura da linha baseada no tamanho da fonte
    
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            # Extrai o conteúdo HTML
            html_content = item.get_body_content()
            # Converte para texto
            root = etree.HTML(html_content)
            text = ''.join(root.itertext())
            
            # Itera por cada linha do texto
            for line in text.splitlines():
                # Quebra a página se não houver espaço suficiente para a próxima linha
                if y < margin:  # Se a posição y for menor que a margem, cria uma nova página
                    c.showPage()
                    c.setFont("Helvetica", font_size)
                    y = height - margin  # Reseta a posição y para o topo da nova página
                
                # Adiciona a linha ao PDF
                c.drawString(x, y, line[:100])  # Limita a linha a 100 caracteres como exemplo
                y -= line_height  # Move para a próxima linha
    
    c.save()

def convert_all_epubs(input_folder, output_folder):
    # Verifica se a pasta de saída existe, se não, cria
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Lista todos os arquivos .epub na pasta de entrada
    for filename in os.listdir(input_folder):
        if filename.endswith('.epub'):
            epub_path = os.path.join(input_folder, filename)
            pdf_filename = filename.replace('.epub', '.pdf')
            pdf_path = os.path.join(output_folder, pdf_filename)
            epub_to_pdf(epub_path, pdf_path)
            print(f"Convertido: {filename} para PDF.")

# Caminhos das pastas de entrada e saída
input_folder = 'input'
output_folder = 'output'

convert_all_epubs(input_folder, output_folder)
