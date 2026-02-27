
# 🚀 Feel The Future (Plataforma de Estudos)

> Um sistema web robusto desenvolvido em **Django** para otimizar rotinas de estudo através de metodologias ativas.

**Feel The Future** é uma plataforma de aprendizado assíncrono focada em ajudar estudantes a organizarem e reterem conhecimento de forma eficiente. O sistema integra gestão de usuários, materiais de estudo (apostilas) e um sistema interativo de **Flashcards** para revisão espaçada.

---

## 🏗️ Arquitetura e Apps (Django)

O projeto foi construído seguindo o padrão MVT (Model-View-Template) do Django, com a lógica de negócios dividida em aplicativos modulares ("apps"):

* ⚙️ **`study_async/`**: Diretório principal do projeto contendo as configurações globais (`settings.py`, `urls.py`).
* 👤 **`usuarios/`**: App responsável pelo sistema de autenticação, cadastro, login e gestão de perfis.
* 🗂️ **`flashcard/`**: App focado na criação e gestão de flashcards, permitindo aos usuários testarem seus conhecimentos de forma dinâmica.
* 📚 **`apostilas/`**: Módulo dedicado ao armazenamento e organização de materiais de estudo e leitura.

---

## 💻 Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Framework Web:** Django
* **Banco de Dados:** SQLite (`db.sqlite3` - *configurado por padrão para o ambiente de desenvolvimento*)
* **Frontend:** Templates HTML nativos do Django integrados a CSS/JS (localizados na pasta `templates/`).

---

## 🔧 Instalação e Execução Local

Para testar a plataforma na sua máquina, siga o passo a passo abaixo:

### 1. Clonar o repositório
~~~bash
git clone https://github.com/AntDavid/prj_feel_the_future_djg.git
cd prj_feel_the_future_djg
~~~

### 2. Criar e Ativar o Ambiente Virtual
É altamente recomendado o uso de um ambiente virtual para não gerar conflito de bibliotecas.
~~~bash
python -m venv venv

# Para ativar no Windows:
venv\Scripts\activate

# Para ativar no Linux/Mac:
source venv/bin/activate
~~~

### 3. Instalar as Dependências
*(Caso possua um `requirements.txt`, rode o comando abaixo. Se não, instale o Django manualmente: `pip install django`)*
~~~bash
pip install -r requirements.txt
~~~

### 4. Executar as Migrações do Banco de Dados
Como o projeto possui banco de dados local, aplique as tabelas necessárias:
~~~bash
python manage.py makemigrations
python manage.py migrate
~~~

### 5. Rodar o Servidor de Desenvolvimento
~~~bash
python manage.py runserver
~~~
Acesse no seu navegador através do link: `http://127.0.0.1:8000/`

---

## 👨‍💻 Comandos Administrativos Úteis

Para acessar o painel de administração do Django e gerenciar os dados dos aplicativos diretamente:
~~~bash
# Cria um superusuário administrador
python manage.py createsuperuser
~~~

---

## 📄 Licença

Projeto desenvolvido para fins de estudo e portfólio. Livre para uso e modificação.
