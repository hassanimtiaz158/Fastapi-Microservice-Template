<div align="center">

# ⚡ FastAPI Microservice Template

> **A production-ready FastAPI backend for deploying Machine Learning models with clean REST APIs.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.136.1-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Pydantic](https://img.shields.io/badge/Pydantic-v2-E92063?style=for-the-badge&logo=pydantic&logoColor=white)](https://docs.pydantic.dev/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.8.0-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

<br/>

*A hands-on template demonstrating full CRUD REST APIs, ML model serving, Pydantic data validation, and scalable microservice patterns — all in pure Python.*

</div>

---

## 🗂️ Project Structure

```
Fastapi-Microservice-Template/
│
├── 📄 Get-Post.py          # Core FastAPI app — GET & POST endpoints with Patient model
├── 📄 put_request.py       # PUT endpoint — update existing patient records
├── 📄 delete_request.py    # DELETE endpoint — remove patient records
├── 📄 pydantic_code.py     # Pydantic v2 deep-dive — validation, types, computed fields
├── 📄 patients.json        # JSON file acting as a lightweight data store
├── 📁 ML_Model's API/      # Machine Learning model serving via FastAPI
├── 📄 requirements.txt     # All pinned dependencies
└── 📄 .gitignore
```

---

## ✨ Features

| Feature | Description |
|---|---|
| 🚀 **Full CRUD API** | Create, Read, Update, Delete endpoints for patient records |
| 🧠 **ML Model Serving** | Serve scikit-learn models through REST endpoints |
| 🛡️ **Pydantic v2 Validation** | Strict type-checking, computed fields (BMI), and custom validators |
| 📊 **Sorting & Filtering** | Query params for sorting by height, weight, or BMI (asc/desc) |
| ⚠️ **Proper Error Handling** | HTTP exceptions with meaningful status codes (400, 404, 201) |
| 📂 **JSON Persistence** | Lightweight file-based storage — no database setup required |
| 📦 **Pinned Dependencies** | Fully reproducible environment via `requirements.txt` |

---

## 🔌 API Endpoints

### 🏥 Patient Management API

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Health check — Hello World |
| `GET` | `/view` | Retrieve all patients |
| `GET` | `/about` | API info |
| `GET` | `/patient/{patient_id}` | Fetch a single patient by ID |
| `GET` | `/sort?sort_by=bmi&order=asc` | Sort patients by `height`, `weight`, or `bmi` |
| `POST` | `/create` | Add a new patient record |
| `PUT` | `/update/{patient_id}` | Update an existing patient |
| `DELETE` | `/delete/{patient_id}` | Delete a patient record |

---

## 🧬 Patient Data Model

```python
class Patient(BaseModel):
    patient_id: str          # Unique identifier (e.g., "P001")
    name:       str          # Patient name
    age:        int          # Age (1–119)
    gender:     Literal["Male", "Female", "Others"]
    height:     float        # Height in metres (> 0)
    weight:     float        # Weight in kg (> 0)

    # Auto-computed fields ✨
    bmi:        float        # weight / height²
    verdict:    str          # underweight / normal / A-normal / overweight / obese
```

> BMI and health verdict are **automatically computed** using Pydantic `@computed_field` — no manual calculation needed.

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/hassanimtiaz158/Fastapi-Microservice-Template.git
cd Fastapi-Microservice-Template
```

### 2. Create a virtual environment

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the API server

```bash
uvicorn Get-Post:app --reload
```

### 5. Explore the interactive docs

Open your browser and navigate to:

```
http://127.0.0.1:8000/docs      ← Swagger UI
http://127.0.0.1:8000/redoc     ← ReDoc UI
```

---

## 📬 Example Requests

### Create a Patient

```bash
curl -X POST "http://127.0.0.1:8000/create" \
     -H "Content-Type: application/json" \
     -d '{
           "patient_id": "P001",
           "name": "Hassan Imtiaz",
           "age": 22,
           "gender": "Male",
           "height": 1.75,
           "weight": 70
         }'
```

**Response:**
```json
{ "message": "Patient created successfully" }
```

### Sort Patients by BMI (Descending)

```bash
curl "http://127.0.0.1:8000/sort?sort_by=bmi&order=desc"
```

---

## 📦 Tech Stack

| Package | Version | Purpose |
|---------|---------|---------|
| `fastapi` | 0.136.1 | Web framework |
| `uvicorn` | 0.46.0 | ASGI server |
| `pydantic` | 2.13.3 | Data validation |
| `scikit-learn` | 1.8.0 | ML model training & serving |
| `numpy` | 2.4.4 | Numerical computations |
| `pandas` | 3.0.2 | Data manipulation |
| `email-validator` | 2.3.0 | Email field validation |

---

## 🧪 What You'll Learn

This template is a great reference for understanding:

- ✅ Building REST APIs with **FastAPI** from scratch
- ✅ **Pydantic v2** — `BaseModel`, `Field`, `computed_field`, `Annotated`, `EmailStr`, `AnyUrl`
- ✅ **Path parameters**, **query parameters**, and **request body** handling
- ✅ HTTP **status codes** and custom **error responses**
- ✅ Serving **machine learning models** (scikit-learn) via API endpoints
- ✅ Structuring a **microservice** for real-world AI applications

---

## 🗺️ Roadmap

- [ ] Add PostgreSQL / SQLite database integration
- [ ] Add JWT authentication & authorization
- [ ] Dockerize the application
- [ ] Add unit tests with `pytest`
- [ ] Add CI/CD pipeline with GitHub Actions
- [ ] Deploy to AWS / GCP / Render

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 👨‍💻 Author

**Hasan Ali**

[![GitHub](https://img.shields.io/badge/GitHub-hassanimtiaz158-181717?style=flat-square&logo=github)](https://github.com/hassanimtiaz158)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Hassan%20Imtiaz-0077B5?style=flat-square&logo=linkedin)](https://linkedin.com/in/hassanimtiaz158)

---

## ⭐ Show Your Support

If this project helped you, please consider giving it a **⭐ star** on GitHub — it motivates further development!

---

<div align="center">
  <sub>Built with ❤️ using FastAPI & Python</sub>
</div>
