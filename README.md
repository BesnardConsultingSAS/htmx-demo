
# Django HTMX setup
If you're on Ubuntu 20.04, run the following command to install the app using python 3.10

```bash
sudo apt install python3.10-distutils
python3.10 -m virtualenv venv
source venv/bin/activate
curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10
poetry install
python manage.py migrate
```