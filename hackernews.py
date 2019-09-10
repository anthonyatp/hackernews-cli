import click
import requests
import json

BASE_URL = 'https://hacker-news.firebaseio.com/v0/'

@click.command()
@click.option('--posts', '-p', default=1, help='Number of posts to display from Hackernews')
def hackernews(posts: int):
    response = requests.get(url=f'{BASE_URL}topstories.json')
    post_ids = response.json()
    requested_posts = []

    for post_id in post_ids:
        if len(requested_posts) == posts:
            break

        post = requests.get(url=f'{BASE_URL}item/{post_id}.json').json()
        requested_posts.append(
            {
                'title': post['title'],
                'uri': post['url'],
                'author': post['by'],
                'points': post['score'],
                'comments': len(post['kids']),
                'rank': post_ids.index(post_id) + 1
                }
        )
    
    print(json.dumps(requested_posts, indent = 4))
    

if __name__ == '__main__':
    hackernews()
