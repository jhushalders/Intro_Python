#PANDAS + SEABORN

#preparando o ambiente
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="whitegrid")

#carregando o dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00267/data_banknote_authen
cols = ["variance","skewness","curtosis","entropy","class"]
dados = pd.read_csv(url, header=None, names=cols)
dados.head()

#dimensão e tipo
dados.shape
dados.dtypes

#Converter a classe para texto
dados["class"] = dados["class"].map({0:"falsa", 1:"autêntica"})
dados["class"].value_counts()

#Gráfico de barras
ax = sns.countplot(data=dados, x="class")
ax.set_title("Distribuição de classes")
ax.set_xlabel(""); ax.set_ylabel("Contagem")
for c in ax.containers:
ax.bar_label(c, fmt="%.0f")
plt.tight_layout(); plt.show()

#Histograma: variance
sns.histplot(data=dados, x="variance", bins=30)
plt.title("Histograma — variance")
plt.tight_layout(); plt.show()

#Histograma: skewness
sns.histplot(data=dados, x="skewness", bins=30)
plt.title("Histograma — skewness")
plt.tight_layout(); plt.show()

#Histograma: curtosis
sns.histplot(data=dados, x="curtosis", bins=30)
plt.title("Histograma — curtosis")
plt.tight_layout(); plt.show()

#Histograma: entropy
sns.histplot(data=dados, x="entropy", bins=30)
plt.title("Histograma — entropy")
plt.tight_layout(); plt.show()

#Histogramas por classe (variance)
sns.histplot(data=dados, x="variance", hue="class", bins=30, alpha=0.6)
plt.title("Variance por classe")
plt.tight_layout(); plt.show()

#Densidade (KDE) por classe (skewness)
sns.kdeplot(data=dados, x="skewness", hue="class", fill=True, alpha=0.5)
plt.title("Skewness — densidade por classe")
plt.tight_layout(); plt.show()

#$Boxplot: skewness por classe
sns.boxplot(data=dados, x="class", y="skewness")
plt.title("Boxplot — skewness por classe")
plt.tight_layout(); plt.show()

#Boxplot: curtosis por classe
sns.boxplot(data=dados, x="class", y="curtosis")
plt.title("Boxplot — curtosis por classe")
plt.tight_layout(); plt.show()

#Violino: entropy por classe
sns.violinplot(data=dados, x="class", y="entropy", inner="quartile")
plt.title("Violino — entropy por classe")
plt.tight_layout(); plt.show()

#Dispersão: variance × skewness
sns.scatterplot(data=dados, x="variance", y="skewness", hue="class", s=25, alpha=0.7)
plt.title("Scatter — variance × skewness")
plt.tight_layout(); plt.show()

#Dispersão: variance × entropy
sns.scatterplot(data=dados, x="variance", y="entropy", hue="class", s=25, alpha=0.7)
plt.title("Scatter — variance × entropy")
plt.tight_layout(); plt.show()

#Ajuste de estilo rápido
sns.set_theme(style="ticks") ## outras opções: darkgrid", "ticks"
sns.histplot(data=dados, x="variance", bins=30)
plt.title("Mesmo histograma, outro estilo")
plt.tight_layout(); plt.show()
sns.set_theme(style="whitegrid") ## retorna ao padrão

#Pairplot básico
g = sns.pairplot(dados, hue="class", corner=True, diag_kind="hist")
g.fig.suptitle("Relações gerais entre variáveis", y=1.02)
plt.show()

#Correlação via heatmap simples
corr = dados.drop(columns="class").corr(numeric_only=True)
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", center=0)
plt.title("Matriz de correlação (Pearson)")
plt.tight_layout(); plt.show()

#Limitando eixos
x1, x2 = dados["variance"].quantile([0.05, 0.95])
y1, y2 = dados["skewness"].quantile([0.05, 0.95])
ax = sns.scatterplot(data=dados, x="variance", y="skewness", s=20, alpha=0.6)
ax.set_xlim(x1, x2); ax.set_ylim(y1, y2)
ax.set_title("Zoom nos 5%–95%")
plt.tight_layout(); plt.show()

#Anotando pontos no gráfico
ax = sns.scatterplot(data=dados, x="variance", y="entropy", s=20, alpha=0.6)
ax.annotate("Região densa", xy=(dados["variance"].median(), dados["entropy"].median()),
xytext=(1, 4), arrowprops=dict(arrowstyle="->"))
ax.set_title("Exemplo de anotação")
plt.tight_layout(); plt.show()

#Salvando figuras (PNG)
ax = sns.histplot(data=dados, x="variance", bins=30)
plt.title("Histograma — variance")
plt.tight_layout()
plt.savefig("hist_variance.png", dpi=150)
plt.show()
