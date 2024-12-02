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
   


