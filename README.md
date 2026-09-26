# Memora
- Temporary information should not automatically become long-term memory.
- Useful memories should help the assistant personalize future conversations.
- Candidate memory types: preferences, facts, goals, projects, and important context.
- A memory needs structured fields, not just raw text.
- content: the actual information being remembered.
- type: categorizes the memory, such as preference, fact, goal, project, or context.
- importance: indicates how valuable the memory is for future conversations.
- confidence: indicates how certain the system is that the memory is correct.
- created_at: records when the memory was created.
- updated_at: records when the memory was last changed.
- id: uniquely identifies each memory.
- Memory creation converts extracted information into a structured Memory object.

## Current Capabilities

- Create structured memory objects.
- Store memories in an in-memory memory store.
- Retrieve all stored memories.
- Retrieve a memory by ID.
- Delete a memory by ID.


## Retrieval

Memora currently supports keyword-based memory retrieval.

- Search is case-insensitive.
- Leading and trailing spaces are ignored.
- Empty searches return no results.