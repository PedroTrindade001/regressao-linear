import pandas as pd

def fromFileToArrays(filePath):
    arrays = []

    if ".csv" in filePath:
        print("A string contém a extensão .csv")
        BaseDados = pd.read_csv(filePath)
        Eixo_x = BaseDados.iloc[:, 0].values
        Eixo_y = BaseDados.iloc[:, 1].values
        arrays.append(Eixo_x)
        arrays.append(Eixo_y)
    elif ".xlsx" in filePath:
        print("A string contém a extensão .xlsx")
        BaseDados = pd.read_excel(filePath, 'Plan1')
        Eixo_x = BaseDados.iloc[:, 0].values
        Eixo_y = BaseDados.iloc[:, 1].values
        arrays.append(Eixo_x)
        arrays.append(Eixo_y)
    else:
        print("A string não contém nenhuma das extensões especificadas")

    return arrays
