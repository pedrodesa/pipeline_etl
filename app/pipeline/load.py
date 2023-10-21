import pandas as pd

'''
Receber um dataframe e salvar como excel

args: 
data_frame (pd.DataFrame): dataframe a ser salvo como excel
output_path (str): caminho onde o arquivo será salvo
file_name (str): nome do arquivo que será salvo

return: "Arquivo salvo com sucesso!"
'''

def load_excel(data_frame: pd.DataFrame, output_path: str, file_name: str) -> str:
    data_frame.to_excel(f"{output_path}/{file_name}.xlsx, index = False")
    return "Arquivo salvo com sucesso"
