import matplotlib.pyplot as plt

def plotGraph(data):
    #Cria e mostra o gráfico.
    plt.figure(figsize=(10, 5))
    plt.scatter(data[0], data[1])
    plt.title('Gráfico com 2 Eixos [ Salario x Limite ]')
    plt.xlabel('Salário')
    plt.ylabel('Limite')
    plt.show(block=True)