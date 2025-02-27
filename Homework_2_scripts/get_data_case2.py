import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata

def get_data_case_1(file_path):

    df = pd.read_csv(file_path)
    print(df)
          
    # Obtenção de Variáveis
    x_axys = df["Points_0"]  
    temperature_values = df["T"]  
    U_magnitude = np.sqrt(df["U_0"]**2 + df["U_1"]**2 + df["U_2"]**2) 

    # Gráfico de distribuição de temperatura ao longo de X

    plt.scatter(x_axys, temperature_values, c=temperature_values, cmap="hot", alpha=0.7)
    plt.xlabel("Position X")
    plt.ylabel("Temperature (K)")
    plt.title("Temperature Distribution")
    plt.colorbar(label="Temperature")
    plt.grid()
    plt.show()

    # Gráfico de dispersão da velocidade ao longo de X

    plt.scatter(x_axys, U_magnitude, c=U_magnitude, cmap="coolwarm", alpha=0.7)
    plt.xlabel("Position X")
    plt.ylabel("Velocity (m/s)")
    plt.title("Velocity Distribution")
    plt.colorbar(label="Velocity Magnitude")
    plt.grid()
    plt.show()


if __name__ == "__main__":
    
    file_path = "CSV/caso2.csv"
    get_data_case_1(file_path)