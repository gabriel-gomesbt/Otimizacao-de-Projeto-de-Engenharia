import pandas as pd
import matplotlib.pyplot as plt

file_path = 'CSV/newtonian_turbulent.csv'

df = pd.read_csv(file_path)
print(df)

x1r=df['U_Magnitude']
y1r=10*df['Points_1']

plt.scatter(x1r, y1r)
plt.ylabel ('Newtoniano Turbulento')

plt.show()