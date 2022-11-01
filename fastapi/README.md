```
docker build -t jakmat-api .
docker run -d --rm -p 5050:5050 --name jakmat-api jakmat-api
```
### Test locally: 
http://0.0.0.0:5050/observation?objects=moon&time=1650773000&lat=52n&lon=19e

### Test remotely: 
http://185.201.115.103:5050/observation?objects=moon&time=1650773000&lat=52n&lon=19e