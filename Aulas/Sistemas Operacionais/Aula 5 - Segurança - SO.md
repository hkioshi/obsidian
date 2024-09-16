fontes: [[cap08.pdf]], [[cap09.pdf]] - São de 2 livros diferentes
# O que é segurança 
- Confidencialidade -
	- Apenas o remetente e o destinatário pretendido devem entender o conteúdo da mensagem
	- Remetente criptografa a mensagem
	- Destinatário descriptografa a mensagem
- Autenticação 
	- remetente e destinatário tenham a confirmação da identidade um do outro 
- Integridade da mensagem
	- Garantir que a mensagem esta inalterada
- Acesso e disponibilidade
	- Os serviços devem estar acessíveis e disponíveis ao usuário
 - Obs1: Cifragem $\neq$ Criptografia
	- Mensagem em outras letras
	- Esconder o significado da mensagem
- Obs2: 

# Criptografia Básica
- ![[Pasted image 20240913194156.png]]
# Amigos e Inimigos
- ![[Pasted image 20240913200608.png]]
- ## Quem seriam Bob e Alice? 
	- bem, Bobs e Alice da vida real! 
	- navegador/servidor da Web para transações eletrônicas (por exemplo, compras online) 
	- cliente/servidor de banco online 
	- servidores DNS 
	- roteadores BGP trocando atualizações da tabela de roteamento 
	- outros exemplos?
- ## Inimigos
	- O que invasores podem fazer
	- Bisbilhotar(eavesdrop)
	- Inserir
	- Personificação
		- Falsificar (Spoof) o endereço de origem no pacote
	- Sequestro(hijiacking)
		- "Assumir" a conexão em andamento, removendo o remetente ou o destinatário
	- Negação de serviço(Denial of service)

# Quebrando um esquema de criptografia
- Ataque apenas de texto
	- Trudy tem texto cifrado que ela pode analisar
- Duas abordagens
	- Força Bruta 
	- Analise estatística
- ataque de texto simples conhecido
	- Trudy tem texto simples correspondente ao texto cifrado
- ataque de texto simples escolhido
	- Trudy pode obter texto cifrado para texto simples escolhido

# Chave Simétrica
![[Pasted image 20240913201231.png]]
- A mesma chave
- Texto simples $\Rightarrow$ Algoritmo de criptografia(chave K) $\Rightarrow$ mensagem $\Rightarrow$ Algoritmo de descriptografia(chave K) $\Rightarrow$  Texto simples 
- Esquema de criptografia simples
	- Substituindo uma coisa por outra
		- Monoalfabética: substitui uma letra por outra
			- P.ex.:  a $\Rightarrow$ x, b $\Rightarrow$ z, ...
- Como eles concordam com o valor da chave
	- ![[Pasted image 20240913203157.png]]
	- **Diffie-Hellman**
# Criptografia de chave simétrica: 
- DES Security: 8- 18 DES: Data Encryption Standard padrão de criptografia dos EUA [NIST 1993] 
	- chave simétrica de 56 bits, entrada de texto simples de 64 bits
	- cifra de bloco com encadeamento de bloco de cifra
	- Quão seguro é o DES? Desafio do DES:
		- frase criptografada com chave de 56 bits descriptografada (força bruta) em menos de um dia 
		- nenhum bom ataque analítico
	- conhecido tornando o DES mais seguro: 3DES: 
		- criptografar 3 vezes com 3 chaves diferentes
- AES: Advanced Encryption Standard
	- padrão do NIST de chave simétrica, substituiu o DES (novembro de 2001)
	- processa dados em blocos de 128 bits
	- chaves de 128, 192 ou 256 bits
	- descriptografia de força bruta (tentar cada chave) em uma máquina que levaria 1 segundo com o DES, levaria 149 trilhões de anos com o AES
# Algoritmos de criptografia de chave publica
- ![[Pasted image 20240913211551.png]]
- ![[Pasted image 20240913211622.png]]
- ## RSA: se preparando
	- mensagem: apenas um padrão de bit
	- um padrão de bits pode ser representado por um número inteiro único
	- assim, criptografar uma mensagem é equivalente a criptografar um número
	- exemplo:
		- m= 10010001. Esta mensagem é representada exclusivamente pelo número decimal 145.
		- para criptografar m, criptografamos o número correspondente, que fornece um novo número (o texto cifrado).
- Por que o RSA é seguro? 
	- Security: 8- 32 suponha que você conheça a chave pública de Bob (n,e). Quão difícil é determinar d? 
	- essencialmente é necessário encontrar fatores de n sem conhecer os dois fatores p e q 
		- fato: fatorar um número grande é difícil
	- Vc quer um algoritmo lento para atrapalhar força bruta
# Autenticação
 - [[Aula 5.1 - Autenticação - SO]]

# Esteganografia 
- é a técnica de ocultar informações dentro de outros arquivos, como imagens, vídeos ou áudio, de modo que a presença da informação seja imperceptível.



