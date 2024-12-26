![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![Github Pages](https://img.shields.io/badge/github%20pages-121013?style=for-the-badge&logo=github&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)

# Descrição do Projeto 📋

O projeto tem como objetivo demonstrar a integração entre diferentes tecnologias, incluindo o uso de APIs, armazenamento de dados em bancos de dados NoSQL (MongoDB) e relacionais (MySQL), além de apresentar visualizações de dados utilizando a biblioteca Matplotlib do Python.

# Objetivo do Projeto 🎯

O objetivo do projeto é praticar o uso de APIs e explorar o funcionamento de bancos de dados não relacionais, como o MongoDB, como alternativa aos bancos de dados relacionais. Além disso, o projeto visa integrar tecnologias modernas para o gerenciamento de ambiente, utilizando o Poetry, e para a documentação, com o MkDocs.

# 3. Tecnologias Utilizadas 💻

- Git
- Github Pages
- SQL
- DBeaver
- Python
- MongoDB Atlas
- MondoDB Compass

# 4. Descrição das Tecnologias no Projeto 📝

Para o projeto, foi criado um banco de dados não relacional utilizando o MongoDB 🗄️, com o servidor hospedado no MongoDB Atlas 🌐, uma plataforma de banco de dados como serviço que oferece uma solução escalável e gerenciada para armazenar dados em coleções. A conexão com o banco de dados foi realizada por meio da URI fornecida pelo Atlas, utilizando o MongoDB Compass 🧭, uma ferramenta GUI que facilita a administração e visualização dos dados armazenados no MongoDB. O Compass é bastante útil para explorar e consultar os dados de forma intuitiva, além de permitir a criação e modificação de coleções e índices.

No projeto, foi desenvolvido um script ETL (Extração, Transformação e Carga) 🔄 em Python 🐍 para extrair dados históricos de ações listadas na B3, a bolsa de valores brasileira 📈. O script foi responsável por realizar o tratamento e limpeza dos dados, como remoção de valores nulos 🚫, transformação de formatos de data 📅 e normalização de valores, antes de carregar as informações no banco de dados MongoDB. Para garantir uma organização eficiente, os dados de cada ação foram armazenados em coleções separadas 📊, permitindo uma estrutura bem definida e de fácil acesso.

Além do banco de dados não relacional, também foi criado um banco de dados relacional utilizando o MySQL 🛢️, que permite o armazenamento estruturado de dados em tabelas inter-relacionadas. Para interagir com o MySQL, foi utilizado o DBeaver 🖥️, uma ferramenta de administração de banco de dados muito poderosa e de fácil utilização. O DBeaver facilita a criação de consultas SQL 🔍, execução de scripts e visualização de dados, oferecendo recursos que aumentam a produtividade e reduzem erros ao lidar com bancos de dados relacionais.

Para o processamento e visualização dos dados, foi desenvolvido um segundo script em Python 🐍, que buscava os dados do banco de dados relacional MySQL, realizava o tratamento necessário e, em seguida, gerava um gráfico de linha 📊 utilizando a biblioteca Matplotlib 📈. O gráfico gerado permitiu comparar o desempenho de diferentes ações ao longo do tempo ⏳, facilitando a análise visual dos dados históricos. O Matplotlib é uma das bibliotecas mais populares para visualização de dados em Python, permitindo criar gráficos de diferentes tipos e personalizá-los conforme necessário.

Essa combinação de tecnologias — MongoDB Atlas e Compass 🌐🧭, Python 🐍, MySQL com DBeaver 🛢️🖥️ e Matplotlib 📊 — proporcionou uma solução robusta e eficiente para a extração, transformação, armazenamento e visualização de dados financeiros 💰, permitindo uma análise completa e interativa do comportamento das ações na bolsa brasileira 📈.

# 5. Exibição do Projeto 👁️

## 5.1 MongoDB Compass

### 5.1.1 Coleções criadas no MongoDB

![MongoDB Compass](/assets/img/mongodb_1.png)

### 5.1.2 Documentos armazenados dentro das coleções (GOLL4.SA)

![MongoDB Compass](/assets/img/mongodb_2.png)

### 5.1.3 Documentos armazenados dentro das coleções (MGLU3.SA)

![MongoDB Compass](/assets/img/mongodb_3.png)

## 5.2 DBeaver

### 5.2.1 Dados gravados no MySQL

![DBeaver](/assets/img/dbeaver_1.png)

### 5.2.2 Demonstrando todos os tickers

![DBeaver](/assets/img/dbeaver_2.png)

# 6. Visite a Documentação do Projeto

https://kjonnathas.github.io/DataLake_MongoDB

# 7. Instalação e Configuração 🔗

- Pré-requisitos:

  a. Criar uma conta gratuita no MongoDB Atlas;

  b. Baixar e instalar o MongoDB Compass;

  - Link para download: https://www.mongodb.com/try/download/compass

  c. Baixar e instalar o DBeaver;

  - Link para download: https://dbeaver.io/download/

  d. Baixar e instalar o MySQL;

  - Link para download: https://dev.mysql.com/downloads/mysql/

- Passo a passo:

1. Primeira coisa que precisamos fazer é instalar o python. Para isso, vamos utilizar o Pyenv que é um pacote que permite gerenciar diversas versões do Python na mesma máquina.

```bash
git clone https://github.com/pyenv-win/pyenv-win.git %USERPROFILE%\.pyenv
```

2. Após executar o comando acima, será criada uma pasta no seu usuário chamada .pyenv, que conterá todos os arquivos necessários para que o Pyenv possa funcionar. Agora, precisamos configurar variáveis de ambiente para que o sistema operacional consiga compreender os comandos do Pyenv no prompt de comando. Vá até a lupa de pesquisa e procure por "configurações avançadas do sistema". Em seguida, clique em "Variáveis de ambiente" e posteriormente clique em "Novo" na parte de variáveis do usuário. Após isso, abrirá uma janela para incluir o nome e o valor da variável de ambiente que está logo abaixo.

```bash
PYENV=C:\Users\seu_usuario\.pyenv\pyenv-win\
PYENV_HOME=C:\Users\seu_usuario\.pyenv\pyenv-win\
PYENV_ROOT=C:\Users\seu_usuario\.pyenv\pyenv-win\
```

3. Para ter certeza que o Pyenv está instalado e funcionando corretamente, abra o prompt de comando e digite:

```bash
pyenv --version
```

4. Se após a execução do código acima retornar a versão do Pyenv é porque o sistema operacional já está conseguindo compreender os comandos. Caso contrário, revise o passo a passo descrito e se for necessário busque ajuda no Google. Por conseguinte, agora com as configurações necessárias, precisamos instalar o Python através do Pyenv.

```bash
pyenv install 3.12.1
```

5. Com o Python instalado, precisamos agora clonar o projeto. Caso queira manter o projeto em uma pasta específica, você pode navegar através da estrutura de pastas do seu notebook/computador com o comando "cd nome_pasta". Se não especificar a pasta, provavelmente o projeto será criado na sua pasta de usuário.Feito isso, digite:

```bash
https://github.com/Kjonnathas/DataLake_MongoDB.git
```

6. Com o projeto clonado, precisamos especificar a versão do python que irá rodar no projeto. Para isso, execute o seguinte comando dentro da pasta do projeto:

```bash
pyenv local 3.12.1
```

7. Exclua o arquivo "pyproject.toml" da pasta;

8. Agora precisamos criar um ambiente virtual e para isso vamos utilizar o poetry que é uma ótima ferramenta para gerenciamento de ambientes virtuais. Navegue até a pasta do projeto, no caso a pasta "DataLake_MongoDB" e depois digite:

```bash
poetry init
```

9. O comando acima inicializará um projeto poetry na sua pasta, inclusive com a criação do arquivo "pyproject_toml". Na sequência, digite:

```bash
poetry shell
```

10. Novamente, o comando acima serve para entrar no ambiente virtual do poetry e isolar as instalações do seu projeto. Vamos seguir... Agora, digite:

```bash
poetry add pymongo python-dotenv yfinance pandas pyodbc matplotlib
```

11. O comando acima fará a instalação de todas essas bibliotecas. Com as bibliotecas instaladas, praticamente fechamos as configurações necessárias e podemos seguir com o andamento do projeto.

12. Ah, não podemos esquecer de criar o arquivo ".env" onde estarão armazenadas todas as nossas variáveis de ambiente. Essa parte é muito importante e sem ela o projeto não funciona. Portanto, faça o seguinte:

    - Crie um arquivo chamado ".env", sem as aspas;

    - Neste arquivo você terá que incluir as seguintes variáveis:

    - MONGO_URI=coloque_sua_uri_aqui
    - MONGO_DATABASE=ACOES
    - MYSQL_DRIVER={MySQL ODBC 8.0 Unicode Driver}
    - MYSQL_SERVER=localhost
    - MYSQL_DATABASE=db_acoes
    - MYSQL_USERNAME=root
    - MYSQL_PASSWORD=coloque_sua_senha
    - LOG_PATH=coloque_o_caminho_completo_da_pasta_de_log
    - IMG_PATH=coloque_o_caminho_completo_da_pasta_img

13. Ao criar a conta no MongoDB Atlas escolha a opção de ter um servidor free. Depois disso, será fornecida uma URI de conexão para seu servidor. É importante guardar essa URI para podermos conectar no MongoDB Compass, pois não estaremos nos conectando na máquina local que é o localhost. O servidor está hospedado na AWS pelo MongoDB Atlas.

14. Abra o seu MongoDB Compass e faça a conexão utilizando a sua URI. Não será necessário criar o banco de dados e nem as coleções, pois serão criadas em tempo de execução ao rodar o script "main.py".

15. Agora abra o seu DBeaver e clique em um botão logo abaixo da aba "Arquivo". Abrirá o dropdown e selecione "Nova Conexão". Escolha a opção "MySQL" e clique em avançar. Por padrão já vai vir com o nome do host como localhost, a porta como 3306 e o nome de usuário como root. Sendo assim, apenas insira a sua senha que foi definida ao baixar e instalar o mysql e clique em avançar.

16. Neste momento, com todas as configurações feitas e todos os client já configurados, vamos executar os dois scripts python que fazem a mágica acontecer. Portanto, navegue até a pasta src e digite:

```bash
python main.py
```

17. Depois que o código acima finalizar a execução, verique no MongoDB Compass se os dados foram carregados fazendo um refresh e também verifique no DBeaver se os dados foram carregados na tabela, neste caso basta apenas clicar com o botão direito sobre o banco de dados e selecionar a opção "Editor SQL" e em sequência "Novo script SQL". Depois disso, com o editor aberto, você pode usar o seguinte código SQL para visualizar os dados `SELECT * FROM db_acoes.tbl_historico_acoes;` e clicar no botão de run ao lado ou selecionar o código e "CRTL + ENTER".

18. Se tudo estiver carregado com sucesso, agora vamos executar o outro script que buscará os dados no MySQL, gerará um gráfico de linhas comparando duas ações ao longo do tempo e, por fim, salvará uma imagem png desse gráfico. Então, digite:

```bash
python graph_viewer.py
```

8. Licença

Este projeto está licenciado sob os termos da licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
