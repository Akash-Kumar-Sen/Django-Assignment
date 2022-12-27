# Django-Assignment

## Installation

#### 1. Install Python
Install ```python-3.8.10``` and ```python-pip```. Follow the steps from the below reference document based on your Operating System.
Reference: [https://docs.python-guide.org/starting/installation/](https://docs.python-guide.org/starting/installation/)

#### 2.1 Setup virtual environment
python3 -m venv envname

#### 2.2 Activate virtual environment
```
source envname/bin/activate
```

#### 3. Clone git repository
```bash
git clone "https://github.com/Akash-Kumar-Sen/Django-Assignment.git"
```

#### 4. Install requirements
```bash
cd Django-Assignment/
pip install -r requirements.txt
```

#### 5. Run the server
```bash
# Make migrations
python manage.py makemigrations
python manage.py migrate

# Run the server
python manage.py runserver

# your server is up on port 8000
```
