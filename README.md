```
docker build -t "jakmat-api" -f dev.Dockerfile .
docker run --rm --mount type=bind,source="$(pwd)"/src,target=/src --name jakmat-api jakmat-api
```
