import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

def treinarRegressaoLinear(arrays):
    # Dividir os dados em conjuntos de treinamento e teste
    x_treinamento, x_teste, y_treinamento, y_teste = train_test_split(
        arrays[0],
        arrays[1],
        test_size=0.20
    )
    print('Número de Dados usados para treinamento: {1}\nNúmero de Dados não utilizadas para treinamento: {0}'.format(len(x_treinamento), len(x_teste)))

    treinamento = [x_treinamento, y_treinamento, x_teste, y_teste]
    analisarPerfomance(treinamento)

def analisarPerfomance(treinamento):
    #Avaliar performance dos dados.
    modelo = LinearRegression()
    modelo.fit(treinamento[0], treinamento[1])
    print('Avaliação de performance: {}'.format(modelo.score(treinamento[0], treinamento[1])))

    # Margem de erro da previsão.
    previsoes = modelo.predict(treinamento[2])
    print('RMSE/Margem de Erro', np.sqrt(metrics.mean_squared_error(treinamento[3], previsoes)))

    #Plot do Gráfico com Previsão!
    plt.figure(figsize=(10, 5))
    plt.scatter(treinamento[0], treinamento[1])
    plt.title('Gráfico com 2 Eixos [ Salario x Limite ]')
    plt.xlabel('Salário')
    plt.ylabel('Limite')
    plt.plot(treinamento[2], modelo.predict(treinamento[2]), color='red')
    plt.show(block=True)