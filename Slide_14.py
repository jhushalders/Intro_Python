import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Implementação manual: gerando dados para regressão linear simples
# Fixando seed
np.random.seed(42)
# Gerando dados
n = 100
X = np.random.uniform(0, 10, n)
beta_0 = 5
beta_1 = 2
epsilon = np.random.normal(0, 2, n)
Y = beta_0 + beta_1 * X + epsilon
# Criando DataFrame
dados = pd.DataFrame({'X': X, 'Y': Y})
print(dados.head())

#estimando parâmetros
# Construindo matriz X (com intercepto)
X_mat = np.column_stack([np.ones(n), X])
# Estimando beta pelo método OLS
beta_hat = np.linalg.inv(X_mat.T @ X_mat) @ X_mat.T @ Y
print(f"Beta_0 estimado: {beta_hat[0]:.4f}")
print(f"Beta_1 estimado: {beta_hat[1]:.4f}")
# Valores ajustados
Y_hat = X_mat @ beta_hat
# Resíduos
residuos = Y - Y_hat

#métricas de ajuste
# Soma dos Quadrados
SQT = np.sum((Y - Y.mean())**2) # Total
SQR = np.sum(residuos**2) # Residual
SQReg = np.sum((Y_hat - Y.mean())**2) # Regressão
# R²
R2 = 1 - (SQR / SQT)
# R² ajustado
p = 1 # número de preditores (sem intercepto)
R2_adj = 1 - (1 - R2) * (n - 1) / (n - p - 1)
# Erro padrão residual
s = np.sqrt(SQR / (n - p - 1))
print(f"R²: {R2:.4f}")
print(f"R² ajustado: {R2_adj:.4f}")
print(f"Erro padrão residual: {s:.4f}")

#inferência
# Variância dos estimadores
var_beta_hat = s**2 * np.linalg.inv(X_mat.T @ X_mat)
ep_beta = np.sqrt(np.diag(var_beta_hat))
# Estatística t
t_stats = beta_hat / ep_beta
# Valor-p (teste bilateral)
from scipy import stats
p_values = 2 * (1 - stats.t.cdf(np.abs(t_stats), df=n-p-1))
print("\nCoeficientes:")
print(f"Beta_0: {beta_hat[0]:.4f} (EP: {ep_beta[0]:.4f}, t: {t_stats[0]:.2f}, p: {p_values[0]:.4f})")
print(f"Beta_1: {beta_hat[1]:.4f} (EP: {ep_beta[1]:.4f}, t: {t_stats[1]:.2f}, p: {p_values[1]:.4f})")

#usando statsmodels: sintaxe básica
import statsmodels.api as sm
# Adicionando intercepto à variável X
X_sm = sm.add_constant(X)
# Ajustando o modelo
modelo = sm.OLS(Y, X_sm)
resultado = modelo.fit()
# Resumo completo
print(resultado.summary())

#acessando resultados
# Coeficientes
print("Coeficientes:")
print(resultado.params)
# Intervalos de confiança
print("\nIntervalos de confiança (95%):")
print(resultado.conf_int())
# R² e R² ajustado
print(f"\nR²: {resultado.rsquared:.4f}")
print(f"R² ajustado: {resultado.rsquared_adj:.4f}")

#comparando resultados: manual vs statsmodels
# Comparação
comparacao = pd.DataFrame({
'Manual': beta_hat,
'Statsmodels': resultado.params,
'Diferença': np.abs(beta_hat - resultado.params)}, index=['Intercepto', 'X'])
print(comparacao)
# Os resultados devem ser idênticos (diferenças devido a arredondamento)

#regressão múltipla: gerando dados
# Gerando dados com 3 preditores
np.random.seed(123)
n = 150
X1 = np.random.uniform(0, 10, n)
X2 = np.random.uniform(0, 5, n)
X3 = np.random.uniform(-2, 2, n)
beta = np.array([3, 1.5, -2, 0.8]) # beta_0, beta_1, beta_2, beta_3
epsilon = np.random.normal(0, 1.5, n)
Y = beta[0] + beta[1]*X1 + beta[2]*X2 + beta[3]*X3 + epsilon
dados_mult = pd.DataFrame({
'Y': Y, 'X1': X1, 'X2': X2, 'X3': X3
})

#Regressão múltipla: implementação manual
# Construindo matriz X
X_mult = np.column_stack([np.ones(n), X1, X2, X3])
# Estimando beta
beta_hat_mult = np.linalg.inv(X_mult.T @ X_mult) @ X_mult.T @ Y
print("Coeficientes estimados (manual):")
for i, nome in enumerate(['Intercepto', 'X1', 'X2', 'X3']):
print(f"{nome}: {beta_hat_mult[i]:.4f}")

#regressão múltipla: usando statsmodels
# Preparando dados
X_mult_sm = sm.add_constant(dados_mult[['X1', 'X2', 'X3']])
# Ajustando modelo
modelo_mult = sm.OLS(dados_mult['Y'], X_mult_sm)
resultado_mult = modelo_mult.fit()
# Resumo
print(resultado_mult.summary())

#fórmulas no statsmodels
from statsmodels.formula.api import ols
# Sintaxe de fórmula
modelo_formula = ols('Y ~ X1 + X2 + X3', data=dados_mult)
resultado_formula = modelo_formula.fit()
print(resultado_formula.summary())

#diagnóstico de resíduos
fig, axes = plt.subplots(1, 2, figsize=(15, 4))
# 1. Resíduos vs Ajustados
axes[0].scatter(resultado_mult.fittedvalues, resultado_mult.resid, alpha=0.6)
axes[0].axhline(0, color='red', linestyle='--')
axes[0].set_xlabel('Valores Ajustados')
axes[0].set_ylabel('Resíduos')
axes[0].set_title('Resíduos vs Ajustados')
# 2. Histograma dos resíduos
axes[1].hist(resultado_mult.resid, bins=20, edgecolor='black')
axes[1].set_xlabel('Resíduos')
axes[1].set_ylabel('Frequência')
axes[1].set_title('Histograma dos Resíduos')
plt.tight_layout()
plt.show()

#teste de homocedasticidade: Breusch-Pagan
from statsmodels.stats.diagnostic import het_breuschpagan
# Teste de Breusch-Pagan
bp_test = het_breuschpagan(resultado_mult.resid, X_mult_sm)
labels = ['LM Statistic', 'LM p-value', 'F-Statistic', 'F p-value']
print("\nTeste de Breusch-Pagan (Homocedasticidade):")
for label, value in zip(labels, bp_test):
print(f"{label}: {value:.4f}")
print("\nInterpretação:")
print("H0: Homocedasticidade (variância constante)")
if bp_test[1] > 0.05:
print("Não rejeitamos H0 (p > 0.05): Assumimos homocedasticidade")
else:
print("Rejeitamos H0 (p < 0.05): Evidência de heterocedasticidade")

#teste de normalidade: Jarque-Bera
from statsmodels.stats.stattools import jarque_bera
# Teste de Jarque-Bera
jb_test = jarque_bera(resultado_mult.resid)
print("Teste de Jarque-Bera (Normalidade dos resíduos):")
print(f"Estatística JB: {jb_test[0]:.4f}")
print(f"p-value: {jb_test[1]:.4f}")
print(f"Skewness: {jb_test[2]:.4f}")
print(f"Kurtosis: {jb_test[3]:.4f}")
print("\nInterpretação:")
print("H0: Os resíduos seguem distribuição normal")
if jb_test[1] > 0.05:
print("Não rejeitamos H0 (p > 0.05): Assumimos normalidade")
else:
print("Rejeitamos H0 (p < 0.05): Evidência contra normalidade")

#teste de multicolinearidade: VIF (Variance Inflation Factor)
from statsmodels.stats.outliers_influence import variance_inflation_factor
# Calculando VIF para cada preditor
vif_data = pd.DataFrame()
vif_data["Variável"] = ['X1', 'X2', 'X3']
vif_data["VIF"] = [variance_inflation_factor(dados_mult[['X1', 'X2', 'X3']].values, i)
for i in range(3)]
print(vif_data)
print("\nInterpretação:")
print("VIF < 5: Baixa multicolinearidade")
print("5 <= VIF < 10: Multicolinearidade moderada")
print("VIF >= 10: Alta multicolinearidade (problema!)")

#Predição com novos dados
# Novos dados para predição
novos_dados = pd.DataFrame({
  'X1': [5.0, 7.5, 2.3],
'X2': [2.5, 3.0, 1.5],
'X3': [0.5, -1.0, 1.2]
})

# Adicionando intercepto
novos_X = sm.add_constant(novos_dados)
# Predições pontuais
predicoes = resultado_mult.predict(novos_X)
print("Predições pontuais:")
print(predicoes)
# Intervalos de predição
pred_int = resultado_mult.get_prediction(novos_X).summary_frame(alpha=0.05)
print("\nIntervalos de predição (95%):")
print(pred_int[['mean', 'obs_ci_lower', 'obs_ci_upper']])

#Visualização da reta de regressão (Simples)
plt.figure(figsize=(10, 6))
plt.scatter(X1, Y, alpha=0.6, label='Dados observados')
plt.scatter(X1, Y_hat_mult, color='red', label='Valores ajustados', alpha=0.7)
plt.xlabel('X1')
plt.ylabel('Y')
plt.title('Regressão Múltipla — projeção sobre X1')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

#Exemplo completo: dados simulados de vendas
# Simulando dados de vendas
np.random.seed(2024)
n = 200
# Variáveis preditoras
investimento_mkt = np.random.uniform(1000, 10000, n)
preco = np.random.uniform(50, 200, n)
concorrentes = np.random.randint(1, 10, n)
# Variável resposta (vendas)
vendas = (100 + 0.5*investimento_mkt - 0.3*preco
- 5*concorrentes + np.random.normal(0, 500, n))
df_vendas = pd.DataFrame({
'vendas': vendas,
'investimento_mkt': investimento_mkt,
'preco': preco,
'concorrentes': concorrentes
})
print(df_vendas.head())

#análise exploratória
import seaborn as sns
# Matriz de correlação
plt.figure(figsize=(8, 6))
sns.heatmap(df_vendas.corr(), annot=True, cmap='coolwarm', center=0)
plt.title('Matriz de Correlação')
plt.show()
# Estatísticas descritivas
print("\nEstatísticas Descritivas:")
print(df_vendas.describe())

#ajuste do modelo completo
from statsmodels.formula.api import ols
# Modelo completo
modelo_vendas = ols('vendas ~ investimento_mkt + preco + concorrentes',
data=df_vendas)
resultado_vendas = modelo_vendas.fit()
print(resultado_vendas.summary())

#diagnóstico do modelo completo
# Teste de Normalidade
from statsmodels.stats.stattools import jarque_bera
jb = jarque_bera(resultado_vendas.resid)
print(f"Jarque-Bera p-value: {jb[1]:.4f}")
# Teste de Homocedasticidade
from statsmodels.stats.diagnostic import het_breuschpagan
X_vendas = sm.add_constant(df_vendas[['investimento_mkt', 'preco', 'concorrentes']])
bp = het_breuschpagan(resultado_vendas.resid, X_vendas)
print(f"Breusch-Pagan p-value: {bp[1]:.4f}")
# VIF
from statsmodels.stats.outliers_influence import variance_inflation_factor
vif = pd.DataFrame()
vif["Variável"] = ['investimento_mkt', 'preco', 'concorrentes']
vif["VIF"] = [variance_inflation_factor(df_vendas[['investimento_mkt',
'preco', 'concorrentes']].values, i) for i in range(3)]
print("\n", vif)

#gráfico de diagnóstico integrados
from statsmodels.graphics.gofplots import ProbPlot
fig = plt.figure(figsize=(12, 8))
# 1. Resíduos vs Ajustados
ax1 = fig.add_subplot(221)
ax1.scatter(resultado_vendas.fittedvalues, resultado_vendas.resid, alpha=0.5)
ax1.axhline(0, color='red', linestyle='--', linewidth=2)
ax1.set_xlabel('Valores Ajustados')
ax1.set_ylabel('Resíduos')
ax1.set_title('Resíduos vs Valores Ajustados')
# 2. Q-Q Plot
ax2 = fig.add_subplot(222)
ProbPlot(resultado_vendas.resid).qqplot(line='s', ax=ax2)
ax2.set_title('Q-Q Plot Normal')
plt.tight_layout()
plt.show()
# 3. Scale-Location (Homocedasticidade)
ax3 = fig.add_subplot(223)
resid_padronizados = resultado_vendas.resid / np.std(resultado_vendas.resid)
ax3.scatter(resultado_vendas.fittedvalues, np.sqrt(np.abs(resid_padronizados)), alpha=0.5)
ax3.set_xlabel('Valores Ajustados')
ax3.set_ylabel('√|Resíduos Padronizados|')
ax3.set_title('Scale-Location')
# 4. Resíduos vs Leverage
ax4 = fig.add_subplot(224)
from statsmodels.stats.outliers_influence import OLSInfluence
influence = OLSInfluence(resultado_vendas)
leverage = influence.hat_matrix_diag
ax4.scatter(leverage, resid_padronizados, alpha=0.5)
ax4.axhline(0, color='red', linestyle='--')
ax4.set_xlabel('Leverage')
ax4.set_ylabel('Resíduos Padronizados')
ax4.set_title('Resíduos vs Leverage')
plt.tight_layout()
plt.show()

#detecção de outliers e observações influentes
from statsmodels.stats.outliers_influence import OLSInfluence
# Calculando medidas de influência
influence = OLSInfluence(resultado_vendas)
# Cook's Distance
cooks_d = influence.cooks_distance[0]
# Identificando observações influentes (Cook's D > 4/n)
threshold = 4 / len(df_vendas)
influentes = np.where(cooks_d > threshold)[0]
print(f"Observações influentes (Cook's D > {threshold:.4f}):")
print(influentes)
print(f"\nTotal: {len(influentes)} observações")
# DFBETAS
dfbetas = influence.dfbetas
print(f"\nMaior DFBETA para intercepto: {np.max(np.abs(dfbetas[:, 0])):.4f}")

#comparação de modelos: AIC e BIC
# Modelo 1: Todas variáveis
modelo1 = ols('vendas ~ investimento_mkt + preco + concorrentes',
data=df_vendas).fit()
# Modelo 2: Sem concorrentes
modelo2 = ols('vendas ~ investimento_mkt + preco',
data=df_vendas).fit()
# Modelo 3: Apenas investimento
modelo3 = ols('vendas ~ investimento_mkt',
data=df_vendas).fit()
# Comparação
comparacao = pd.DataFrame({
'Modelo': ['Completo', 'Sem Concorrentes', 'Apenas Marketing'],
'R²': [modelo1.rsquared, modelo2.rsquared, modelo3.rsquared],
'R² Ajustado': [modelo1.rsquared_adj, modelo2.rsquared_adj,
modelo3.rsquared_adj],
'AIC': [modelo1.aic, modelo2.aic, modelo3.aic],
'BIC': [modelo1.bic, modelo2.bic, modelo3.bic]
})
print(comparacao)
print("\nMenor AIC/BIC indica melhor modelo (penaliza complexidade)")

#Intervalos de confiança vs intervalos de predição
# Criando novos dados
novo_cenario = pd.DataFrame({
'investimento_mkt': [5000],
'preco': [100],
'concorrentes': [5]
})
# Predição com intervalos
predicao = resultado_vendas.get_prediction(novo_cenario)
frame = predicao.summary_frame(alpha=0.05)
print("Predição para novo cenário:")
print(frame[['mean', 'mean_ci_lower', 'mean_ci_upper',
'obs_ci_lower', 'obs_ci_upper']])
print("\nInterpretação:")
print("- IC da média: onde esperamos que a MÉDIA das vendas esteja")
print("- IC da observação: onde esperamos que UMA venda individual esteja")
print("- IC da observação é sempre mais amplo!")

#Regressão com variáveis categóricas
# Adicionando variável categórica
np.random.seed(42)
df_vendas['regiao'] = np.random.choice(['Norte', 'Sul', 'Leste', 'Oeste'],
size=len(df_vendas))
# Modelo com variável categórica
modelo_categ = ols('vendas ~ investimento_mkt + preco + concorrentes + regiao',
data=df_vendas).fit()
print(modelo_categ.summary())
# Statsmodels cria automaticamente variáveis dummy
# Uma categoria é usada como referência (baseline)

#Teste F para restrições lineares
# Testando se múltiplos coeficientes são zero simultaneamente
# H0: beta_preco = 0 e beta_concorrentes = 0
# Modelo restrito (sem preco e concorrentes)
modelo_restrito = ols('vendas ~ investimento_mkt', data=df_vendas).fit()
# Teste F
from scipy import stats
SQR_completo = resultado_vendas.ssr # Soma dos quadrados dos resíduos
SQR_restrito = modelo_restrito.ssr
n = len(df_vendas)
p_completo = resultado_vendas.df_model
p_restrito = modelo_restrito.df_model
q = p_completo - p_restrito # número de restrições
F_stat = ((SQR_restrito - SQR_completo) / q) / (SQR_completo / (n - p_completo - 1))
p_value = 1 - stats.f.cdf(F_stat, q, n - p_completo - 1)
print(f"Estatística F: {F_stat:.4f}")
print(f"p-value: {p_value:.4f}")
print("\nH0: preço e concorrentes não têm efeito conjunto")














































