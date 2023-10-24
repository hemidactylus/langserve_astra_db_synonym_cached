from astradb_synonyms_caching import chain

if __name__ == "__main__":
    response = chain.invoke({"word": "soar"})
    print(response)
