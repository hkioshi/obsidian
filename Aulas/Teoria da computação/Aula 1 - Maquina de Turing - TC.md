u [[aula01_TC.pdf]]
# Tese de Church Turing - Sumario
- ## Maquina de Turing
- ## [[Aula 1.1 - MT Reconhecível - TC]] - [[Reconhecível - Conceito]]
- ## [[Aula 1.2 - Linguagem Turing-Decidível - TC]] - [[Decidível - conceito]]
- ## [[Aula 1.3 - Tese de Church Turing - TC]]
- ## Exercícios
# Maquina de Turing
- ## Definição formal
| Símbolo    | Definição                                                      |
| ---------- | -------------------------------------------------------------- |
| `Q`        | Conjunto de estados                                            |
| `Σ`        | Alfabeto de entrada, não contém o símbolo em branco (`␣`)      |
| `Γ`        | Alfabeto da fita, onde `␣ ∈ Γ` e `Σ ⊆ Γ`                       |
| `δ`        | Função de transição: `δ : Q × Γ → Q × Γ × {L, R}`              |
| `q₀`       | Estado inicial, onde `q₀ ∈ Q`                                  |
| `qₐcₑita`  | Estado de aceitação, onde `qₐcₑita ∈ Q`                        |
| `qᵣₑjₑita` | Estado de rejeição, onde `qᵣₑjₑita ∈ Q` e `qᵣₑjₑita ≠ qₐcₑita` |
- **Configuração Inicial**: A MT está no estado q0 com a cabeça de leitura situado na posição mais a direita da cadeia 
- **configuração de parada**: Um estado na qual a maquina está ou em estado de aceitação (configuração de aceitação) ou no estado de rejeição (configuração de rejeição):
	- configuração de aceitação: “$\large uq\tiny accept \large  v$” 
	- configuração de rejeição: “$\large uq\tiny reject \large  v$”





