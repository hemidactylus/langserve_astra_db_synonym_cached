# LLM-cache LangServe chain template

Env vars required:

```
export OPENAI_API_KEY="..."

export ASTRA_DB_APPLICATION_TOKEN="AstraCS:..."
export ASTRA_DB_ID="12345678-..."
# optional:
export ASTRA_DB_KEYSPACE="my_keyspace"
```

Test with

```
poetry install
poetry run python main.py  # or: `poetry shell`, `python main.py`
```
