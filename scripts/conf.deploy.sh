#scp -r ../proxy/nginx/sites-available/default root@185.201.115.103:/etc/nginx/sites-available;
ssh root@185.201.115.103 "
  sudo systemctl restart nginx;
  sudo systemctl restart api;
  curl http://127.0.0.1/
"
# $ sudo ln -s /etc/nginx/sites-available/new_app /etc/nginx/sites-enabled/