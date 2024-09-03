# Interfaces
- Modo Texto
	- CLI
	- TUI
- Grafica
	- GUI
	- WEB
# -Letra(Opções do comando)
- exemplos
	- ls ==-l==
	- ls ==-h==
	- ls -lh = ls -l -h (-Opçao1, Opçao2)
- ## Formato Longo da opção
	- --Comando
	- p.ex. ls --all

# ls - Lista de diretórios - [Site](https://www.rapidtables.com/code/linux/ls.html)
- Sintaxe( \[Opcional])
	- ls \[Opções]... \[Arquivos(Parâmetros)]...
- -l - Formato longo de lista
- -h - Legível por humanos
- -a, --all, m, M, ...

# exit - Sai 
# whoami - Nome do usuário

# Shell(Terminal -> Sistema operacional)

# Padrao de hierarquia de arquivo []()
- / - Diretorio raiz
	- ## Exemplos
		- /Pasta1/arquivo1
- Pasta Essenciais
	- /bin - Binários essenciais, Todos usuários(Programas essenciais)
	- /boot - Arquivos necessários ao processo de inicialização, incluindo o disco RAM inicial e o Kernel do Linux
	- /dev - Arquivos de dispositivos, dispo físicos conectados, ou virtuais fornecidos pelo kernel
	- /etc - Todos os arquivos de configuração
	- /home - Cada usuários recebe um diretório inicial para armazenar arquivos pessoais
	- /lib - bibliotecas necessárias para iniciar o sistema operacional e executar os binários que estão no /bin e /sbin
	- /media - Arquivo para externos, pendrive, pdfs
	- /mnt - arquivo para montagem para arquivos de montados temporariamente
	- /opt - Pacotes de software opcionais
	- /root - Pasta do usuário root
	- /run - Dados variáveis de tempo de execução
	- /sbin - binário para o root
	- /srv - Dados de serviço fornecidos pelo sistema
	- /tmp - arquivos temporários, pasta virtual relacionada a memoria Ram
	- /usr - Dados de usuário, apenas para leitura e 
	- /proc - buraco de fechadura para o kernel do Linux
	- /var - Dados que vao crescendo ao longo do tempo, p. ex. Logs

# cd - entrar e sair dos diretorios
- . - no lugar 
	- cd .
- .. - na diretorio anterior
- cd caminho do arquivo
- which -  um comando que é usado para localizar o arquivo executável associado ao comando fornecido pesquisando-o na variável de ambiente path

# su - Acesso a super usuario
# apk add gcc - baixa o bcc