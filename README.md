# Sistema Educacional

Sistema web desenvolvido com **Python, Django e Django REST Framework** para uma empresa do setor educacional, permitindo o cadastro, gerenciamento e consulta de alunos, cursos e produtos, além da disponibilização de dados por meio de uma API REST.

O projeto foi desenvolvido como parte das Experiências de Aprendizagem do curso de Análise e Desenvolvimento de Sistemas, sendo construído incrementalmente a cada etapa.

## Tecnologias utilizadas

- Python
- Django
- Django REST Framework
- SQLite
- HTML5
- Git e GitHub

## Funcionalidades

### Alunos e cursos — EA1

- Cadastro de alunos com nome, sobrenome e e-mail.
- Cadastro de cursos com título e descrição.
- Relacionamento entre alunos e cursos (muitos-para-muitos).
- Gerenciamento de alunos e cursos pelo Django Admin.
- Listagem de alunos cadastrados.
- Listagem de cursos cadastrados.
- Exibição dos cursos em que cada aluno está matriculado.

### Produtos — EA2

- Modelo Produto com nome, descrição, preço e validade.
- Formulário próprio para cadastro de produtos, sem depender do Django Admin.
- Validação dos dados do formulário.
- Cadastro e armazenamento de produtos no banco de dados.
- Exibição da data de validade no formato brasileiro (dd/mm/aaaa).
- Listagem dos produtos cadastrados.
- Gerenciamento de produtos pelo Django Admin.

### API e integração de dados — EA3

- Integração do Django REST Framework ao projeto.
- Criação do modelo Usuario, com os campos nome e e-mail.
- Cadastro e armazenamento de usuários no banco de dados SQLite.
- Gerenciamento dos usuários pelo Django Admin.
- Criação do UsuarioSerializer utilizando ModelSerializer para converter os objetos do modelo em JSON.
- Implementação da UsuarioListAPIView utilizando ListAPIView.
- Disponibilização de um endpoint para consulta dos usuários cadastrados.
- Retorno dos dados por meio de requisições HTTP GET, no formato JSON.

**Endpoint da API:**

`GET /api/usuarios/`

Endereço local:

http://127.0.0.1:8000/api/usuarios/

A API retorna os usuários cadastrados no banco de dados, incluindo seus identificadores, nomes e e-mails.

**Exemplo de resposta JSON:**

```json
[
    {
        "id": 1,
        "nome": "Carlos",
        "email": "carlos@email.com"
    },
    {
        "id": 2,
        "nome": "João",
        "email": "joao@email.com"
    }
]
```

**Observação sobre JWT:** o funcionamento da autenticação baseada em JSON Web Token (JWT) foi estudado na parte teórica da EA3. A implementação prática desta etapa consiste na disponibilização da API para consulta dos usuários, sem autenticação JWT.

### Navegação e estrutura

- Página inicial com acesso às funcionalidades do sistema.
- Navegação entre as páginas.
- Template base (`base.html`) compartilhado pelas demais páginas, utilizando o bloco `content`.

## Estrutura do projeto

```text
sistema-educacional-EA-01/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── escola/
│   ├── migrations/
│   ├── templates/
│   │   └── escola/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── alunos.html
│   │       ├── cursos.html
│   │       ├── produtos.html
│   │       └── produto_form.html
│   │
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── .gitignore
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

## Como executar o projeto

### 1. Pré-requisitos

- Python instalado.
- Git instalado.

### 2. Clonar o repositório

```bash
git clone -b EA3 --single-branch https://github.com/paulodiegosantos/sistema-educacional-EA-01.git
```

Entre na pasta do projeto:

```bash
cd sistema-educacional-EA-01
```

### 3. Criar o ambiente virtual

```bash
py -m venv venv
```

### 4. Ativar o ambiente virtual

No Windows:

```bash
venv\Scripts\activate
```

### 5. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 6. Executar as migrações

```bash
py manage.py migrate
```

### 7. Executar o projeto

```bash
py manage.py runserver
```

A aplicação estará disponível em:

http://127.0.0.1:8000/

## Acessando as páginas e a API

| Página ou recurso | Endereço |
|---|---|
| Página inicial | http://127.0.0.1:8000/ |
| Alunos | http://127.0.0.1:8000/alunos/ |
| Cursos | http://127.0.0.1:8000/cursos/ |
| Listagem de produtos | http://127.0.0.1:8000/produtos/ |
| Cadastro de produtos | http://127.0.0.1:8000/produtos/novo/ |
| Django Admin | http://127.0.0.1:8000/admin/ |
| API de usuários | http://127.0.0.1:8000/api/usuarios/ |
| API de usuários (JSON) | http://127.0.0.1:8000/api/usuarios/?format=json |

## Banco de dados

O projeto utiliza SQLite como banco de dados.

O arquivo `db.sqlite3` contém os registros armazenados durante o desenvolvimento, incluindo alunos, cursos, matrículas, produtos e usuários.

Os modelos são definidos em `models.py` e suas alterações são aplicadas ao banco de dados por meio das migrações do Django.

## Autor

Projeto acadêmico desenvolvido por **Paulo Diego** como prática de desenvolvimento web utilizando Django e Django REST Framework.