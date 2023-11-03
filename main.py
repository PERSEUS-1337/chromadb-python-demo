import chromadb

# Get the chroma client
chroma_client = chromadb.Client()

# Create a collection
collection = chroma_client.create_collection(name="my_collection")

# Add some text documents to collection
collection.add(
    documents=["THis is a bad document", "This is a good document"],
    metadatas=[{"source": "my_source"}, {"source": "my_source"}],
    ids=["id1", "id2"],
)

# Query the collection
results = collection.query(query_texts=["bad"], n_results=1)
print(results)
