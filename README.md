# hackernews-cli

This is a simple command line application that outputs the top posts from hackernews in JSON.

```bash
git clone https://github.com/anthonyatp/hackernews-cli.git
cd hackernews-cli
```


## Run using Docker
### Prerequisites
* Download and install [Docker](https://www.docker.com/community-edition#/download)

### Build
To build this app, simply run:

```bash
docker build -t hackernews-cli .
```

### Run & Usage
```bash
docker run hackernews-cli
```

By default, the above command will return the top post from hackernews. Or you can use:

```text
Options:

-p, --posts  The number of posts to return from hackernews (between 1 and 100)
```

For example:

```bash
docker run hackernews-cli --posts 3
```

## Run withour using Docker

### Install dependencies
```bash
pip -r install requirements.txt
```

### Run & Usage
```bash
python3 hackernews.py
```

By default, the above command will return the top post from hackernews. Or you can use:

```text
Options:

-p, --posts  The number of posts to return from hackernews (between 1 and 100)
```

For example:

```bash
python3 hackernews.py --posts 3
```


## Packages/Libraries used

* pytest: A testing framework which allows us to write test codes using python. I chose this because I have used it before - very easy to start with because of its simple and easy syntax.

* jsonschema: This is to define our required structure to validate the json responses we receive from hackernews

* click: This is to create command line interfaces in a composable way with as little code as necessary.

* requests: This is simply so we can send get requests to the hackernews api