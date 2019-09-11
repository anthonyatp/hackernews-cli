FROM python:3.6

COPY . /hackernews-cli
WORKDIR /hackernews-cli

RUN pip install -r requirements.txt
ENTRYPOINT ["python", "hackernews.py"]
