# Hipervisor
- Sistema de virtualização, emular outro computador
- Virtual Box
	- Tipo 1 - Direto no computador
	- TIpo 2 - Em Cima de um Sistema operacional

# Para que serve um so(vai cair)
- Gerenciamento de recursos
	- Processamento 
	- Memoria
	- IO
- O sistema operacional gera uma abstração do hardware, 
	- Abrir pastas
	- Graficos

# Sistema Operacional é Hardware ou Software
- Software
- Usa CPU

Arquitetura - o q enxerga

acessos indevidos, Estruturas do SO


# Minix
# BSD
- Sistema operacional de codigo aberto, pegue esse codigo e faça oque vc quiser
- Base 
- FreeBSD

# instalar alpine
Passo 1 - Instalar o virtualBox certo
	https://www.virtualbox.org/wiki/Downloads
	Windows hosts
Passo 2 - Colocar nome, A iso do Alpine, Na versão coloque Other Linux(64-Bits)
--Próximo--
Passo 3 - colocar Memoria, Processadores, Tamanho do disco
--finaliza--

Nas configurações
	No sistema coloque Disco Rigido em primeiro, Ópico em segundo e desliga o disquete
	No áudio desabilita áudio
	O resto deixa como esta

Abre a Maquina
	Coloca o nome do root
	setup-alpine
	Keymap: br
	variant: br
	Coloca o hostname
	interface: eth0 (so apertar enter)
	Ip address: dhcp (so apertar enter)
	configuração manual?:n (so apertar enter)
	coloque a senha do root
	Timezone: America/
	Onde vc esta?: Sao_Paulo
	Proxy: none (so apertar enter)
	APK Mirror: 39
	Coloque o nome do user(letras minusculas)
	Coloque nome completo
	Coloque a senha do usuário
	ssh server: openssh (so apertar enter)
	Qual disco?: sda
	Como gostaria de usar?: sys
	Erase the above disk? y
	
Pronto :D