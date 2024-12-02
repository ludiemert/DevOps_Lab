# DevOps_Lab
 - This repository is dedicated to my continuous learning in DevOps. Here, I will explore and document fundamental practices, tools, and concepts, covering topics such as CI/CD, automation, Infrastructure as Code (IaC), containers, monitoring, and more.
 - The goal is to develop both practical and theoretical knowledge of DevOps best practices, with hands-on examples and projects that showcase the use of technologies like Docker, Kubernetes, Ansible, Terraform, GitHub Actions, among others

### Project_02

 - The project demonstrates the use of container orchestration with Docker Compose and works with multiple containers, such as:
1.	Container orchestration - Docker Compose:
- The docker-compose.yml was used to configure the services in an integrated way, including the application (app) and the database (db).
- This allows for the management and automation of containers.
2.	Working with multiple containers:
- I configured the app and db as separate services that communicate via Docker's internal network, something essential for development or production environments.
- I configured dependencies such as psycopg2 to communicate with the PostgreSQL database and ensured that the containers were initialized correctly.
3.	Evaluated learning about multiple containers:
- The use of Docker Compose in this project demonstrated:
-- How to configure multiple services in the docker-compose.yml file.
-- How to share networks and volumes between containers.
-- How to solve problems with logs (docker logs), rebuilding (docker-compose build) and restarting (docker-compose up).
-- Validating communication between the Python application and the PostgreSQL database.


