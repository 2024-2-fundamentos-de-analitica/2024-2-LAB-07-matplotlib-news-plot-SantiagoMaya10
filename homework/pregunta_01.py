"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    
    
    plt.figure()

    df = pd.read_csv("files/input/news.csv", index_col=0)

    colors ={
        'Television': 'dimgray',
        'Radio': 'lightgrey',
        'Newspaper': 'grey',
        'Internet': 'tab:blue',
    }

    zorder ={
        'Television': 1,
        'Radio': 1,
        'Newspaper': 1,
        'Internet': 2,
    }

    linewidths ={
        'Television': 2,
        'Radio': 2,
        'Newspaper': 2,
        'Internet': 3,
    }
    for col in df.columns:
        plt.plot(
            df[col],
            color = colors[col],
            zorder = zorder[col],
            linewidth = linewidths[col],
            label=col)
    
    plt.title("How people get news")
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)

    for col in df.columns:
        first_year = df.index[0]
        plt.scatter(
            x = first_year,
            y = df[col][first_year],
            color = colors[col],
            zorder = zorder[col]
        )
        plt.text(
            x = first_year-0.2,
            y = df[col][first_year],
            s = col + ""+str(df[col][first_year]) + "%",
            color = colors[col],
            zorder = zorder[col],
            ha = 'right',
            va = 'center'
        )

        last_year = df.index[-1]
        plt.scatter(
            x = last_year,
            y = df[col][last_year],
            color = colors[col],
            zorder = zorder[col]
        )

        plt.text(
            x = last_year+0.2,
            y = df[col][last_year],
            s = str(df[col][last_year]) + "%",
            color = colors[col],
            zorder = zorder[col],
            ha = 'left',
            va = 'center'
        )

    import os
    if not os.path.exists("files/plots"):
        os.makedirs("files/plots")

    plt.savefig("files/plots/news.png")
    plt.close()

pregunta_01()
