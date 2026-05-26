# Contributing

## Development Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Code Style

- Use black for formatting: `black app/`
- Use flake8 for linting: `flake8 app/`
- Type hints required: `mypy app/`

## Testing

```bash
pytest tests/
```

## Pull Request Process

1. Create feature branch: `git checkout -b feature/my-feature`
2. Make changes and test
3. Push and create PR
4. PR must pass CI/CD
