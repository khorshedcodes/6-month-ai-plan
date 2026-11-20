# Day 20: Code Implementation
# CLI News & HackerNews Top Stories Aggregator
# Write your implementation here independently.
from dataclasses import dataclass, asdict
from pathlib import Path
import logging
import requests
import argparse
import json



parser = argparse.ArgumentParser(description="A tool for parsing CLI arguments")
parser.add_argument("--limit",type=int,default=5,help="Max article to show")
parser.add_argument("--verbose",action="store_true",help="Enable debug logs")

@dataclass
class Article:
    id:int
    title:str
    url:str=""
    score:int=0
    by:str=""


class NewsAggregator:
    def __init__(self,cache_file:Path):
        self.cache_file = cache_file
        self.articles = []
    
    def fetch_top_stories(self,limit:int=5) -> list [Article]:
        logging.info("Fetching top stories...")
        try:
            res = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json",timeout=5)
            if res.status_code != 200:
                    res.raise_for_status()
            ids = res.json()
        except requests.exceptions.RequestException:
            logging.warning("Netwrok erNetwork unavailable. Falling back to local cache...ror")
            self.load_from_cache()
        for story_id in range(0,limit):
            try:
                r = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{ids[story_id]}.json",timeout=5)
                if r.status_code != 200:
                    r.raise_for_status()
                data = r.json()
                art = Article(id= data['id'] , title=data['title'],url=data.get("url",""),score=data.get('score',""),by=data.get("by",""))
                self.articles.append(art)
                self.save_to_cache(self.articles)
            except requests.exceptions.RequestException as e:
                logging.warning('Network unavailable. Falling back to local cache...')
                self.load_from_cache()
        return self.articles
    def save_to_cache(self,articles:list[Article])-> None:
        try:
            with open(self.cache_file, 'w') as file:
                stories = [asdict(a) for a in articles]
                json.dump(stories,file,indent=2)
        except FileNotFoundError as e:
             print(f"File Not found : {e}")
    
    def load_from_cache(self) -> list[Article]:
        try:
            with open(self.cache_file,"r") as file:
                data = json.load(file)
                py_data = [Article(**item) for item in data]
                return py_data
        except FileNotFoundError:
            print("file Not found")
        except json.JSONDecodeError as e:
            print(f"Json Error: {e}")


def main():
     args = parser.parse_args()
     newsAgg = NewsAggregator('cache.json')
     artical_list = newsAgg.fetch_top_stories(args.limit)
     for index,artical in enumerate(artical_list):
        print(f"{index+1}. [Score:{artical.score}] {artical.title} (by {artical.by}) \n URL:{artical.url}")

if __name__ == "__main__":
    main()