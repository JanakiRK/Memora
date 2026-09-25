from src.memory import Memory


class MemoryStore:
    def __init__(self):
        self.memories = []

    def add(self, memory: Memory):
        self.memories.append(memory)

    def get_all(self):
        return self.memories

    def get_by_id(self, memory_id: str):
        for memory in self.memories:
            if memory.id == memory_id:
                return memory
        return None

    def delete(self, memory_id: str):
        self.memories = [
            memory for memory in self.memories
            if memory.id != memory_id
        ]

    def search(self, query: str):
        query = query.strip().lower()

        if not query:
            return []
        results = []

        for memory in self.memories:
            if query.lower() in memory.content.lower():
                results.append(memory)

        return results