# LLM Dispatch Tool 🚀

This is a FastAPI-based backend project for dispatching user messages to a local Large Language Model (LLM) and analyzing Python code using SonarQube, CodeScene, and LLM feedback. This tool was developed as part of the **Advance Software Quality and Security** course.

## 📁 Project Structure

```
llm_dispatch_tool/
│
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app entrypoint
│   ├── models.py            # SQLAlchemy ORM models
│   ├── schemas.py           # Pydantic schemas
│   └── database.py          # DB setup with SQLAlchemy
│
├── resources/
│   └── migrate.sql          # SQL schema script
│
├── messages.db              # SQLite DB (used for quick demo)
├── requirements.txt         # All dependencies
├── UML_diagram.png          # UML model diagram
└── .env                     # Environment variables (ignored by Git)
```

## ⚙️ Features

- Send message to a local LLM (e.g., DeepSeek via LM Studio).
- Store user message and model response in a database.
- Analyze Python source code quality using:
  - SonarQube output
  - CodeScene output
  - Local LLM's feedback

## 🧑‍💻 How to Run (Development)

### 1. Clone the repository

```bash
git clone https://github.com/Nhantran65/ASEQS
cd ASEQS
```

### 2. Set up a virtual environment (Windows)

```bash
python -m venv env
source env/Scripts/activate
```

> Use `source env/bin/activate` on Linux/macOS.

### 3. Install dependencies

```bash
pip install -r requirements.txt
```
### 4. Create SQL Database in MySQL Workbench using the sql scripts in the `resources/migrate.sql` file

``` Run the migrate.sql script```

### 5. Create a `.env` file

Set your own MySQL/MariaDB connection string like:

```env
DATABASE_URL=mysql+pymysql://user:password@localhost:3306/llm_messages
```

### 6. Run the FastAPI server

```bash
uvicorn app.main:app --reload
```

Now open your browser and navigate to:  
📎 `http://127.0.0.1:8000/docs` — to access the Swagger UI for testing the API.

## 📬 API Endpoints

- `POST /messages/` — Send message to LLM and save response.
- `GET /messages/{id}` — Get message by ID.
- `GET /messages/?skip=0&limit=10` — Paginated list of messages.
- `POST /analyze-code/` — Analyze code using LLM + SonarQube + CodeScene.

## 💡 Note

- This project calls a **local LLM server**, such as [LM Studio](https://lmstudio.ai/), running on `http://localhost:1234`. Make sure your model (e.g., DeepSeek-R1) is running before sending requests.
- You can modify the model used in `main.py`.

## 🧠 Authors

- [Nhan Tran](https://github.com/Nhantran65)
- [Pramodi Samaratunga](https://github.com/pramodisamaratunga)

## 📜 License

This project is for academic use as part of the course **Advanced Software Quality and Security**.