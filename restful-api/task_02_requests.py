import requests
import csv


def fetch_and_print_posts():
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {r.status_code}")
    
    if r.status_code == 200:
        imprime = r.json()
        for p in imprime:
            print(p["title"])

def fetch_and_save_posts():
    rep = requests.get("https://jsonplaceholder.typicode.com/posts")
    
    if rep.status_code == 200:
        imp = rep.json()
        formjson = [{"id": p["id"], "title": p["title"], "body": p["body"]} for p in imp]

