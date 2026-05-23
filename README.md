# FastAPI KR4 — Migrations, Errors, Validation, Tests

Instructions to run the project:

1. Create virtualenv and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Configure environment (optional): copy `.env.example` to `.env`.

3. Run the app:

```bash
uvicorn app.main:app --reload
```

4. Run tests:

```bash
pytest -q
```

Alembic migrations are included in the `alembic/` folder. The DB default is `sqlite:///./test.db`.