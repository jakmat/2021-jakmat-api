cd /var/www/jakmat-api
echo '### Restarting services'
docker stop jakmat-api
docker build -t jakmat-api .
docker run -d --rm -p 5050:5050 --name jakmat-api jakmat-api
systemctl restart nginx
echo '#### Restart successful'