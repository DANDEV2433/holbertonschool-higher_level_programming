#!/usr/bin/python3
"""
Consuming and processing data from an API using Python
"""
import csv
import requests


def fetch_and_print_posts():
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {r.status_code}")
    if r.status_code == 200:
        posts = r.json()
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {r.status_code}")
    if r.status_code == 200:
        # Analyse données JSON de la réponse et stocke dans la variable posts.
        posts = r.json()
        new_posts = [
            {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            }for post in posts
        ]
    with open('post.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ["id", "title", "body"]
        # Crée un objet DictWriter qui utilise les noms des colonnes définis.
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(new_posts)


fetch_and_print_posts()
fetch_and_save_posts()
