# Contributing to Oracle 26ai RAG API

## Getting Started

1. Fork the repository
2. Clone your fork:
```bash
   git clone git@github.com:YOUR_USERNAME/oracle-26ai-rag-api.git
   cd oracle-26ai-rag-api
```
3. Create a virtual environment:
```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
```
4. Copy environment template:
```bash
   cp .env.example .env
   # Edit .env with your credentials
```
5. Start developing!

## Development Guidelines

- Follow [PEP 8](https://pep8.org/) style guide
- Add docstrings to all functions
- Use type hints for better code clarity
- Test locally before submitting PRs
- Update documentation if needed

## Testing

```bash
# Run unit tests
pytest tests/ -v

# Check code style
black --check app/
flake8 app/
mypy app/
```

## Submitting Changes

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Commit changes: `git commit -am 'Add new feature'`
3. Push to your fork: `git push origin feature/your-feature`
4. Submit a Pull Request with clear description

## Reporting Issues

- Use GitHub Issues for bug reports and feature requests
- Check existing issues first to avoid duplicates
- Provide clear steps to reproduce bugs
- Include environment details (OS, Python version, etc.)

## Questions?

- Check the [Wiki](https://github.com/kjosh2008/oracle-26ai-rag-api/wiki) for guides
- Review [troubleshooting docs](docs/TROUBLESHOOTING.md)
- Open a discussion in Issues

Thank you for contributing! 🙏
