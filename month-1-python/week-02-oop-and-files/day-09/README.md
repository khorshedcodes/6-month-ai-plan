# Day 9: Inheritance, Composition, Type Hints & Dataclasses

## Learning Objectives
1. Python Type Hints: `str`, `int`, `float`, `bool`, `list[str]`, `dict[str, Any]`, `Optional[int]`.
2. Python's modern `@dataclass` decorator: writing clean data classes without boilerplate `__init__`.
3. Inheritance (`class Child(Parent):`) and `super().__init__(...)`.
4. Composition vs. Inheritance: When to inherit ("is-a") vs when to compose ("has-a").

---

## Daily Task: Task Management Domain Model (Without AI)
Build a modular domain model for a project management system:
1. Base class `Task` using `@dataclass`:
   - `id: int`
   - `title: str`
   - `is_completed: bool = False`
   - Method `mark_complete()`: sets `is_completed = True`.
2. Child class `BugTask(Task)`:
   - Inherits from `Task`.
   - Adds attribute `severity: str` (e.g., "Critical", "Low").
3. Child class `FeatureTask(Task)`:
   - Inherits from `Task`.
   - Adds attribute `estimated_hours: float`.
4. Class `Project` (demonstrating **Composition**):
   - Attribute `name: str`.
   - Attribute `tasks: list[Task]` (holds both `BugTask` and `FeatureTask` polymorphically!).
   - Methods:
     - `add_task(task: Task)`
     - `get_pending_tasks() -> list[Task]`
     - `get_completed_tasks() -> list[Task]`

---

## Developer English Task: Architectural Trade-off
Explain in 3-4 professional sentences:
*"When should a software engineer use `@dataclass` instead of a standard `class` with manual `__init__`?"*

