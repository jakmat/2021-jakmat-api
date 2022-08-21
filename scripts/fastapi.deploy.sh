scp ../fastapi/app.py root@185.201.115.103:/var/www/fastapi
ssh root@185.201.115.103 "
  cd /var/www/fastapi
  source venv/bin/activate
  pip install gunicorn
  gunicorn app:app -k uvicorn.workers.UvicornWorker
  curl http://localhost:8000
"
