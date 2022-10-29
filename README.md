### Local development
```
docker build -t "jakmat-api" -f dev.Dockerfile .
docker run --rm --mount type=bind,source="$(pwd)"/src,target=/src --name jakmat-api jakmat-api
```
### Remote deployment
```
docker build -t "jakmat-api" -f Dockerfile .
docker run -d --rm -p 5000:5000 --name jakmat-api jakmat-api
```