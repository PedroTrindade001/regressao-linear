import pandas as pd

def fromFileToArrays(filePath):
    arrays = []

    if ".csv" in filePath:
        print("A string contém a extensão .csv")
        # Carrega o arquivo CSV usando o pandas
        BaseDados = pd.read_csv(filePath)
        # Extrai as colunas de interesse como arrays separados
        Eixo_x = BaseDados.iloc[:, 0].values
        Eixo_y = BaseDados.iloc[:, 1].values
        arrays.append(Eixo_x)
        arrays.append(Eixo_y)
    elif ".xlsx" in filePath:
        print("A string contém a extensão .xlsx")
        # Carrega o arquivo Excel usando o pandas
        BaseDados = pd.read_excel(filePath, 'Plan1')
        # Extrai as colunas de interesse como arrays separados
        Eixo_x = BaseDados.iloc[:, 0].values
        Eixo_y = BaseDados.iloc[:, 1].values
        arrays.append(Eixo_x)
        arrays.append(Eixo_y)
    else:
        print("A string não contém nenhuma das extensões especificadas")

    return arrays
