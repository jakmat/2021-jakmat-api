```
docker build -t "jakmat-api" .
docker run --rm --mount type=bind,source="$(pwd)"/src,target=/src --name jakmat-api jakmat-api
```
