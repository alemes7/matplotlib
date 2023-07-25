# Importar a biblioteca matplotlib.pyplot
import matplotlib.pyplot as plt

# Dados das variáveis
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

# Criação do gráfico de área
plt.fill_between(x, y)

# Exibir o gráfico criado
plt.show()