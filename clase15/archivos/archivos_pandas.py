import pandas as pd
import matplotlib.pyplot as plt

def guardar_csv():
    df = pd.DataFrame({
        "Nombre": ["Cesar Diaz", "Sebastian Murillo", "Nataly Rodriguez", "Betsy Gamboa"],
        "Edad": [41, 32, 25, 19],
        "Profesor": [True, False, False, False],
        "Nota": [5.0, 3.5, 4.0, 3.7]
    })
    print(df)
    
    # Guardar en csv
    df.to_csv("personas.csv", sep=";")

def leer_csv():
    df = pd.read_csv("personas.csv", sep=";")
    del df["index"]
    print(df)

    print(df.describe())

    df.plot.bar(x="Nombre", y="Edad")
    plt.show()

