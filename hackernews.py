import click
import requests
import json
import jsonschema

BASE_URL = 'https://hacker-news.firebaseio.com/v0/'

# Loading required JSON schema for validation
with open('post_schema.json', 'r') as f:
    schema_data = f.read()
schema = json.loads(schema_data)

@click.command()
@click.option(
    '--posts',
    '-p',
    default=1,
    help='Number of posts to display from Hackernews',
    type=int
    )
def hackernews(posts: int):
    if posts > 100 or posts < 1:
        print("Please select a number between 1 and 100")
        return

    response = requests.get(url=f'{BASE_URL}topstories.json')

    # Return the JSON-encoded content of this response
    post_ids = response.json()

    # Create an empty list which will store our posts
    requested_posts = []

    for i, post_id in enumerate(post_ids):
        if i == posts:
            break

        try:
            post = requests.get(url=f'{BASE_URL}item/{post_id}.json').json()

            # Validating JSON response from hackernews against our json schema
            jsonschema.validate(post, schema)

            requested_posts.append(
            {
                'title': post['title'],
                'uri': post['url'],
                'author': post['by'],
                'points': post['score'],
                'comments': post['descendants'],
                'rank': post_ids.index(post_id) + 1
                }
            )

        # If the JSON validation fails, print error message.
        except jsonschema.exceptions.ValidationError as e:
            print("invalid JSON:", e)


    # Print our JSON output with indent set to 4 so the formatting is clearer
    print(json.dumps(requested_posts, indent = 4))


if __name__ == '__main__':
    hackernews()
