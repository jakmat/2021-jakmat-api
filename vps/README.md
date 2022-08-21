# VPS configuration
Essential steps for setting up a Virtual Private Server.
Applicable to Ubuntu Server 20.04 x86_64.
## First login
Create new SSH key pair, for instance `id_rsa_vps`
```
cd ~/.ssh
ssh-keygen -t rsa -b 4096
```
Log into VPS using password
```
ssh root@<vps_ip>
```
## System update
Update package list
```
sudo apt update
```
Update the packages
```
sudo apt upgrade
```
## Custom SSH port
Edit SSH configuration file
```
nano /etc/ssh/sshd_config
```
Change `Port 22` to one within 49152 and 65535 range.
```
Port <custom_port_number>
```
Restart SSH
```
systemctl restart ssh
```
Logout and login using new port
```
exit
ssh root@<vps_ip> -p <custom_port_number>
```
# SSH authorization 
Create .ssh directory
```
mkdir .ssh
```
Create `authorized_keys` file
```
touch .ssh/authorized_keys
```
Logout
```
exit
```
Copy SSH key to VPS authorized keys, authorize using password for the last time
```
cat ~/.ssh/id_rsa_vps.pub | ssh root@<vps_ip> 'cat >> .ssh/authorized_keys && echo "Key copied"'
```
Logout and login without password prompt
```
exit
ssh root@<vps_ip>
```
## Password authorization removal
Edit SSH configuration file
```
nano /etc/ssh/sshd_config
```
Remove password authentication by changing `PermitRootLogin` value from `yes` to `no`
```
PermitRootLogin no
```
Restart SSH
```
systemctl restart ssh
```
## Non-root user creation
Add new user and create account password
```
sudo adduser <username>
```
Logout
```
exit
```
Login as new user and enter password
```
ssh <username>@<vps_ip> -p <custom_port_number>
```