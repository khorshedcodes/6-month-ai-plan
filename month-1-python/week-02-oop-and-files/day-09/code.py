# Day 9: Code Implementation
# Task Management Domain Model with Inheritance & Dataclasses
# Write your implementation here independently.
from dataclasses import dataclass

@dataclass
class Task:
    id:int
    title:str
    is_completed:bool = False

    def mark_complate(self) -> None:
        self.is_completed = True
    

@dataclass
class BugTask(Task):
    severity:str = "Low"


@dataclass
class FeatureTask(Task):
    estimated_hours:float = 1.0


class Project:
    def __init__(self,name:str):
        self.name = name
        self.tasks:list[Task]=[]
    
    def add_task(self, task:Task) -> None:
        self.tasks.append(task)
    
    def get_pending_task(self) -> list[Task]:
        n_list = [n for n in self.tasks if n.is_completed == False]
        return n_list
    def completed_task(self) -> list[Task]:
        n_list = [ n for n in self.tasks if n.is_completed]
        return n_list


p1 = Project(name="AI application Development")
t1 = BugTask(id=1,title="Fix token parsing",severity="Critical")
t2 = FeatureTask(id=2,title="Implement RAG pipeline",estimated_hours=12.5)
p1.add_task(t1)
p1.add_task(t2)
t1.mark_complate()
print(p1.get_pending_task())
print(p1.completed_task())
