
# Django Project Template

## Introduction
Create a website/application using Django using this template.

## Prerequisites
  - Windows 10/11 with WSL installed.
  - RHEL(AlmaLinux or RockyLinux or Fedora) Linux Desktop.

## Basic Setup
  - Login into your Liunx Desktop or WSL.
  - Install Homebrew as following with  user having sudo privileges.
```sh
$ whoami
user
```
```sh
$ sudo -l
```
```sh
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
<details>
  <summary><span style="color: red;">Expand</span></summary>

  - Edit and add the following in your user profile **~/.bashrc** or **~/.bash_profile** or **~/.profile**
```sh
$ cat ~/.bashrc
#
# Homebrew
#
eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
for FILE in $(ls /home/linuxbrew/.linuxbrew/etc/bash_completion.d/);
do
  . /home/linuxbrew/.linuxbrew/etc/bash_completion.d/$FILE;
done

# User specific environment
if ! [[ "$PATH" =~ "$HOME/.local/bin:$HOME/bin:" ]]; then
  PATH="$HOME/.local/bin:$HOME/bin:$(gem environment user_gemhome)/bin:$(gem environment gemdir)/bin:/home/linuxbrew/.linuxbrew/opt/libpq/bin:$PATH"
fi

#
# Virtualenvwrapper
#
export WORKON_HOME=$HOME/.venv
export PROJECT_HOME=$HOME/Projects
export VIRTUALENVWRAPPER_SCRIPT=/home/linuxbrew/.linuxbrew/bin/virtualenvwrapper.sh
source /home/linuxbrew/.linuxbrew/bin/virtualenvwrapper.sh
```

</details>

  - Logout and Login or open a new tab in your terminal.
```sh
$ brew install git libpq pre-commit bash-completion django-completion dotenvx/brew/dotenvx redis
```
  - Create the file as following and set the permission.
```sh
$ vim ~/.sshpass
my_user_password_sudo
$ chmod 0600 ~/.sshpass
```
```sh
$ sshpass sudo dnf -y install nss-tools certbot nginx rsync cronie crontabs cronie-anacron
$ brew install nss mkcert sshpass pipenv virtualenvwrapper nodejs pnpm
$ brew service start redis
$ redis-cli PING
PONG
$ export CAROOT=/etc/nginx/ssl
$ sshpass sudo chown user:user /etc/nginx/ssl
$ sshpass sudo chmod 0755 /etc/nginx/ssl
$ mkcert -install
$ mkcert -CAROOT
/etc/nginx/ssl
```

  - Import the **/etc/nginx/ssl/rootCA.pem** to your browser. **Example:** chrome://certificate-manager/
  - Create your project directory as following.
```sh
$ mkvirtualenv  dj_project_name
$ mkdir -pv $HOME/Projects/dj_project_name/ssl
$ cd $HOME/Projects/dj_project_name
$ mkcert -key-file ssl/key.pem \
    -cert-file ssl/cert.pem \
    domain.tld "*.domain.tld" \
    localhost 127.0.0.1 ::1
```
  - Now, install the django package and create project using this template.
```sh
$ workon dj_project_name
$ python -m pip install django
$ django-admin startproject --template=https://github.com/GaiusJuiliusCaesar/dj-project-template/archive/main.zip dj_project_name .
```
  - Then, edit and update the environment variables in **.env**
<details>
  <summary><span style="color: red;">Expand</span></summary>

```sh
$ ./generate_secret_key.py
*n^6=76@%pqtn(k2onh_@e%!psv@*dt08yv)vwdvmlqn6s628(
```
```sh
$ vim .env
#
# .env
#

#
# DATABASE URL
#
DATABASE_URL='postgresql://db_user:db_password@db-server.fqdn.tld/db_name?sslmode=require'

#
# SECRET_KEY
#
SECRET_KEY='*n^6=76@%pqtn(k2onh_@e%!psv@*dt08yv)vwdvmlqn6s628('

#
# ALLOWED_HOSTS
#
ALLOWED_HOSTS='localhost,domain.tld'

#
# DEBUG
#
DEBUG='True'

#
# ADMINS
#
ADMINS='Django Dev,djdev_0cba7@domain.tld'

#
# INTERNAL_IPS
#
INTERNAL_IPS='127.0.0.1,::1'

#
# CORS_ORIGIN_WHITELIST
#
CORS_ORIGIN_WHITELIST='https://localhost,https://domain.tld'

#
# CORS_ALLOW_METHODS
#
CORS_ALLOW_METHODS='GET,POST,PUT,DELETE'

#
# EMAIL_URL
#
EMAIL_URL='submission://SMTP_LOGIN_ID:SMTP_PASSWORD@sandbox.smtp.mailtrap.io/?_server_email=djdev_0cba7@domain.tld'

#
# DEFAULT_FROM_EMAIL
#
SERVER_EMAIL='djdev_0cba7@domain.tld'
DEFAULT_FROM_EMAIL='djdev_0cba7@domain.tld'

#
# CACHE_TIMEOUT
#
CACHE_TIMEOUT='60'

#
# CORS_ORIGIN_WHITELIST
#
CORS_ORIGIN_WHITELIST='https://localhost,https://domain.tld'

#
# CORS_ALLOW_METHODS
#
CORS_ALLOW_METHODS='GET,POST,PUT,DELETE'

#
# CSRF_TRUSTED_ORIGINS
#
CSRF_TRUSTED_ORIGINS='${CORS_ORIGIN_WHITELIST}'

#
# CACHE_URL
#
CACHE_URL='redis://127.0.0.1:6379/1'

#
# ADMIN LOGIN
#
DJANGO_SUPERUSER_USERNAME='djadmin'
DJANGO_SUPERUSER_EMAIL='projectadmin@domain.tld'
DJANGO_SUPERUSER_PASSWORD='Subheader8_Collide0_Width7_Postbox3_Flagstick3'

#
# SSL CERTIFICATE VERIFICATION
#
REQUESTS_CA_BUNDLE='${HOME}/.local/share/mkcert/rootCA.pem'
CURL_CA_BUNDLE='${REQUESTS_CA_BUNDLE}'
```

  - Encrypt the **.env** file as following.
```sh
$ dotenvx encrypt
# Do not push this file without encrypt it.
```
  - To create a seperate file for production use **.env.production** as mentioned in [Advance Dotenvx](https://dotenvx.com/docs/advanced/run-dotenv-private-key-multiple.html)
```sh
$ vim .env.production
$ dotenvx encrypt -f .env.production
# To decrypt (Do not push this file without encrypt it.)
$ dotenvx decrypt -f .env.production
```
```sh
# Copy the private keys to your Password Manager and delete the .env.keys.
$ rm -rf .env.keys
```

</details>

  - Add the following lines in file **/etc/hosts** in your **WSL** or **Linux Desktop**.
<details>
  <summary><span style="color: red;">Expand</span></summary>

```sh
$ cat /etc/hosts
#
# Development
#
127.0.0.1       localhost
127.0.0.1       domain.tld www.domain.tld
```

</details>

  - Add the following lines in file **C:\Windows\System32\drivers\etc\hosts** if your are using WSL.
<details>
  <summary><span style="color: red;">Expand</span></summary>

```powershell
$ Get-Content C:\Windows\System32\drivers\etc\hosts
#
# Development
#
127.0.0.1       localhost
127.0.0.1       domain.tld www.domain.tld
```

</details>

  - Install the required packages as following.
```sh
$ pipenv install
$ pipenv install --dev
```
  - Add the **DOTENV_PRIVATE_KEY** to your virtual environment postactive file in **~/.venv/dj_project_name/bin/postactivate** that you copied from **.env.keys** to your **Password Manager**.
```sh
$ vim ~/.venv/dj_project_name/bin/postactivate
export DOTENV_PRIVATE_KEY="your_development_private_key_you_find_in_dot_env_keys_file"
```
  - Update the file **~/.venv/dj_project_name/bin/postdeactivate**
```sh
$ vim ~/.venv/dj_project_name/bin/postactivate
unset DOTENV_PRIVATE_KEY
```
  - Deactivate and activate again as following.
```sh
$ deactivate
$ workon dj_project_name
```
  - Run the following command and verify the access using [localhost](https://localhost:8000) or your domain name [domain.tld](https://domain.tld:8000)
```sh
# Update the following file before verify the access.
$ vim ~/.venv/dj_project_name/lib/python3.12/site-packages/sslserver/management/commands/runsslserver.py
# Find and replace the following line.
self.socket = ssl.wrap_socket(self.socket, certfile=certificate, ...)
# With
class SecureHTTPServer(ThreadedWSGIServer):
    def __init__(self, address, handler_cls, certificate, key, ipv6=False):
        .......
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain(certfile=certificate, keyfile=key)
        self.socket = context.wrap_socket(self.socket, server_side=True)

# Reference: https://github.com/teddziuba/django-sslserver/issues/111#issuecomment-2439592643

```
```sh
$ dotenvx run -- python manage.py runsslserver \
    --certificate ssl/cert.pem \
    --key ssl/key.pem
```

## To run development server in SSL Port 443.

  - Then, add the following lines in your project virtual environment profile **~/.venv/dj_project_name/bin/postactivate**
```sh
$ cat ~/.venv/dj_project_name/bin/postactivate
#
# Alias to run development server in SSL Port 443
#
alias sshpass="sshpass -f ~/.sshpass"
alias runsslserver="sshpass sudo \
  DOTENV_PRIVATE_KEY=your_development_private_key_you_find_in_dot_env_keys_file \
  /home/linuxbrew/.linuxbrew/bin/dotenvx run -- \
  /home/user/.Envs/DJPT/bin/python manage.py runsslserver \
  --certificate ssl/cert.pem \
  --key ssl/key.pem \
  127.0.0.1:443"
```
  - Update the file **~/.venv/dj_project_name/bin/postdeactivate**
```sh
$ cat ~/.venv/dj_project_name/bin/postdeactivate
unset DOTENV_PRIVATE_KEY
unalias sshpass
unalias runsslserver
```
  - Logout and Login or open a new tab
```sh
$ cd $HOME/Projects/dj_project_name
$ runsslserver
[dotenvx@1.20.0] injecting env (14) from .env
Watching for file changes with StatReloader
Validating models...

System check identified no issues (0 silenced).
December 13, 2024 - 17:36:35
Django version 5.1.4, using settings 'dj_project_name.settings'
Starting development server at https://127.0.0.1:443/
Using SSL certificate: ssl/cert.pem
Using SSL key: ssl/key.pem
Quit the server with CONTROL-C.
```
  - Verify the access using [localhost](https://localhost) or your domain name [domain.tld](https://domain.tld)

## SSL and Nginx Setup
  - Run the following command to get your SSL certificate.
```sh
$ sshpass sudo certbot certonly --manual --preferred-challenges dns-01 \
	--domains domain.tld --domains *.domain.tld \
	--email your_email_id@domain.tld \
	--agree-tos --no-eff-email
```
```sh
# Validate
$ sshpass sudo certbot certificates
```
  - Add the **nginx** service user to your user group.
```sh
$ sshpass sudo usermod -a -G $(whoami) nginx
$ getent group $(whoami)
user:x:1000:user,nginx
```
  - Change the permission of your user home directory
```sh
$ chmod 0710 /home/user
```
  - Create the following log directory set permissions and ownership.
```sh
$ sshpass sudo mkdir -pv /var/log/gunicorn
$ sshpass sudo chmod 0711 /var/log/gunicorn
$ sshpass sudo chown user:nginx /var/log/gunicorn
```
  - Create the following logrotate file.
```sh
$ cat /etc/logrotate.d/gunicorn
/var/log/gunicorn/*.log {
  rotate 12
  weekly
  compress
  missingok
  notifempty
}
```
  - Then, create the following directory and copy systemd service and nginx files as following. Update your path and accordingly in the configuration files.
```sh
$ sshpass sudo mkdir -pv /etc/nginx/ssl /etc/nginx/htpasswd /var/www/default
$ sshpass sudo openssl dhparam -out /etc/nginx/ssl/dhparams.pem 4096
$ sshpass sudo cp -av /home/user/.local/share/mkcert/rootCA.pem /etc/nginx/ssl/
$ cd $HOME/Projects/dj_project_name
$ sshpass sudo cp -av ssl/*.pem /etc/nginx/ssl/
$ sshpass sudo rsync -Pavz misc/nginx/etc/ /etc/nginx/
$ sshpass sudo rsync -Pavz misc/nginx/default/ /var/www/default/
$ sshpass sudo rsync -Pavz misc/gunicorn/ /etc/systemd/system/
```

```sh
$ vim ~/.venv/dj_project_name/bin/envfile
DOTENV_PRIVATE_KEY=your_development_private_key_you_find_in_dot_env_keys_file

# Edit and set the correct path and user names in the systemd service files.
$ sshpass sudo vim /etc/systemd/system/gunicorn.service
$ sshpass sudo vim /etc/systemd/system/gunicorn.socket
# Create a user (Change the name) to protect the admin.
$ sudo htpasswd -c /etc/nginx/htpasswd/.htpasswd user1
# Edit and set the correct path and user names in the configuration files.
# Update allow IP address to access the admin
$ sshpass sudo vim /etc/nginx/conf.d/vh_domain.tld.conf
```
  - Then, reload and start the service.
```sh
$ sshpass sudo systemctl daemon-reload
$ sshpass sudo systemctl enable gunicorn.socket nginx.service
$ sshpass sudo systemctl start gunicorn.socket gunicorn.service nginx.service
```
  - Run the following commands
```sh
$ npm install -D tailwindcss
$ npm install flowbite
$ npx tailwindcss build
$ dotenvx run -- python manage.py collectstatic --noinput
$ dotenvx run -- python manage.py createsuperuser --noinput
$ dotenvx run -- python manage.py compress --force
$ dotenvx run -- python manage.py makemigrations
$ dotenvx run -- python manage.py migrate
$ dotenvx run -- python manage.py crontab add
$ dotenvx run -- python manage.py crontab show
```
  - Verify your django project app via curl and in your browser.
```sh
$ curl https://domain.tld
...
<title>Home</title>
...
```
```sh
$ curl -I --http2 https://domain.tld
HTTP/2 200
...
x-page-generation-duration-ms: 1
...
```

## About HTTP/3
  - You need to enable in your browser **chrome://flags#enable-quic** or **edge://flags/#enable-quic**
  - For security reasons this is disabled by default.

## Check Error logs
  - Run the following command.
```sh
$ sshpass sudo tail -fn0 /var/log/gunicorn/django.log /var/log/nginx/domain.tld.error.log /var/log/nginx/domain.tld.access.log
==> /var/log/gunicorn/django.log <==

==> /var/log/nginx/domain.tld.error.log <==

==> /var/log/nginx/domain.tld.access.log <==
```

## Enable and Disable Debug mode.
  - Run the following command to get the **DEBUG** status.
```sh
$ dotenvx get DEBUG
False
```
  - To enable the **DEBUG** mode.
```sh
$ dotenvx set DEBUG True
✔ set DEBUG with encryption (.env)
```
```sh
$ dotenvx get DEBUG
True
```
  - Then, stop the Nginx and Gunicorn service.
```sh
$ sshpass sudo systemctl stop nginx gunicorn.socket gunicorn.service
```
  - Run the development server to fix your issues.
```sh
$ runsslserver
```

## Conclusion
That is it! You are ready to make changes in your project. Happy Coding!!
