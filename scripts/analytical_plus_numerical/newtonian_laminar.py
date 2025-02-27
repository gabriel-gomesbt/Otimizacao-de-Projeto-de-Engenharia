import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def plot_analytyical():
    # Definição dos parâmetros do problema
    R = 0.7 # Raio do tubo (m)
    L = 2.3  # Comprimento do tubo (m)
    mu = 0.001  # Viscosidade dinâmica do fluido (Pa.s) (exemplo: água)
    v_0 = 1
    dPdz = -(8 * mu * v_0) / (R**2)

    # Definição do perfil de velocidade
    r = np.linspace(-R, R, 100)  # Coordenada radial (0 a R)
    u = - (1 / (4 * mu)) * dPdz * (R**2 - r**2)  # Perfil de velocidade

    # Criando o gráfico
    plt.figure(figsize=(8,6))
    plt.plot(u, r, label='Analítico', color='b')

    plt.xlabel('Velocidade u(r) (m/s)')
    plt.ylabel('Raio r (m)')
    plt.title('Perfil de Velocidade do Escoamento de Poiseuille')
    plt.legend()
    plt.grid(True)

    file_path = 'CSV/newtonian_laminar.csv'

    df = pd.read_csv(file_path)
    print(df)

    x1r=df['U_Magnitude']
    y1r=10*df['Points_1']

    plt.scatter(x1r, y1r, label='Numérico')
    plt.legend()
    plt.ylabel ('Newtoniano Laminar')


    plt.show()



if __name__ == '__main__':
    plot_analytyical()