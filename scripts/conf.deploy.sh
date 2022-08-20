scp -r ../conf/default root@185.201.115.103:/etc/nginx/sites-available;
ssh root@185.201.115.103 "
  sudo systemctl restart nginx;
  sudo systemctl restart api;
  curl http://127.0.0.1/
"