# Day 10: Code Implementation
# Persistent Task Manager with JSON, Pathlib & Datetime
# Write your implementation here independently.

from dataclasses import dataclass,asdict
from pathlib import Path
from datetime import datetime
import json

@dataclass
class Task:
    id:int
    title:str
    is_completed:bool = False
    created_at: str = datetime.now().isoformat()


@dataclass
class TaskManager:
    def __init__(self,file_path:Path):
        self.file_path = file_path
        self.tasks : list[Task]=[]
    
    def add_task(self,title:str)-> Task:
        t = Task(id=len(self.tasks)+1,title=title)
        self.tasks.append(t)
        return t
    def save(self) -> None:
        all_tasks = [ asdict(t) for t in self.tasks]
        try:
          with open(self.file_path,"w") as file:
            json.dump(all_tasks,file,indent=2)
            print("Saved successfully to tasks.json")
        except FileNotFoundError:
             print("file location invalid")
    def load(self) -> None:
        if not self.file_path.exists():
            self.tasks = []
            return
        try: 
            with open(self.file_path,"r") as file:
                all_tasks = json.load(file)
                for task in all_tasks :
                    self.tasks = all_tasks
                return self.tasks
        except FileNotFoundError:
            print("File location is invalid")
        except json.JSONDecodeError as e:
            print(f"Error: {e}")


    
    
File = Path(__file__).parent / 'tasks.json'
manager = TaskManager(File)
manager.add_task('Learn JSON serialization')
manager.save()
print(manager.load())
