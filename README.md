# Python Inventory API

A five-project progression building a full inventory management backend — from modular scripts through OOP, a SQLite data layer, and a production-style FastAPI REST API with tests and environment configuration.

Each project introduces one new backend concept on top of the last, using the same inventory dataset throughout.

---

## Project 6 — Modular Design (`project6_modular_design/`)

**New skill: Multi-file project organization**

Refactored a single-file script into a proper module with separation of concerns. Each file owns one responsibility.

| File | Responsibility |
|---|---|
| `file_handler.py` | JSON load/save with exception handling |
| `validation.py` | Input validation and data cleaning |
| `inventory.py` | Business logic (totals, highest-value item) |
| `reporting.py` | Report formatting |
| `inventory_main.py` | Entry point — orchestrates the pipeline |

Key concepts: `import`, module-level vs function-level side effects, `try/except` for `FileNotFoundError` and `json.JSONDecodeError`.

---

## Project 7 — Object-Oriented Programming (`project7_oop/`)

**New skill: Classes, instances, and composition**

Replaced the dict-based data model with classes. `InventoryItem` represents a single record; `InventoryManager` holds a collection and exposes business logic as methods.

Key concepts: `__init__`, `self`, instance methods, attribute access (`self.price` vs `record['price']`), composition (manager owns a list of items).

---

## Project 8 — SQLite Data Layer (`project8_sqlite/`)

**New skill: Relational database with Python's `sqlite3` module**

Replaced JSON file storage with a SQLite database. Functions map directly to SQL CRUD operations.

Key concepts: `CREATE TABLE`, `INSERT`, `SELECT`, `UPDATE`, `DELETE`, parameterized queries (`?` placeholders to prevent injection), `cursor.lastrowid`, `cursor.rowcount`, `GROUP BY` for aggregation vs `ORDER BY` for sorting.

---

## Projects 9 & 10 — FastAPI REST API (`project9_10_fastapi/`)

**New skills: REST API, Pydantic validation, dependency injection, testing, logging, environment configuration**

Exposed the SQLite data layer as a fully functional HTTP API using FastAPI. Added a test suite, structured logging, and production-ready configuration management.

### What was built

- **8 endpoints** — full CRUD (`GET`, `POST`, `PUT`, `DELETE`) on `/inventory` plus three analytics routes
- **Pydantic models** — separate `Item` (request), `ItemResponse` (response), and `ItemUpdate` (partial update) schemas
- **Dependency injection** — `Depends(db_connection)` wires a SQLite connection into each route without global state
- **`pytest` test suite** — `test_routes.py` uses `TestClient` for end-to-end route tests; `test_crud.py` uses an in-memory SQLite fixture to test CRUD functions in isolation
- **Logging** — dual handlers (file + stdout) via Python's `logging` module; each module uses `getLogger(__name__)`
- **Environment config** — `python-dotenv` + `pathlib` for database path resolution that works from any working directory

### Project structure

```
project9_10_fastapi/
├── app/
│   ├── __init__.py
│   ├── main.py        # route definitions
│   ├── crud.py        # SQL functions
│   ├── models.py      # Pydantic schemas
│   ├── mydb.py        # DB connection dependency
│   └── config.py      # env var loading
├── tests/
│   ├── test_routes.py
│   └── test_crud.py
├── requirements.txt
└── .env.example
```

### Running locally

```bash
# from project9_10_fastapi/
pip install -r requirements.txt
cp .env.example .env

py -m uvicorn app.main:app --reload
# API available at http://127.0.0.1:8000
# Interactive docs at http://127.0.0.1:8000/docs

py -m pytest tests/
```

### Endpoints

| Method | Route | Description |
|---|---|---|
| GET | `/inventory` | All items |
| GET | `/inventory/{id}` | Single item |
| POST | `/inventory` | Create item |
| PUT | `/inventory/{id}` | Partial update |
| DELETE | `/inventory/{id}` | Delete item |
| GET | `/analytics/category_totals` | Value summed by category |
| GET | `/analytics/highest_value_item` | Single highest-value item |
| GET | `/analytics/total_inventory_value` | Sum of all inventory value |

---

## Skills Progression

| Project | Storage | Paradigm | New Concept |
|---|---|---|---|
| 6 | JSON file | Procedural, modular | Module separation, exception handling |
| 7 | JSON file | OOP | Classes, self, composition |
| 8 | SQLite | Procedural | SQL CRUD, parameterized queries, aggregation |
| 9/10 | SQLite | FastAPI | REST, Pydantic, DI, pytest, logging, dotenv |
