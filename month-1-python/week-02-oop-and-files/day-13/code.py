# Day 13: Code Implementation
# CLI GitHub Profile & Public API Fetcher
# Write your implementation here independently.
import requests

def fetch_github_user(username:str) -> dict | None:
    try:
        res = requests.get(f"https://api.github.com/users/{username}",timeout=5)
        status_code = res.status_code
        if status_code == 200:
            data = res.json()
            return data
        elif status_code == 404:
            print("User not found.")
            return None
        elif status_code == 403|429:
             print("Rate limit exceeded")
             return None
        else:
            print ('Unexpected status')
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e} ")

def display_profile(data:dict) -> None:
    print(f"""
    =============================== \n
    Github Profile : {data['name']} \n
    Bio : {data['bio']} \n
    Public Repos : {data['public_repos']} \n
    Followers : {data['followers']} \n
    following : {data['following']} \n
    Profile URL : {data['html_url']} \n
    """)


def main():
    username = input("Enter Github username: ")
    res = fetch_github_user(username)
    display_profile(res)


main()