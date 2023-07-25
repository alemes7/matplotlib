# Para criar um gráfico de dispersão em Matplotlib, você pode usar a função scatter() que cria um gráfico de 
# dispersão representando os dados em um array. 

# scatter(): é um método que cria um gráfico de dispersão representando os dados em um array.
# array: é uma estrutura de dados que armazena um conjunto de valores.

#-----------------------------------------------------------------------------------------------------------------

# Importar a biblioteca matplotlib.pyplot
import matplotlib.pyplot as plt

# Criação das arrays x e y com os dados/valores que estabelecemos para cada uma
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

# Criação do gráfico a partir das variáveis x, y
plt.scatter(x, y)

# show(): é um método que exibe o gráfico criado. Com isso, nosso gráfico será criado
plt.show()