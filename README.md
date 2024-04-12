## 🛒 API Python para Controle de Carrinho de Compras

Repositório para o case técnico do Mercado Livre.
API capaz de gerar dados para controlar o fluxo de um carrinho de compras, permitindo:

- Listar todos os produtos
- Adicionar itens ao carrinho
- Listar os produtos adicionados ao carrinho

## 🛠️ Tecnologias

Esse projeto foi desenvolvido com as seguintes tecnologias:

- [Python](https://www.python.org/) - Linguagem de programação.
- [Docker](https://docs.docker.com/) - Plataforma de software para automação de implantação e execução de aplicativos em ambientes isolados chamados containers.

  ### 🧪 Testes

  - [Unittest](https://docs.python.org/3/library/unittest.html) - Módulo de teste unitário padrão do Python, projetado para automatizar testes de unidades individuais de código.

## 🚀 Como executar

Clone o projeto e acesse a pasta do mesmo.

```bash
$ git clone ...
```

Para iniciar o projeto, siga as instruções abaixo:

# Windows

#### 💻 Executar com pip install

```bash
# Instalando dependências do projeto
$ python -m venv venv
$ venv/scripts/activate
$ pip install -r requirements.txt

# Rodar o projeto
$ uvicorn main:app --reload
```

#### 🐳 Executar com Docker

```bash
# Construa a imagem Docker:
$ docker build -t carrinhocomprasbackend:latest .

# Execute o contêiner Docker:
$ docker run -d -p 8000:8000 carrinhocomprasbackend
```

- ###### O Swagger estará acessível em http://localhost:8000/docs.
