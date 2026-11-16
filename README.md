# Healthcare project in Django

A Django project with 5 models and a REST API (Django REST Framework).

## Tech stack

- Python 3
- Django
- Django REST Framework
- Pillow
- Database: PostgreSQL

## Project structure

- `healthcare_project/`: project settings and root URLs
- `assessment/`: Django app
- Tests: `assessment/tests.py`

## Data model

| Model | App | Fields |
|---|---|---|
| `Patient` | `assessment` | full_name, date_of_birth, gender, medical_history |
| `Doctor` | `assessment` | specialty, hospital, years_of_experience |
| `MedicalTest` | `assessment` | name, result, date, health_records |
| `HealthRecord` | `assessment` | patient, doctor, blood_pressure, cholesterol, bmi, diabetes_history, medical_tests |
| `Prediction` | `assessment` | condition_type, risk_score, prediction_date, health_record, doctor |

## URL routes

Declared in `urls.py`:

- `/patients/ (router)`
- `/doctors/ (router)`
- `/medical-tests/ (router)`
- `/health-records/ (router)`
- `/blog/`
- `/health/`

## How to run

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

`settings.py` is configured for PostgreSQL: create the database and use your own credentials before running `migrate`.

Then open `http://127.0.0.1:8000/`.

---

Author: [Chaouki Bayoudhi](https://github.com/ChaoukiBayoudhi)
