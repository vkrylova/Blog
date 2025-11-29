# 📜 Flask Blog API

A lightweight Flask-based backend application.

---

## 🧭 Authentication

- **User Registration**  
- **User Login (JWT)**  
- **Protected Routes** using `Authorization: Bearer <token>`

## 📝 Posts

- **Create** a new post  
- **Update** an existing post  
- **Delete** a post  
- **Retrieve All Posts**  
- **Retrieve a Single Post** by its ID  

## 💬 Comments

- **Add a Comment** to a specific post  
- **Retrieve All Comments** for that post  

## 🧩 Additional Notes

- Follows a **RESTful API** structure  
- No user interface — a **pure server-side application**  
- All responses in **JSON**  
- Designed for **clarity**, **simplicity**, and **future expansion**

---
## 📁 Project Structure

```
project/
│
├── app.py            # Application initialization
├── routes.py         # All API endpoints
├── models.py         # User, Post, Comment models
├── requirements.txt  # Dependencies
├── config.py         # Settings
└── run.py            # To start the application

```

---


## ⚙️ Setup
1. Install dependencies:

```
pip install -r requirements.txt
```

2. Set environment variables:

```
export FLASK_APP=app.py
export JWT_SECRET_KEY="your-secret-key"
```

3. Run the application:

```
flask run
```

---
## 🔐 Authentication
The project uses flask-jwt-extended.

After obtaining a token from **/v1/login**, include it in requests:

```
Authorization: Bearer <token>
```

---

## 🗺️ API Endpoints
Below lies the map of all available routes.

<details>
  <summary>Open me</summary>
  
1. **Registration**
   
```
POST /v1/register
```

Body:

```json
{
  "email": "vk@gmail.com",
  "username": "Vk",
  "password": "123456"
}
```


2. **Login**

```
POST /v1/login
```

Response:

```json
{
  "access_token": "..."
}
```

### 📚 Posts

1. **Create a Post** (JWT required)

```
POST /v1/posts
```

Body:

```json
{
    "title": "First post",
    "body": "First post First post First post"
}
```

2. **Get All Posts**

```
GET /v1/posts
```

Response:
  
  ```json
{
    "posts": [
        {
            "author": {
                "id": 1
            },
            "body": "First post First post First post",
            "id": 1,
            "timestamp": "28-11-2025 21:40:55",
            "title": "First post"
        },
        {
            "author": {
                "id": 1
            },
            "body": "Second post Second post Secondst post",
            "id": 2,
            "timestamp": "28-11-2025 21:42:03",
            "title": "Second post"
        }
    ]
}
  ```

3. **Get a Single Post**

```
GET /v1/posts/<post_id>
```

Response:

```json
{
    "posts": {
        "author": {
            "id": 1
        },
        "body": "First post First post First post",
        "id": 1,
        "timestamp": "28-11-2025 21:40:55",
        "title": "First post"
    }
}
```

4. **Update a Post** (JWT required)

```
PATCH /v1/posts/<post_id>
```

5. **Delete a Post** (JWT required)

```
DELETE /v1/posts/<post_id> 
```

### ✒️ Comments
6. **Add a Comment** (JWT required)

```
POST /v1/posts/<post_id>/comments 
```
Body: 

```json
{
    "body": "Looking good!"
}
```

7. **Get Comments**

```
GET /v1/posts/<post_id>/comments
```

Response:

```json
{
    "comments": [
        {
            "author": {
                "id": 1
            },
            "body": "Looking good!",
            "id": 1,
            "timestamp": "29-11-2025 15:49:56"
        },
        {
            "author": {
                "id": 1
            },
            "body": "Wow!",
            "id": 2,
            "timestamp": "29-11-2025 15:49:56"
        }
    ]
}
```

</details>

---

## 🧾 Response Format

All responses are returned in clean, structured JSON.

Example:

```json
{
  "message": "User registered successfully"
}
```

---
