from src.memory import build_memory, extract_memory
from src.memory_store import MemoryStore


def test_extract_memory():
    result = extract_memory("I prefer Python")

    assert result["content"] == "I prefer Python"
    assert result["type"] == "preference"


def test_build_memory():
    memory = build_memory("My goal is to become an AI engineer", "1")

    assert memory is not None
    assert memory.type == "goal"
    assert memory.content == "My goal is to become an AI engineer"


def test_store_memory():
    store = MemoryStore()

    memory = store.add_from_text("I prefer Python", "1")

    assert memory is not None
    assert store.get_by_id("1") == memory


def test_duplicate_memory_id():
    store = MemoryStore()

    store.add_from_text("I prefer Python", "1")
    duplicate = store.add_from_text("I prefer Java", "1")

    assert duplicate is None
    assert len(store.get_all()) == 1


def test_memory_search():
    store = MemoryStore()

    store.add_from_text("I prefer Python", "1")
    store.add_from_text("My goal is to become an AI engineer", "2")

    results = store.search("Python")

    assert len(results) == 1
    assert results[0].content == "I prefer Python"