 Create Virtual Environment
# Mac
python3 -m venv venv
source venv/bin/activate
# Windows
python3 -m venv venv
.\venv\Scripts\activate.bat

- Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

- Migrate to database
python manage.py migrate
python manage.py createsuperuser

- Run application
python manage.py runserver

