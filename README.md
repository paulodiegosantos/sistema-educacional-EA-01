# Sistema Educacional

Sistema web desenvolvido com **Python e Django** para uma empresa do setor educacional, permitindo o cadastro, gerenciamento e consulta de alunos e cursos.

O projeto foi desenvolvido como parte de uma Experiência de Aprendizagem do curso de Análise e Desenvolvimento de Sistemas.

## Tecnologias utilizadas

- Python
- Django
- SQLite
- HTML5
- Git e GitHub

## Funcionalidades

- Cadastro de alunos com nome, sobrenome e e-mail.
- Cadastro de cursos com título e descrição.
- Relacionamento entre alunos e cursos (muitos-para-muitos).
- Gerenciamento de alunos e cursos pelo Django Admin.
- Listagem de alunos cadastrados.
- Listagem de cursos cadastrados.
- Exibição dos cursos em que cada aluno está matriculado.

## Estrutura do projeto

```text
sistema-educacional/
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
│   │       ├── alunos.html
|   |       ├── cursos.html
│   │       └── home.html
│   ├── admin.py
│   ├── models.py
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
git clone https://github.com/paulodiegosantos/sistema-educacional-EA-01.git
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

### 6. Executar o projeto

```bash
py manage.py runserver
```

A aplicação estará disponível em:

http://127.0.0.1:8000/

## Acessando as páginas

| Página | Endereço |
|---|---|
| Alunos | http://127.0.0.1:8000/alunos/ |
| Cursos | http://127.0.0.1:8000/cursos/ |
| Django Admin | http://127.0.0.1:8000/admin/ |

## Banco de dados

O projeto utiliza SQLite como banco de dados.

O arquivo `db.sqlite3` está incluído no repositório e contém registros de exemplo de alunos, cursos e suas respectivas matrículas. Dessa forma, ao clonar o projeto, os dados de demonstração já estarão disponíveis.

## Autor

Projeto acadêmico desenvolvido por **Paulo Diego** como prática de desenvolvimento web utilizando o framework Django.
