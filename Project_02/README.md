# DevOps Project with Docker Compose

This is a demonstration project that uses **Docker Compose** to efficiently orchestrate multiple containers. It implements a Python Flask application integrated with a PostgreSQL database to showcase the use of containers in development and production environments.

## 🛠️ Technologies Used

- **Python 3.10**
- **Flask**
- **PostgreSQL**
- **Docker**
- **Docker Compose**

  -----

  <h4 align="center"># DevOps Project with Docker Compose - WEB 🚀</h4>

<div align="center">
    <table>
        <tr>
            <td style="width: 50%; text-align: center;">
                <img src="Projeto\img_projec/localhost_5000 _DevOps_Docker Compose.png" style="width: 90%;" alt="localhost_5000 _DevOps_Docker Compose">
                <p style="margin-top: 5px;">localhost_5000 _DevOps_Docker Compose - WEB</p>
            </td>           
        </tr>
    </table>
</div>

  <br/>
  <br/>
---


## 📋 Features

- **Container Orchestration**:
  - Configure multiple services in the `docker-compose.yml` file.
  - Communication between Flask application and PostgreSQL database via Docker's internal network.

- **Simple API**:
  - Endpoint to list records from the PostgreSQL database.

- **Fully Containerized Integration**:
  - Simplified setup for development and testing.

## 🚀 How to Run the Project

### Prerequisites

- **Docker** and **Docker Compose** installed on your machine.

### Step-by-Step Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/repository-name.git
   cd repository-name
   ```

2.   ### Build the containers:
   ```bash
   docker-compose build
   ```

3.   ### Start the services:
  ```bash
  docker-compose up
   ```

4.   ### Access the application::
   -  Open http://localhost:5000 in your browser to interact with the application.


5.   ### Sample API:   
 - List data from the database: http://localhost:5000/data


6.   ### Stopping the Services
 -  To stop the containers, use:
 ```bash
docker-compose down
 ```

-----

🗂️ Project Structure

 ```bash
Project/
│
├── app/
│   ├── main.py               # Main Flask application code
│   ├── requirements.txt      # Python application dependencies
│
├── db/
│   └── data/                 # Persistent volume for PostgreSQL data
│
├── Dockerfile                # Application container configuration
├── docker-compose.yml        # Container orchestration file
└── README.md                 # Project documentation

 ```

----

🐳 Docker Compose File Overview

 ```bash

version: '3.8'
services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "5000:5000"
    depends_on:
      - db
    volumes:
      - ./app:/app

  db:
    image: postgres:13
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: mydatabase
    volumes:
      - ./db/data:/var/lib/postgresql/data
    ports:
      - "5432:5432"


 ```

📚 Learnings:

 - Configuring multiple services with Docker Compose.
 - Establishing communication between an application and a database using environment variables.
 - Troubleshooting common issues in containerized environments (e.g., dependencies, connectivity).
 - Using volumes for data persistence in PostgreSQL.

 ----

📜 License
 - This project is licensed under the MIT License.

   -----
   ### Portugues
   ### Projeto DevOps com Docker Compose

Este é um projeto de demonstração que utiliza **Docker Compose** para orquestrar múltiplos contêineres de forma eficiente. Ele implementa uma aplicação Python Flask integrada com um banco de dados PostgreSQL para exemplificar o uso de contêineres em ambientes de desenvolvimento e produção.

#### 🛠️ Tecnologias Utilizadas

- **Python 3.10**
- **Flask**
- **PostgreSQL**
- **Docker**
- **Docker Compose**

#### 📋 Funcionalidades

- **Orquestração de Contêineres**:
  - Configuração de múltiplos serviços no arquivo `docker-compose.yml`.
  - Comunicação entre aplicação Flask e banco de dados PostgreSQL via rede interna do Docker.

- **API Simples**:
  - Endpoint para listar registros do banco de dados PostgreSQL.

- **Integração Totalmente Contêinerizada**:
  - Configuração simplificada para desenvolvimento e testes.

#### 🚀 Como Executar o Projeto

### Pré-requisitos

- **Docker** e **Docker Compose** instalados em sua máquina.

#### Passo a Passo

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
     ```
   cd nome-do-repositorio

2. #### Construa os contêineres:
  ```bash
 docker-compose build
  ```

3. #### Inicie os serviços:
 ```bash
docker-compose up
 ```

#### Acesse a aplicação:
 - Acesse http://localhost:5000 no navegador para interagir com a aplicação.

#### API de exemplo:
Listar os dados do banco: http://localhost:5000/data

#### Encerrando os Serviços
Para parar os contêineres, utilize:
 ```bash
docker-compose down
 ```
-----

📚 Aprendizados

 - Configuração de múltiplos serviços no Docker Compose.
 - Comunicação entre aplicação e banco de dados utilizando variáveis de ambiente.
 - Solução de problemas comuns durante o uso de contêineres (ex.: dependências, conectividade).
 - Uso de volumes para persistência de dados no PostgreSQL.
   
   ----

   - #### My LinkedIn - [![Linkedin Badge](https://img.shields.io/badge/-LucianaDiemert-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/lucianadiemert/)](https://www.linkedin.com/in/lucianadiemert/)

#### Contact

<img align="left" src="https://www.github.com/ludiemert.png?size=150">

#### [**Luciana Diemert**](https://github.com/ludiemert)

🛠 Full-Stack Developer <br>
🖥️ Python Enthusiast | Computer Vision | AI Integrations <br>
📍 São Jose dos Campos – SP, Brazil

<a href="https://www.linkedin.com/in/lucianadiemert" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white" alt="LinkedIn Badge" height="25"></a>&nbsp;
<a href="mailto:lucianadiemert@gmail.com" target="_blank"><img src="https://img.shields.io/badge/Gmail-D14836?style=flat&logo=gmail&logoColor=white" alt="Gmail Badge" height="25"></a>&nbsp;
<a href="#"><img src="https://img.shields.io/badge/Discord-%237289DA.svg?logo=discord&logoColor=white" title="LuDiem#0654" alt="Discord Badge" height="25"></a>&nbsp;
<a href="https://www.github.com/ludiemert" target="_blank"><img src="https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white" alt="GitHub Badge" height="25"></a>&nbsp;

<br clear="left"/>



