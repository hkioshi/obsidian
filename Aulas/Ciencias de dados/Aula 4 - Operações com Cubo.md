[slides](https://dados.crivelaro.me/04-operacoes-cubo.html#/title-slide)
![[Pasted image 20240905160132.png]]
### 1. **Drill Down** [[Aula 4.1 - Drill-down - CD]]
- **Descrição:** Imagine que você está olhando para um cubo de dados e vê apenas a face que mostra as vendas anuais. "Drill down" é como girar o cubo para revelar uma nova face que mostra os dados detalhados por mês.
- **Exemplo:** Se o cubo mostra vendas totais para 2023, ao fazer um "drill down", você vê uma face que detalha essas vendas por cada mês de 2023.

### 2. **Roll Up** [[Aula 4.2 - Roll-Up - CD]]
- **Descrição:** Agora, imagine que você está examinando uma face do cubo que mostra as vendas diárias. "Roll up" é como empilhar essas faces para ver uma visão geral mais alta, como as vendas agregadas por mês ou por ano.
- **Exemplo:** Ao fazer "roll up" a partir das vendas diárias, você vê a face do cubo que mostra as vendas agregadas por mês ou por ano.

### 3. **Slice** [[Aula 4.3 - Slice -CD]]
- **Descrição:** Imagine que você está cortando uma fatia do cubo para visualizar apenas uma seção específica. "Slice" é como cortar o cubo ao longo de uma dimensão, mantendo as outras dimensões intactas.
- **Exemplo:** Se você cortar o cubo para focar apenas no ano de 2023, você vê uma face que mostra apenas os dados de 2023, ignorando outros anos.

### 4. **Dice** [[Aula 4.4 - Dice - CD]]
- **Descrição:** "Dice" é como pegar uma seção específica do cubo que se cruza em várias direções. Imagine cortar o cubo em vários eixos para visualizar uma fatia específica que inclui várias dimensões.
- **Exemplo:** Se você cortar o cubo para mostrar vendas específicas de 2023 e apenas para determinados produtos, você está "dicing" para ver apenas a interseção dessas condições.

### 5. **Pivot** [[Aula 4.5 - Pivot - CD]]
- **Descrição:** "Pivot" é como girar o cubo para ver diferentes perspectivas. Imagine que você gira o cubo para transformar uma face em outra, reorganizando as dimensões para obter uma nova visualização.
- **Exemplo:** Se você começar com uma face que mostra vendas por ano e deseja ver vendas por produto, você "pivot" o cubo para reorganizar os dados de acordo com os produtos e anos.
### 6. Como fazer no PostgreSQL [[Aula 4.6 - Operações de Cubo em PostgreSQL - CD]]
