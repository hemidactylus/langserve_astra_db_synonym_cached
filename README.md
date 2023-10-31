# LLM-cache Langchain template with Cassandra

A simple chain template showcasing usage of LLM Caching
backed by (CQL) Astra DB / Apache Cassandra®.

## Setup:

You need:

- an [Astra](https://astra.datastax.com) Vector Database (free tier is fine!). **You need a [Database Administrator token](https://awesome-astra.github.io/docs/pages/astra/create-token/#c-procedure)**, in particular the string starting with `AstraCS:...`;
- likewise, get your [Database ID](https://awesome-astra.github.io/docs/pages/astra/faq/#where-should-i-find-a-database-identifier) ready, you will have to enter it below;
- an **OpenAI API Key**. (More info [here](https://cassio.org/start_here/#llm-access), note that out-of-the-box this demo supports OpenAI unless you tinker with the code.)

_Note:_ you can alternatively use a regular Cassandra cluster: to do so, make sure you provide the `USE_CASSANDRA_CLUSTER` entry as shown in `.env.template` and the subsequent environment variables to specify how to connect to it.

You need to provide the connection parameters and secrets through environment variables. Please refer to `.env.template` for what variables are required.

## Running the chain

### Within a LangChain app

Assuming you have already created the app (i.e. `langchain app new MyApp; cd MyApp`), this is what you'll need:

```
langchain app add --repo "hemidactylus/langserve_cassandra_synonym_caching" --branch main
```

*Important*: adjust the project's `server.py` as instructed in the output of the above.

Now, make sure all required environment variables are set, and run

```
langchain serve
```

that's it. You can now test the new endpoints by opening `http://127.0.0.1:8000/docs`, or visiting directly `http://127.0.0.1:8000/cassandra_entomology_rag/playground/`.

You will provide a word and get up to five synonyms back. Pay attention to the response times when submitting a word already used: the answer will be much faster, showing caching in action.


### Stand-alone

For a standalone usage (outside of `langchain serve`), clone this repo,
`cd` to its root directory, ensure you set all environment variables,
then launch:

```
poetry install
poetry run python main.py
```
