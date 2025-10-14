import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y) # plotagem simples
plt.title("Primeiro gráfico com Matplotlib") # título do gráfico
plt.xlabel("x") # rótulo do eixo x
plt.ylabel("sin(x)") # rótulo do eixo y
plt.show() # exibe o gráfico

plt.figure() # cria uma nova figura

#figura e eixos
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(7,4)) # cria uma figura
ax = fig.add_subplot(1,1,1) # adiciona um subplot
ax.plot(x, y) # plota no subplot
ax.set(title="API orientada a objetos", xlabel="x", ylabel="sin(x)") # define título e rótulos
fig.tight_layout() # ajusta o layout
plt.show()

#linha básica
x = np.linspace(0, 2*np.pi, 256) # valores de x de 0 a 2π
plt.figure(figsize=(7,4)) # cria uma figura
plt.plot(x, np.sin(x), color="steelblue", linestyle="-", linewidth=2, label="seno") # plota o seno
plt.plot(x, np.cos(x), color="tomato", linestyle="--", linewidth=2, label="cosseno") # plota o cosseno
plt.title("Seno e Cosseno") # título do gráfico
plt.xlabel("Ângulo (rad)") # rótulo do eixo x
plt.ylabel("Valor") # rótulo do eixo y
plt.legend()() # exibe a legenda
plt.grid(True, alpha=.3) # adiciona uma grade
plt.show()

#rótulos, limites e ticks
fig, ax = plt.subplots(figsize=(7,4)) # cria figura e eixos
ax.plot(x, np.sin(x)) # plota o seno
ax.set_title("Customização de eixos") # título do gráfico
ax.set_xlabel("Ângulo (rad)") # rótulo do eixo x
ax.set_ylabel("sin(x)") # rótulo do eixo y
ax.set_xlim(0, 2*np.pi) # define limites do eixo x
ax.set_ylim(-1.1, 1.1) # define limites do eixo y
ax.grid(True, linestyle=":") # adiciona uma grade personalizada
plt.show() 

#Subplots com plt.subplot
plt.figure(figsize=(7,5)) # cria uma figura
plt.subplot(2,1,1) # primeiro subplot
plt.plot(x, np.sin(x)); plt.title("Seno") # título do primeiro subplot
plt.subplot(2,1,2) # segundo subplot
plt.plot(x, np.cos(x)); plt.title("Cosseno") # título do segundo subplot
plt.tight_layout() # ajusta o layout
plt.show()

fig, axes = plt.subplots(1,2, figsize=(9,3), sharex=True, sharey=True)
axes[0].plot(x, np.sin(x)); axes[0].set_title("Seno")
axes[1].plot(x, np.cos(x)); axes[1].set_title("Cosseno")
fig.suptitle("Múltiplos painéis com OO", y=1.05)
fig.tight_layout()
plt.show()

#Dispersão básica
rng = np.random.default_rng(0) # gerador de números aleatórios
X = rng.normal(size=100)# 100 pontos normais
Y = 0.5*X + rng.normal(scale=0.6, size=100)# relação linear com ruído
plt.figure(figsize=(6.5,4)) # cria uma figura
plt.scatter(X, Y) # gráfico de dispersão
plt.title("Relação entre X e Y") # título do gráfico
plt.xlabel("X"); plt.ylabel("Y") # rótulos dos eixos
plt.show()

#dispersão com estilo
sizes = 50 + 250*(np.abs(X)/X.max()) # tamanhos baseados em |X|
colors = Y # cores baseadas em Y
plt.figure(figsize=(6.5,4)) # cria uma figura
sc = plt.scatter(X, Y, s=sizes, c=colors, alpha=.8, cmap="viridis", edgecolor="k") # gráfico de dispersão estilizado
plt.colorbar(sc, label="Y") # barra de cores
plt.title("Dispersão com tamanho e cor mapeados") # título do gráfico
plt.grid(True, alpha=.3) # adiciona uma grade
plt.show()

#Histograma básico
data = rng.normal(loc=0, scale=1, size=1000) # 1000 pontos normais
plt.figure(figsize=(6.5,4)) # cria uma figura
plt.hist(data, bins=30, color="steelblue", edgecolor="k", alpha=.9) # histograma
plt.title("Histograma (bins=30)") # título do gráfico
plt.xlabel("Valor"); plt.ylabel("Frequência") # rótulos dos eixos
plt.show()

#Histograma com densidade
plt.figure(figsize=(6.5,4)) # cria uma figura
plt.hist(data, bins=30, density=True, histtype="stepfilled", alpha=.6) # histograma com densidade
plt.title("Densidade aproximada via histograma") # título do gráfico
plt.xlabel("Valor"); plt.ylabel("Densidade") # rótulos dos eixos
plt.show()

#Boxplot simples
grupo_A = rng.normal(0, 1, 200)
grupo_B = rng.normal(0.5, 1.3, 200)
grupo_C = rng.normal(-0.2, 0.8, 200)
plt.figure(figsize=(7,4))
plt.boxplot([grupo_A, grupo_B, grupo_C], labels=["A","B","C"])
plt.title("Boxplots por grupo")
plt.ylabel("Valor")
plt.grid(True, axis="y", alpha=.3)
plt.show()

#Boxplot com opções
plt.figure(figsize=(7,4))
plt.boxplot([grupo_A, grupo_B, grupo_C], labels=["A","B","C"],
showmeans=True, meanline=True, patch_artist=True,
boxprops=dict(facecolor="lavender"))
plt.title("Boxplots com média e preenchimento")
plt.show()

#Gráfico de barras simples
cats = ["A","B","C","D"]# categorias
vals = [25, 35, 20, 20]# valores
plt.figure(figsize=(7,4)) # cria uma figura
plt.bar(cats, vals, color=["#4C78A8","#F58518","#E45756","#72B7B2"]) # gráfico de barras
plt.title("Distribuição por categoria") # título do gráfico
plt.ylabel("%") # rótulo do eixo y
plt.grid(axis="y", alpha=.3) # adiciona uma grade horizontal
plt.show()

#Barras empilhadas
import numpy as np
base = np.array([30, 40, 20, 10])# valores base
extra = np.array([20, 15, 10, 5])# valores extras
labs = ["Q1","Q2","Q3","Q4"]# rótulos
plt.figure(figsize=(7,4)) # cria uma figura
plt.bar(labs, base, label="Base") # barras base
plt.bar(labs, extra, bottom=base, label="Extra") # barras extras empilhadas
plt.title("Barras empilhadas") # título do gráfico
plt.legend() # exibe a legenda
plt.show()

#Gráfico de Setores circulares (pizza)
plt.figure(figsize=(6,6)) # cria uma figura
plt.pie(vals, labels=cats, autopct="%1.1f%%", startangle=90) # gráfico de pizza
plt.title("Participação relativa") # título do gráfico
plt.axis("equal") # aspecto igual
plt.show()

#Anotações e setas
plt.figure(figsize=(7,4)) # cria uma figura
plt.plot(x, np.sin(x)) # plota o seno
plt.annotate("Pico", xy=(np.pi/2, 1), xytext=(2.2, 1.2),# anotação com seta
arrowprops=dict(arrowstyle="->"))# ponto de anotação
plt.title("Usando annotate para destacar pontos") # título do gráfico
plt.show()

#Salvando gráficos
fig, ax = plt.subplots(figsize=(6,4))
ax.plot(x, np.sin(x), label="seno")
ax.legend()
fig.tight_layout()
fig.savefig("fig_seno.pdf")

#Estilos prontos
plt.style.use('seaborn-v0_8')# usar estilo seaborn
plt.figure(figsize=(7,4))# cria uma figura
plt.plot(x, np.sin(x), label="seno")# plota o seno
plt.plot(x, np.cos(x), label="cosseno")# plota o cosseno
plt.legend(); plt.title("Usando um estilo predefinido")# exibe o gráfico
plt.show()
# Voltar ao clássico para os próximos exemplos
#plt.style.use('classic')

#Tema escuro rápido
plt.style.use('dark_background')
plt.figure(figsize=(7,4))
plt.plot(x, np.sin(x), linewidth=3)
plt.title("Estilo dark_background")
plt.show()
plt.style.use('classic') # voltar ao clássico

#Pandas + Matplotlib
import pandas as pd
rng = np.random.default_rng(42) # gerador de números aleatórios
df = pd.DataFrame({
"dia": pd.date_range("2025-09-01", periods=14, freq="D"),
"max": rng.normal(24, 3, 14).round(1),
"min": rng.normal(16, 2, 14).round(1),
})# dados de temperatura
ax = df.plot(x="dia", y=["max","min"], figsize=(8,4), title="Temperaturas")# plota com pandas
ax.set_xlabel(""); ax.set_ylabel("°C"); ax.grid(True, alpha=.3)# rótulos e grade
plt.show()

#Seaborn - Gráfico de Dispersão
import seaborn as sns
# Dadaset de gorjetas
df = sns.load_dataset('tips')
# Gráfico de dispersão com linha de regressão
plt.figure()
sns.lmplot(x='total_bill', y='tip', data=df)
plt.title('Relação entre Conta Total e Gorjeta')
plt.show()

#Seaborn - Boxplot
# Boxplot por dia da semana
plt.figure()
sns.boxplot(x='day', y='total_bill', data=df, palette='Set2')
plt.title('Distribuição da Conta por Dia da Semana')
plt.show()

#Seaborn - contagem
# Contagem de fumantes por sexo
plt.figure()
sns.countplot(x='sex', hue='smoker', data=df, palette='pastel')
plt.title('Fumantes por Sexo')
plt.show()








