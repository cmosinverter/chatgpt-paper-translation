import PyPDF2
import os

def get_split_list(pdf_name):

    # delete if the file already exists
    if os.path.exists(f'text/{pdf_name}.txt'):
        os.remove(f'text/{pdf_name}.txt')

    with open(f'papers/{pdf_name}.pdf', 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    
    with open(f'text/{pdf_name}.txt', 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)

    sentence_end_index = []

    with open(f'text/{pdf_name}.txt', 'r', encoding='utf-8') as txt_file:
        for i, line in enumerate(txt_file):
            if (len(line.rstrip()) == 0) or (line.rstrip()[-1] == '.'):
                sentence_end_index.append(i)

    # print(sentence_end_index)
    split_index_list = [sentence_end_index[0]]

    for i in range(len(sentence_end_index)):
            if sentence_end_index[i] - split_index_list[-1] >= 15:
                split_index_list.append(sentence_end_index[i-1])
                
    if split_index_list[0] < 15:
        split_index_list.pop(0)

    split_index_list = [i+1 for i in split_index_list]
    split_index_list.insert(0, 0)

    return split_index_list

def read_specific_rows(file_path, start_row, end_row):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)

            # Adjust start_row and end_row if they exceed the number of lines
            start_row = max(start_row, 0)
            end_row = min(end_row, num_lines)

            # Ensure start_row is smaller than end_row
            if start_row >= end_row:
                raise ValueError("Invalid start_row or end_row values.")

            selected_lines = lines[start_row:end_row]
            return '翻譯成繁體中文: '+' '.join(selected_lines).replace('\n', '')
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print("An error occurred:", str(e))

def create_txt_file(data, filename):
    # Join the list of strings with newline characters
    text = '\n\n'.join(data)

    # Create the text file
    with open(filename, 'w') as file:
        file.write(text)