# Blog de Receitas com Django

Uma aplicação de blog simples para compartilhar e visualizar receitas, construída com Django.

## Funcionalidades

* Visualizar uma lista de receitas.
* Ver os detalhes de uma receita específica, incluindo ingredientes e instruções.
* Interface de administração para gerenciar receitas (adicionar, editar, excluir).

## Começando

Estas instruções permitirão que você obtenha uma cópia do projeto em funcionamento em sua máquina local para fins de desenvolvimento e teste.

### Pré-requisitos

* Python 3.8+
* Pip (instalador de pacotes Python)

### Instalação

1. **Clone o repositório:**
   ```sh
   git clone https://github.com/seu-usuario/django-blog-recipes.git
   cd django-blog-recipes
   ```

2. **Crie e ative um ambiente virtual:**
   ```sh
   # Para Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Para macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   *(Nota: Um arquivo `requirements.txt` ainda não está presente no projeto. Você deve criar um usando `pip freeze > requirements.txt` após instalar o Django)*
   ```sh
   pip install Django
   ```

4. **Aplique as migrações do banco de dados:**
   ```sh
   python manage.py migrate
   ```

5. **Crie um superusuário para acessar o painel de administração:**
   ```sh
   python manage.py createsuperuser
   ```
   Siga as instruções para criar um nome de usuário, email e senha.

6. **Execute o servidor de desenvolvimento:**
   ```sh
   python manage.py runserver
   ```
   A aplicação estará disponível em `http://127.0.0.1:8000/`.

## Uso

* Acesse o site principal em `http://127.0.0.1:8000/` para ver a lista de receitas.
* Acesse o painel de administração em `http://127.0.0.1:8000/admin/` para fazer login и gerenciar as receitas.

## Construído Com

* [Django](https://www.djangoproject.com/) - O framework web utilizado
* [Python](https://www.python.org/) - A linguagem de programação

## Licença

Este projeto está licenciado sob os termos do arquivo LICENSE.