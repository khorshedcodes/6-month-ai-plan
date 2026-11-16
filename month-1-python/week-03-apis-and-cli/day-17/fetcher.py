# Day 17: Code Implementation
# Production CLI Tool with argparse and structured logging
# Write your implementation here independently.
import argparse
import logging
import requests

parser = argparse.ArgumentParser(description="A tool for github repo")

parser.add_argument("--user", type=str,required=True,help="Github Username")
parser.add_argument("--limit",type=int,default=5,help="Max repo to display 5")
parser.add_argument("--verbose", action="store_true",help="Enable debug logs")








def fetch_repo(username:str,limit:int) -> list[dict]:
    try:
        url = f"https://api.github.com/users/{username}/repos?per_page={limit}"
        logging.info(f"Connecting to Github API for user: {username}..")
        logging.debug(f"Request URL: {url} with timeout=5")
        res = requests.get(url,timeout=5)
        status_code = res.status_code
        if status_code ==200:
            repos = res.json()
            logging.info(f"Successfully retrived {len(repos)}")
            return repos
        elif status_code == 404:
            logging.error(f"User {username} was not found on github")
            return []
        else:
            logging.error(f"Unexpected HTTP satus {status_code}")
            return []
    except requests.exceptions.RequestException as e:
        logging.error(f"Error : { e}")


def main():
    args = parser.parse_args()
 # Put logging.basicConfig inside or configure it after parsing args:
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(
        level=log_level,
        format="[%(asctime)s] [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    
    repos = fetch_repo(args.user,args.limit)
    for r in repos:
        print(f"{r['name']} - ⭐ {r.get('stargazers_count', 0)}")
        
if __name__ == "__main__":
    main()