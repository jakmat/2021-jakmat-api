# fix for Flask dependency: Markupsafe
cd /var/www/api/lib/python3.6/site-packeges
wget https://cbs.centos.org/kojifiles/packages/python-markupsafe/1.1.0/2.el7/x86_64/python2-markupsafe-1.1.0-2.el7.x86_64.rpm
sudo yum localinstall python2-markupsafe-1.1.0-2.el7.x86_64.rpm
