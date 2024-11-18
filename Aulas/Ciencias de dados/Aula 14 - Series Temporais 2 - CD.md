Modelos de series temporais
- Objetivo: Ajuda a analisar e prever dado que dependem do temporais
- Tipos: Desde estatísticos clássicos ate técnicas de machine learning e deep learning

- **Definição**: Uma série temporal é estacionária se suas propriedades estatísticas (média, variância, autocorrelação) não mudam ao longo do tempo.
- **Características principais**:
    - **Média constante**: a média não varia com o tempo.
    - **Variância constante**: a dispersão dos valores permanece a mesma ao longo do tempo.
    - **Autocorrelação constante**: a correlação entre valores próximos é a mesma em qualquer período.
- **Importância**: Muitos modelos de séries temporais (como ARIMA) assumem que a série é estacionária para funcionar corretamente.

## Testes para Detectar Estacionariedade

- **1. Análise Visual**:
    - Plotar a série para observar se a média e variância parecem constantes.
- **2. Gráfico de Autocorrelação (ACF)**:
    - Em uma série estacionária, a autocorrelação diminui rapidamente, enquanto uma série não estacionária apresenta autocorrelação persistente.
- **3. Teste de Dickey-Fuller Aumentado (ADF)**:
    - Teste estatístico usado para verificar a presença de uma raiz unitária (não estacionariedade).
    - **Hipóteses**:
        - H0H0: A série não é estacionária (tem uma raiz unitária).
        - HaHa: A série é estacionária.
    - **Interpretação**: Se o p-valor é baixo (< 0,05), rejeitamos H0H0 e consideramos a série estacionária.

## Transformações para Tornar uma Série Estacionária

- **Diferenciação**: Subtrair o valor anterior do atual para remover a tendência.
- **Transformação Logarítmica**: Reduz a variabilidade em séries com crescimento exponencial.
- **Suavização**: Média móvel e suavização exponencial para reduzir flutuações.
- **Exemplo**: Aplicar diferenciação em uma série de vendas pode ajudar a estabilizar a média e torná-la estacionária.
- [Codigo](https://colab.research.google.com/drive/1xAazExG9e9S4q-DX3cmEbt6XiRsq_bKx#scrollTo=mDvIMxNasVDt)
## Modelo de Média Móvel (MA)

- **Definição**: O valor atual da série é uma média ponderada dos erros passados.
- **Fórmula**: Yt=μ+∑qi=1θiεt−iYt=μ+∑i=1qθiεt−i
- **Uso**: Captura o efeito de flutuações passadas; útil para séries estacionárias.
- **Limitações**: Não modela a tendência ou sazonalidade.

## Modelo Auto-Regressivo (AR)

- **Definição**: O valor atual é uma função dos valores passados da série.
- **Fórmula**: $Yt=ϕ1Yt−1+ϕ2Yt−2+⋯+ϕpYt−p+εtYt=ϕ1Yt−1+ϕ2Yt−2+⋯+ϕpYt−p+εt$
- **Uso**: Adequado para séries onde o valor depende das observações anteriores.
- **Limitações**: Não lida bem com sazonalidade ou séries não estacionárias.
## Modelo ARIMA (Auto-Regressivo Integrado de Média Móvel)

- **Extensão do ARMA**: Inclui um componente de integração para lidar com séries não estacionárias.
- **Fórmula**: Yt=ϕ(B)Yt−1+θ(B)εtYt=ϕ(B)Yt−1+θ(B)εt
- **Parâmetros**: (p, d, q) onde d é a ordem de diferenciação.
- **Uso**: Amplamente utilizado para séries com tendência.

## Modelo SARIMA (Sazonal ARIMA)

- **Extensão do ARIMA**: Adiciona componentes sazonais para séries com padrão sazonal.
- **Parâmetros**: (p, d, q)(P, D, Q, s) onde s é o período da sazonalidade.
- **Uso**: Adequado para séries temporais com padrões de sazonalidade complexos.

## Modelo de Suavização Exponencial Simples

- **Definição**: Dá mais peso às observações mais recentes.
- **Fórmula**: Ft=αYt−1+(1−α)Ft−1Ft=αYt−1+(1−α)Ft−1
- **Uso**: Simples e útil para previsões de curto prazo em séries sem sazonalidade.

## Modelos de Machine Learning: Regressão Linear e Árvores de Decisão

- **Regressão Linear**: Modela uma relação linear entre o tempo e a variável dependente.
- **Árvores de Decisão**: Divide a série em segmentos com características distintas.
- **Uso**: Para séries com padrões não lineares ou dependências complexas.

## Modelos de Redes Neurais (RNN e LSTM)

- **RNN (Rede Neural Recorrente)**: Especializada em dados sequenciais.
- **LSTM (Long Short-Term Memory)**: Resolve problemas de longa dependência em séries temporais.
- **Uso**: Padrões complexos e não lineares em grandes volumes de dados.

[](https://dados.crivelaro.me/17-modelos-series-temporais.html#)