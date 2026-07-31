import chromadb

class Memory:

    def __init__(self):
        self.client = chromadb.PersistentClient(path="./memory_db")
        self.collection = self.client.get_or_create_collection(
            name="ananya_memory"
        )

    def save(self, text):
        self.collection.add(
            documents=[text],
            ids=[str(self.collection.count() + 1)]
        )

    def recall(self):
        data = self.collection.get()

        if len(data["documents"]) == 0:
            return []

        return data["documents"]