from src.services.ArquivoService import fromFileToArrays
from src.services.RegressaoLinearService import treinarRegressaoLinear
from src.view.GraphView import plotGraph

# Caminho do arquivo
filePath = "BaseDados_RegressaoLinear.cssv"
# Carregar os arrays a partir do arquivo (csv/xlsx)
arrays = fromFileToArrays(filePath)
if arrays:
    # Plotar o gráfico
    plotGraph(arrays)
    # Redimensionar os arrays para uso na regressão linear
    arrays[0] = arrays[0].reshape(-1, 1)
    arrays[1] = arrays[1].reshape(-1, 1)
    # Treinar o modelo de regressão linear/Mostrar linha de regressão
    treinarRegressaoLinear(arrays)
else:
    print("Formato não suportado!")