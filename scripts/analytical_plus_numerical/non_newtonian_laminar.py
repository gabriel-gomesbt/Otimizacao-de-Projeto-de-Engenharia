import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def plot_analytical():
    # Definição de parâmetros
    R = 0.7  # Raio do tubo (m)
    K = 10  # Índice de consistência (Pa.s^n)
    n = 0.1  # Expoente da lei de potência
    L = 5 # Comprimento do cilindro
    deltaP = 1.9 # Queda de pressão no cilindro


    # Definição da malha radial
    r = np.linspace(-R, R, 100)  # Posição radial de 0 até R

    # Cálculo da velocidade média
    average_u = (((1/2*K)*(deltaP/L))**(1/n))  *  (n/((3*n)+1))  *  (R**(1+(1/n)))

    # Perfil de velocidade
    u = average_u  *  (1 - (abs(r)/R)**((n+1)/n))  *  (((3*n)+1)/(n+1))


    # Plot do perfil de velocidade
    plt.figure(figsize=(6, 5))
    plt.plot(u, r, label=f"Analítico (n={n}, k={K})", color='b', linewidth=2)
    plt.xlabel("Velocidade (m/s)")
    plt.ylabel("Raio (m)")
    plt.title("Perfil de Velocidade de um Fluido Não Newtoniano\n em um Duto Cilíndrico")
    plt.gca().invert_yaxis()  # Inverte o eixo y para representar corretamente o raio
    plt.legend()
    plt.grid()

    file_path = 'CSV/non_newtonian_laminar.csv'

    df = pd.read_csv(file_path)
    print(df)

    x1r=df['U_Magnitude']
    y1r=10*df['Points_1']

    plt.scatter(x1r, y1r, label="Numérico" )
    plt.legend()
    plt.ylabel ('Não Newtoniano Laminar')


    plt.show()

if __name__ == "__main__":
    plot_analytical()