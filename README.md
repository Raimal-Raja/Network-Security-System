# Network-Security-System

Machine-learning pipeline and FastAPI application for network-security classification, training, and CSV prediction.

## Repository guide

### Contents

- [Dockerfile](Dockerfile)
- [LICENSE](LICENSE)
- [Network_data](Network_data)
- [README.md](README.md)
- [app.py](app.py)
- [data_schema](data_schema)
- [final_model](final_model)
- [main.py](main.py)
- [networksecurity](networksecurity)
- [prediction_output](prediction_output)
- [push_data.py](push_data.py)
- [requirements.txt](requirements.txt)
- [setup.py](setup.py)
- [templates](templates)
- [test_mongodb.py](test_mongodb.py)
- [valid_data](valid_data)

### Getting started

```bash
git clone https://github.com/Raimal-Raja/Network-Security-System.git
cd Network-Security-System
```

Create and activate a virtual environment, then install the project dependencies:

```bash
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r "requirements.txt"
```

Application entry point:

```bash
python -m uvicorn app:app --host 127.0.0.1 --port 8000
```

### Configuration and limitations

Training requires MongoDB configuration and may synchronize artifacts to S3. Live training and saved-model inference were not exercised.

### Maintenance fixes

- Resolve prediction models, templates, and output paths relative to app.py.
- Remove MongoDB URL printing.
- Evaluate pipeline timestamps when each configuration is created.

### Validation

Reviewed on 2026-10-08. Python syntax checks passed for 32 source files. Syntax validation does not establish runtime correctness or dependency compatibility.

### Contributions

Describe the issue, reproduction steps, environment, and expected behavior when proposing a change. Keep generated environments, credentials, and unnecessary build artifacts out of new commits.

### License

See [LICENSE](LICENSE) for the repository’s licensing terms.
