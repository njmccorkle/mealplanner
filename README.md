# Setup
```
python.exe -m venv .venv
. .\.venv\Scripts\activate
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
python .\manage.py migrate
python .\manage.py createsuperuser
python .\manage.py runserver

```

# Generate new requirements.txt file
`pip freeze > .\requirements.txt`

# Dump data from Django DB
`python.exe .\manage.py dumpdata --exclude=auth --exclude=sessions --exclude=contenttypes --exclude=admin --output .\sample_data\sample_data.json`
# Load data to Django DB
`python.exe .\manage.py loaddata .\sample_data\sample_data.json`


# YOLO upgrading all packages
```
$(pip list --outdated) -split("`r`n") | select -skip 2 | foreach { $package = $_.split(" ")[0]; pip install $package --upgrade; }
```