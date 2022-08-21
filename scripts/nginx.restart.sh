ssh root@185.201.115.103 "
  sudo nginx -t
  sudo systemctl restart nginx;
  #sudo systemctl restart api;
  #sudo systemctl restart fastapi;
  sudo systemctl status nginx;
  curl http://127.0.0.1/
"