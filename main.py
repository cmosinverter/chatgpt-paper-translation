import pypdf
import os

from utils import convert_pdf_to_txt

# Example usage
pdf_name = '1.pdf'
convert_pdf_to_txt(pdf_name.split('.')[0])

sentence_end_index = []

with open(f'results/{pdf_name.split(".")[0]}.txt', 'r', encoding='utf-8') as txt_file:
    for i, line in enumerate(txt_file):
        if len(line.rstrip()) == 0:
            continue
        if line.rstrip()[-1] == '.':
            # print(i, line.rstrip())
            sentence_end_index.append(i)

print(sentence_end_index)