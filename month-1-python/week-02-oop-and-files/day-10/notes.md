# Day 10: Notes & Developer English Practice

## Topic: JSON Persistence, Pathlib, Datetime & Serialization

---

## 1. Key Concepts & Architecture Mastered

### The JSON Quartet
| Function | Direction | Destination |
| :--- | :--- | :--- |
| `json.dumps()` | Python Object $\rightarrow$ JSON | Returns Python `str` in memory |
| `json.loads()` | JSON `str` $\rightarrow$ Python Object | Returns Python `dict` / `list` |
| `json.dump()` | Python Object $\rightarrow$ JSON File | Streams bytes directly to file descriptor |
| `json.load()` | JSON File $\rightarrow$ Python Object | Reads bytes directly from file descriptor |

### Serialization vs. Deserialization
- **Serialization:** Converting an in-memory runtime data structure or object into a standardized, transportable byte or text format (e.g. JSON string).
- **Deserialization:** Parsing an external serialized format (JSON) back into native runtime domain objects in memory.

### Dictionary Unpacking for Deserialization (`**kwargs`)
```python
# Instead of manual mapping:
# Task(id=item["id"], title=item["title"], is_completed=item["is_completed"])

# Use dictionary unpacking:
tasks = [Task(**item) for item in raw_json_list]
```

---

## 2. Professional Developer English: Standup Review

### Student's Raw Draft:
> **Yesterday:** I learn about @dataclass  
> **Today:** I have successfully implemented and about json in python . I have done some hands on prectice with it . as well as I also learn about asdict  
> **Blockers:** I was feacing problem in deserialization . when I load a json file and deserialize the list now I need to create task and append on self.tasks. I have tried Task(task.name) which gives error . then I try appending tasks directly which was wrong as you sugggest leter.  

### Polished Version (For Standup Meetings & Slack Channels):
> - **Yesterday:** Explored Python's `@dataclass` decorator, inheritance, and type annotations by building a project task domain model.
> - **Today:** Implemented persistent storage using `pathlib` and the `json` module, converting dataclasses with `asdict()` and saving formatted JSON to disk.
> - **Blockers:** Encountered a minor blocker during object deserialization when converting raw parsed dictionaries back into `Task` instances; resolved it using dictionary unpacking (`**item`). No blockers now.

---

## 3. High-Value Tech Vocabulary Learned
- **Serialization / Marshaling:** Transforming memory objects into a storable format.
- **Deserialization / Unmarshaling:** Reconstructing live objects from serialized data.
- **Dictionary Unpacking (`**`):** Passing key-value pairs of a dictionary as keyword arguments into a function/constructor.
- **Deterministic Paths:** Paths anchored to `__file__` that behave identically regardless of which directory the command was launched from.

