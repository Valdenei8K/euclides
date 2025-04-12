# Euclides - Desafio Técnico Full Stack

Este projeto é um desafio técnico Full Stack com foco em processamento assíncrono utilizando Django, Celery e RabbitMQ, com um frontend Angular consumindo os dados da API.

---

## 📚 Descrição

A aplicação permite que o usuário envie três números via frontend. Esses números são enviados ao backend, que os coloca em uma fila utilizando Celery e RabbitMQ. Um worker Celery processa os dados (calculando **média** e **mediana**) de forma assíncrona e salva os resultados no banco de dados (SQLite).

> O nome do projeto — **Euclides** — é uma homenagem a **Euclides de Alexandria**, considerado o "pai da geometria". Como este projeto envolve cálculos matemáticos, a escolha do nome representa essa conexão com a história da matemática.

---

## 🧰 Tecnologias utilizadas

- **Backend**: Django, Django REST Framework, Celery, RabbitMQ
- **Frontend**: Angular
- **Mensageria**: RabbitMQ
- **Banco de dados**: SQLite (compartilhado entre backend e worker)
- **Containerização**: Docker e Docker Compose

---

## 🚀 Como rodar o projeto com Docker

### ✅ Pré-requisitos

- Docker instalado
- Docker Compose instalado

### 📦 Clonando o repositório

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo

▶️ Subindo o ambiente completo

# Build e start dos containers
docker-compose up --build

# Acessar o terminal do backend
docker exec -it backend bash

# Rodar as migrations manualmente (caso necessário)
docker exec backend python manage.py migrate

# Parar todos os containers
docker-compose down
```

### 🌐 Endpoints e URLs úteis

Serviço	
- Frontend	http://localhost:4300
- Backend API	http://localhost:8001
- RabbitMQ	http://localhost:15672

### 🧪 Testando a aplicação
   -  Enviar números (POST)  
   -  POST http://localhost:8001/api/processar/   


Body JSON
```json
{
  "numeros": [5,10,15]
}
```

- Ver resultados processados (GET)
- GET http://localhost:8001/api/resultados/
```json
[
  {
    "id": 1,
    "media": 10,
    "mediana": 10,
    "numeros":[5, 10, 15],
    "status":"Concluído",
    "data_processamento": "2025-04-11T15:22:33.123Z"
  }
]
```