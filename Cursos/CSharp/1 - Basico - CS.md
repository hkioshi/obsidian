
 - #console
	 - console.Writeline("ola mundo");
	 - console.Write("ola mundo") - nao pula linha
	 - console.Read()
 - [[1.1 Tipos cs]]
	 - int.
	 - String
		 - [[1.1.2 Raw String]]
		 - [[1.1.3 Metodos de string]]
	 - bool
	 - char
	 - float
	 - double 
	 - decimal
	 - var
	 - const
		 - const var nome // a variavel nome é constante
	 - [[1.1.1 Typecast]]
		 - Typecasting em C# é o processo de converter um valor de um tipo de dados para outro. Existem dois tipos principais de typecasting: explícito e implícito
 - #Comentário
	 - //comentário
 - Interpolação
	 - $" o valor da variavel é {variavel}"
 - [[1.2 Operaçoes]]
	 - Operações Matemáticas
		- `+ - * / % ++ --`
	- Operações Lógicas
		- `&& || !`
	- Operações de Comparação
		- `== != > < >= <=`
	-  Operações Bitwise
		- `& | ^ ~ << >>`
- [[1.3 Condição]]
	- if, else e ifelse
	- #operador_ternário
		- condicao ? valorSeVerdadeiro : valorSeFalso;
- [[1.4 Repetição]]
	- for, foreach, while, do-while
- [[1.5 Switch case]]
	- A instrução `switch` em C# é uma estrutura de controle de fluxo que executa diferentes blocos de código com base no valor de uma expressão, facilitando a substituição de múltiplas instruções `if-else`
- Goto
	-  coisa:
			código
			goto coisa - vai para o inicio de coisa
- Funções
	- (coisas antes como: public, static, etc) tipoDoRetorno NomeDaFuçao(TipodoParam nome )
		{
			codigo
			return ; // se o tipo do retorno nao for void
		}
	* [[1.6 Parametros Especiais]]
		* Params - parametros ilimitados
		* ref e out -  ponteiros
	* [[1.7 lambda]]
		* Lambda é uma expressão que define uma função anônima com parâmetros e uma expressão ou bloco de código.
	* Locais
		* Pode fazer funçoes dentro de funçoes
	* Sobrecarga de funções
		* Funçao com mesmo nome e numero ou tipo de parametros diferentes
		* (coisas antes como: public, static, etc) tipoDoRetorno NomeDaFuçao(TipodoParamDiferenteDoPrimeiro nome )
		{
			codigo
			return ; // se o tipo do retorno nao for void
		}
- [[1.8 Enums]]
	- Uma enumeração (enum) em C# é um tipo de valor que define um conjunto de constantes nomeadas, representando valores inteiros subjacentes, facilitando a leitura e a manutenção do código.
- [[1.9 delegates&Events]]
	- **Delegates:** Delegates em C# são tipos que representam referências a métodos, permitindo que métodos sejam passados como parâmetros e chamados dinamicamente.
	- **Events:** Events em C# são um mecanismo que permite que uma classe forneça notificações quando algo interessante acontece, utilizando delegates para gerenciar a lista de assinantes.
- [[1.10 Erros]]
	- Como tratar erros
- [[1.11 Assincrono]]
# [[2 - POO]] 
