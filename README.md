# Mcp Server
This is a server that connects your workspaces to all your llm accounts and facilitates smooth interoperability.

## Getting Started

### Requirements
- Python 3.9+

### Setup
```bash
# clone repository
# (skip if you already have the code locally)
cd mcp

# create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# install dependencies
pip install -r requirements.txt

# run server
uvicorn app.main:app --reload
```

The server will start at http://localhost:8000. Visit http://localhost:8000/docs for the interactive Swagger UI.

### Environment Variables
Copy `.env.example` to `.env` and adjust values as necessary.
