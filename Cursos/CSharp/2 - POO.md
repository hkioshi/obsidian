
- # Classe
	- Variáveis
		- Tipo1 NomeDaVar1
		- ...
	- Construtor
		- NomeDaClasse(Tipo1 nome1, ... , tipoN nomeN)
			{
				this.NomeDaVar1 = nome1;
				.
				.
				.
				this.NomeDaVarN = nomeN;
				alguma outra coisa que vc queira fazer
			}
	- Métodos
		- Funciona como toda função
	- Destrutor
		- ~NomeDaClasse(){console.Write("objeto destruido")}

- # Objeto
	- Instancia de uma classe
	- sintaxe
		- NomeDaClasse nomeDoObjeto = new NomeDaClasse(argumentos do  construtor)
- # [[2.1 Herança]]
	- Herança é um conceito da programação orientada a objetos que permite que uma classe (chamada de classe derivada ou filha) herde características e comportamentos de outra classe (chamada de classe base ou pai). Isso significa que a classe derivada pode reutilizar código existente da classe base, estender funcionalidades e até mesmo substituir métodos da classe base, promovendo a reutilização e a hierarquia de código. Em essência, a herança facilita a criação de uma estrutura de classes mais organizada e flexível, permitindo que novos tipos sejam construídos a partir de tipos existentes com menor esforço.
- # [[2.2 Sobrecarga]]
	- Sobrecarga é a capacidade de definir múltiplos métodos com o mesmo nome, mas com diferentes listas de parâmetros, permitindo que o compilador escolha qual método chamar com base na assinatura do método.

- # [[2.3 Polimorfismo]]
	- Polimorfismo permite que objetos de diferentes classes sejam tratados através de uma interface comum, com métodos que podem ter comportamentos diferentes conforme a implementação da classe específica.
- # [[2.4 Encapsulamento]]
	- Encapsulamento é o princípio de ocultar os detalhes internos de uma classe e expor apenas uma interface pública para interagir com os dados e funcionalidades da classe.
- # Static
	- Palavra chave para colocar antes do tipo do metodo ou classe, serve para que a função funcione sem que voce tenha que estanciar um objeto 
- # Abstract
	-  Palavra chave para colocar antes do tipo do metodo ou classe, serve para que na classe ou funçao pai nao exista e deve ser criada para cada filho
- # [[2.5 GetSet]]
- # [[2.6 Interfaces]]
	- As interfaces em C# são contratos que definem métodos e propriedades que as classes devem implementar, garantindo consistência na aplicação.