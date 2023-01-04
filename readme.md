# Setup
```
python.exe -m venv .venv
. .\.venv\Scripts\activate
pip install -r requirements.txt
```

# Generate new requirements.txt file
`pip freeze > .\requirements.txt`

# YOLO upgrading all packages
```
$(pip list --outdated) -split("`r`n") | select -skip 2 | foreach { $package = $_.split(" ")[0]; pip install $package --upgrade; }
```