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

        query_words = query.split()
        results = []

        for memory in self.memories:
            content = memory.content.lower()

            if any(word in content for word in query_words):
                results.append(memory)

        return results

    def add_from_text(self, text: str, memory_id: str):
        from src.memory import build_memory

        if self.get_by_id(memory_id) is not None:
            return None

        memory = build_memory(text, memory_id)

        if memory is None:
            return None

        self.add(memory)
        return memory