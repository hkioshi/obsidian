[Codigo](https://colab.research.google.com/drive/1hz72aSEDBkJmwkxVOvv8lxRfysx89FUQ#scrollTo=LFCTOeaOVIX8)
[Aula-Slide](https://dados.crivelaro.me/07-correlacao-regressao.html#/title-slide)
# Inferência Estatística
## Correlação de Pearson
- 2 variáveis continuas
- $$ r = \frac{\sum_{i=1}^{n} (X_i - \overline{X})(Y_i - \overline{Y})}{\sqrt{\sum_{i=1}^{n} (X_i - \overline{X})^2 \sum_{i=1}^{n} (Y_i - \overline{Y})^2}} $$
	- $X_i$ e $Y_i$ são valores individuais de $X_i$ e $Y_i$
	- $\overline{X}$ e $\overline{Y}$ são as médias
-  Em outras palavras, ele ajuda a entender como uma variável muda quando a outra muda, supondo uma relação linear entre ela
- O coeficiente de correlação de Pearson varia de -1 a 1, onde:
	- -1 indica uma correlação negativa perfeita: quando uma variável aumenta, a outra diminui proporcionalmente.
	- 0 indica nenhuma correlação linear: as variáveis não estão relacionadas linearmente.
	- 1 indica uma correlação positiva perfeita: quando uma variável aumenta, a outra também aumenta proporcionalmente.
	- Posso saber relacionamento de duas variáveis
	- Uma pode ser fácil de medir, mas quero saber da outra

# Correlação Spearman
- Para variáveis com ordenação
- Distribuição é não paramétrica
## Correlação de Cramer V
- Para variáveis categóricas
- Exemplo: avaliar se existe associação entre o gênero (masculino/feminino) e a escolha de um tipo de carro (sedan, SUV, hatchback, etc.)
## Regressão Linear
- Método estatístico usado para modelar a relação entre uma variável dependente e uma ou mais variáveis independentes.
- A forma mais simples de regressão linear é a regressão linear simples, que envolve apenas uma variável independente.
- ### Regressão Linear Simples
	- Na regressão linear simples, o objetivo é encontrar a melhor linha reta que descreva a relação entre duas variáveis.
	- A equação desta linha é geralmente expressa como:
$$Y=β0+β1∗X+ϵ$$
## Cálculo dos coeficientes
$$
\overline{x} = \frac{\sum_{i=1}^{n} x_i}{n}, \quad \overline{y} = \frac{\sum_{i=1}^{n} y_i}{n}
$$

$$
\beta_1 = \frac{\sum_{i=1}^{n} (x_i - \overline{x})(y_i - \overline{y})}{\sum_{i=1}^{n} (x_i - \overline{x})^2}
$$

$$
\beta_0 = \overline{y} - \beta_1 \overline{x}
$$
![[Pasted image 20240923195448.png]]
