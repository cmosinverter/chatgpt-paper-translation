import PyPDF2
import os

def convert_pdf_to_txt(file_name):

    # delete if the file already exists
    if os.path.exists(f'results/{file_name}.txt'):
        os.remove(f'results/{file_name}.txt')

    with open(f'papers/{file_name}.pdf', 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    
    with open(f'results/{file_name}.txt', 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)