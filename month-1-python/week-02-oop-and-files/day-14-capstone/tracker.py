# Day 14: Week 2 Capstone Project
# CLI Issue & Habit Tracker
# Write your classes (Issue, IssueManager) and CLI logic here independently.

from dataclasses import dataclass,asdict
from datetime import datetime
from pathlib import Path
import json
import requests

@dataclass
class Issue:
    id:int
    title:str
    category:str
    is_closed:bool = False
    created_at:str = datetime.now().isoformat()
    def __str__(self): 
        return f"[{'CLOSED' if self.is_closed else 'OPEN'}] #{self.id}: {self.title} ({self.category})"


class IssueManager:
    def __init__(self,storage_path:Path):
        self.issues:list[Issue] = []
        self.storage_path = storage_path
    
    def add_issue(self, title:str,category:str)-> Issue:
        new_issue = Issue(id=len(self.issues)+1,title=title,category=category)
        self.issues.append(new_issue)
        return new_issue
        
    def close_issue(self,issue_id:int) -> bool:
         iss = [issue for issue in self.issues if issue.id == issue_id]
         if not iss:
            return False
         else:
            iss[0].is_closed = True
            return True
    def stream_open_issues(self):
        for issue in self.issues:
            if not issue.is_closed:
                yield issue

    def save_to_json(self) -> None:
           serialize_list = [asdict(issue) for issue in self.issues]
           with open(self.storage_path,"w") as file:
                json.dump(serialize_list,file,indent=2)
           
    
    def load_from_json(self) -> None:
        try:
            with open(self.storage_path,'r') as file:
                loaded_issues = json.load(file)
                for issue in loaded_issues:
                    self.issues.append(Issue(**issue))
        except FileNotFoundError:
            print("File not found")
        except json.JSONDecodeError as e:
            print(f"Error: {e}")
    
    def fetch_github_user(self,username:str)-> dict | None:
        res = requests.get(f"https://api.github.com/users/{username}",timeout=5)
        if res.status_code == 200:
            return res.json()
        elif res.status_code  in (404,403):
            print("Invalid request")
        elif res.status_code ==500:
            print("Server Error")
        else:
            print("Unexpected Error")