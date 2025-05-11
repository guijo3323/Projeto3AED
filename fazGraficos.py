import numpy as np
import matplotlib.pyplot as plt

#https://stackoverflow.com/questions/29885408/how-plot-polyfit-n-log-n-with-python


def fazGraficos(tamanhos, tempos,titulo):
    conjuntos = ['Conjunto A', 'Conjunto B', 'Conjunto C']
    cores = ['blue', 'green', 'red']

    plt.figure(figsize=(10, 6))

    for i in range(3):
        x = np.array(tamanhos)
        y = np.array(tempos[i])

        if titulo == 'Insertion Sort':  # O(n^2)
            regressao = np.polyfit(x, y, 2)  # grau 2
            poly_fn = np.poly1d(regressao)
            plt.plot(x, poly_fn(x), '-', color=cores[i], label=f'{conjuntos[i]} (regressão n²)')
        else:  # O(n log n)
            x_log = x * np.log(x)
            regressao = np.polyfit(x_log, y, 1)  # grau 1 em n log n
            poly_fn = np.poly1d(regressao)
            plt.plot(x, poly_fn(x_log), '-', color=cores[i], label=f'{conjuntos[i]} (regressão n log n)')

        plt.plot(x, y, 'o', color=cores[i], label=f'{conjuntos[i]} (real)')
    plt.title(titulo)
    plt.xlabel('Tamanho do array')
    plt.ylabel('Tempo (ms)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

