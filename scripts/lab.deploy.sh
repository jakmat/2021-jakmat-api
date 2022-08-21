scp ../api.wsgi root@185.201.115.103:/var/www/api;
scp ../app.py root@185.201.115.103:/var/www/api;
scp ../requirements.txt root@185.201.115.103:/var/www/api;
scp -r ../src root@185.201.115.103:/var/www/api;
ssh root@185.201.115.103 "
  sudo systemctl restart nginx;
  sudo systemctl restart api;
  curl http://127.0.0.1:5000/test
"