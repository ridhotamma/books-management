## aplikasi manajemen buku
aplikasi ini dibuat menggunakan django

## table yg ada di dalamnya
- publishers
- author
- book
- store

## cara menjalankan
- pip install virtualenv
- virtualenv book_env
- source ./book_env/bin/activate
- pip install -r requirements.txt
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver
