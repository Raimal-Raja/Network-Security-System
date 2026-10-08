# Network-Security-System

Machine-learning pipeline and FastAPI application for network-security classification, training, and CSV prediction.

## Setup and repository reference

### Project structure

- [Dockerfile](Dockerfile)
- [LICENSE](LICENSE)
- [Network_data](Network_data)
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

Training requires MongoDB configuration and may synchronize artifacts to S3. Model selection now uses training-fold macro F1 rather than test-set regression scores. Held-out classification metrics are computed after selection. Preprocessing is currently fitted before cross-validation, so fully fold-isolated preprocessing remains future work. Live training and saved-model inference were not exercised.

Pushes and pull requests run source checks and offline regression tests. Amazon ECR delivery is explicitly selected through workflow_dispatch with publish_image enabled on main. Configure valid AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION and ECR_REPOSITORY_NAME secrets before delivery. The prior delivery run failed because its AWS security token was invalid; this audit cannot repair account credentials.

### Maintenance fixes

- Resolve prediction models, templates, and output paths relative to app.py.
- Remove MongoDB URL printing.
- Evaluate pipeline timestamps when each configuration is created.
- Select classifiers using training-only cross-validation macro F1.
- Support saving artifacts directly in the current directory.
- Replace placeholder CI commands with real syntax/regression checks and correct the ECR registry variable.

### Validation

Audit: 2026-10-08. Repository structure, setup instructions and description were reviewed. 32 existing Python files passed syntax checks; changed files and new regression tests were checked separately. 2 regression tests passed. Syntax checks do not establish full runtime correctness. External APIs, live scraping, GUI interaction, notebook training and production deployment were not comprehensively exercised.

```bash
python -m unittest discover -s tests -v
```

### Repository description

The short GitHub description is provided in [REPOSITORY_DESCRIPTION.md](REPOSITORY_DESCRIPTION.md).

### Contributions

Describe the issue, reproduction steps, environment, and expected behavior when proposing a change. Keep generated environments, credentials, and unnecessary build artifacts out of new commits.

### License

See [LICENSE](LICENSE) for the repository’s licensing terms.
