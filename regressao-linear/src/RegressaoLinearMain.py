from src.services.ArquivoService import fromFileToArrays
from src.services.RegressaoLinearService import treinarRegressaoLinear
from src.view.GraphView import plotGraph

filePath = "BaseDados_RegressaoLinear.csv"
arrays = fromFileToArrays(filePath)
plotGraph(arrays)
arrays[0] = arrays[0].reshape(-1, 1)
arrays[1] = arrays[1].reshape(-1, 1)
treinarRegressaoLinear(arrays)