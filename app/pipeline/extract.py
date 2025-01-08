import os # Biblioteca para manipular arquivos e pastas
import glob # Biblioteca para listar arquivos

import pandas as pd
from typing import List


path = './data/input'


def extract_from_excel(path: str) -> List[pd.DataFrame]:
    """
    Função para ler os aquivos de uma pasta data/input e retornar uma lista de dataframes.

    args: input_path (str): caminho da pasta de arquivos

    return: lista de dataframes
    """

    all_files = glob.glob(os.path.join(path, '*.xlsx'))

    data_frame_list = []
    for file in all_files:
        data_frame_list.append(pd.read_excel(file))

    return data_frame_list


if __name__ == '__main__':
    data_frame_list = extract_from_excel(path='./data/input')
    print(data_frame_list)
