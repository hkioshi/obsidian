[OsDev-MBR](https://wiki.osdev.org/MBR_(x86))
# Bios/Mbr
- BIOS/MBR é uma combinação de firmware (BIOS) e esquema de particionamento (MBR) usada em sistemas mais antigos para inicializar o sistema operacional. A BIOS carrega o MBR, que contém o bootloader e as informações das partições do disco, limitando-se a 2 TB e até 4 partições primárias.
# Partições Linux 
- São divisões lógicas do disco rígido usadas para organizar e gerenciar o armazenamento de dados, como a partição de sistema
- swap 
	- memoria de troca
- Linux tem 4 partições
	- Partição estendida (partições dentro de partições)
		- partições primaria, uma delas, partição estendida
		- Pode ter 1 a 4 primarias, 1 delas pode ser estendidas e dentro quantas partições forem necessárias

# Como instalar o arc_linux
- no vb colocar 
	- nome, a iso, tipo deve ser linux, versao deve ser arcLinux(64x)
	- senha do root: senha
	- usuario e senha: hkioshi