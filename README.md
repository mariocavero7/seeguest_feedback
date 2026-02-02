# SeeGuest – Feedback API

Backend API desarrollada como **technical challenge**, usando **FastAPI**, **SQLModel**, **PostgreSQL** y **Docker**.

La aplicación permite crear feedback de huéspedes y consultar estadísticas agregadas.

---

## 🚀 Tecnologías

* **Python 3.11**
* **FastAPI**
* **SQLModel** (modelos de base de datos)
* **Pydantic** (validación request/response)
* **PostgreSQL 15**
* **SQLAlchemy async / asyncpg**
* **Docker & Docker Compose**

---

## 📦 Estructura del proyecto

```
app/
 ├── crud.py          # Lógica de acceso a datos
 ├── database.py      # Configuración DB y sesiones async
 ├── models.py        # Modelos SQLModel
 ├── schemas.py       # Schemas Pydantic
 ├── routes/
 │    └── feedback.py # Endpoints
 └── main.py          # App FastAPI

Dockerfile
docker-compose.yml
README.md
```

---

## 🐳 Levantar el proyecto

### Requisitos

* Docker
* Docker Compose

### Ejecutar

```bash
docker-compose up --build
```

La API estará disponible en:

```
http://localhost:8000
```

Swagger UI:

```
http://localhost:8000/docs
```

---

## 📌 Endpoints

### ▶️ POST /feedback

Crea un nuevo feedback.

**Request body**

```json
{
  "guest_name": "Mario",
  "rating": 5,
  "comment": "Excellent service"
}
```

**Responses**

* `201 Created`
* `400 Bad Request` (rating inválido)

---

### ▶️ GET /feedback

Obtiene la lista de feedbacks.

**Response**

```json
[
  {
    "id": 1,
    "guest_name": "Mario",
    "rating": 5,
    "comment": "Excellent service",
    "created_at": "2026-02-02T20:35:10.123Z"
  }
]
```

---

### ▶️ GET /feedback/{id}

Obtiene un feedback por ID.

**Responses**

* `200 OK`
* `404 Not Found`

---

### ▶️ GET /feedback/stats

Obtiene estadísticas agregadas.

**Response**

```json
{
  "average_rating": 4.3,
  "total_count": 7
}
```

---

## ⚠️ Manejo de errores

* **400** → Rating fuera del rango permitido (1–5)
* **404** → Feedback no encontrado

---

## 🧪 Desarrollo

La aplicación usa:

* SQLModel para persistencia
* Pydantic para validación y serialización
* AsyncSession para operaciones no bloqueantes

---

## ✅ Estado del proyecto

* CRUD completo
* Endpoints documentados automáticamente
* Base de datos persistente
* Dockerizado

---

## 👤 Autor

Mario Cavero

---

Este proyecto fue desarrollado como **backend technical challenge** siguiendo buenas prácticas de FastAPI y SQLAlchemy async.