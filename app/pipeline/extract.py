import os # Biblioteca para manipular arquivos e pastas
import glob # Biblioteca para listar arquivos

import pandas as pd

from typing import List

'''
função para ler os arquivos de uma 
pasta data/imput e retornar uma lista de dataframes

args: imput_path (str): caminho da pasta com os arquivos

return: lista dataframes
'''

def extract_from_excel(path: str) -> List[pd.DataFrame]:
    all_files = glob.glob(os.path.join(path, '*.xlsx'))

    data_frame_list = []
    for file in all_files:
        data_frame_list.append(pd.read_excel(file))
    
    return data_frame_list

if __name__ == "__main__":
    data_frame_list = extract_from_excel('data/input')
    print(data_frame_list)

