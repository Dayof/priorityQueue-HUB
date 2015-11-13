# Priority Queue

## Sumário

1. Descrição
2. Dados do projeto
3. Instalação
4. Execução

## Conteúdo

### 1. Definição

Trabalho final da matéria de Sistemas de Informação, turma B, ministrada pelo professor Edison Ishikawa do Departamento de Ciência da Computação da Universidade de Brasília.

### 2. Dados do projeto

Título do projeto:
Priority Queue

Professor:
Edison Ishikawa

Departamento: Departamento de Ciência da Computação

Equipes:
* Cadastro de registros e entidades - 1
* Fila de prioridade - 2

Alunos Envolvidos:
* Equipe 1:
  * Carlos Trufini
    * Matrícula: ipox@live.com
    * E-mail: 
  * Matheus Vieira
    * Matrícula: 
    * E-mail: matheusvf1234@gmail.com
  
* Equipe 2:
  * Dayanne Fernandes
    * Matrícula: 13/0107191
    * E-mail: dayannefernandesc@gmail.com
  * Orlando 
    * Matrícula:
    * E-mail: ojfsilva@uol.com.br

### 3. Instalação

Siga as instruções abaixo.

1. Clone o repositório com: 
  `git clone https://github.com/Dayof/priorityQueue-HUB.git`

2. Para instalar o python no Windows:
  [Siga este tutorial](http://docs.python-guide.org/en/latest/starting/install/win/).

3. Para instalar o python no Linux:
> OBS: As últimas versões do Ubuntu e Fedora já vêm com o python 2.7 e as últimas versões do RHEL e CentOS já vêm com o python 2.6.

  * Instale o pip:
    `$ easy_install pip`
  * Instale o virtualenv:
	`$ pip install virtualenv`
  * Selecione o diretório para a instalação do python e execute o virtualenv.
	`$ virtualenv --distributte venv`
  * Para executar o ambiente, rode:
	`$ source venv/bin/activate`
  * Para sair do ambiente:
	`$ deactivate`

4. Para instalar django no Windows:
  * Baixe [Download Django-1.7.1.tar.gz](https://www.djangoproject.com/download/1.7.1/tarball/). Então extraia o arquivo, inicie o DOS
 shell (ctrl+E, cmd) com permissão de administrador e execute o comando no diretório cujo nome inicie com "Django-":
	`$ python setup.py install`

5. Para instalar django no Ubuntu:
  * Pelo pip:
	`$ pip install Django==1.7`
  * "Manualmente":
	* Baixe [Download Django-1.7.1.tar.gz](https://www.djangoproject.com/download/1.7.1/tarball/). Então:
		`$ tar xzvf Django-1.6.2.tar.gz`
		`$ cd Django-1.6.2`
		`$ sudo python setup.py install`

### 4. Execução

Para executar o server pela primeira vez, acesse a pasta HUBqueue dentro da pasta do projeto do git, vá ao terminal e execute os seguinte comandos:
  `python manage.py migrate`
  `python manage.py runserver`


