This is a three model Django project that contains school objects, classroom objects, and student objects.  A student can belong only to one classroom and a classroom only relates to a single school.

You can run it using the following command:
python manage.py runserver


For database migrations, use these commands:
python manage.py makemigrations

and then,

python manage.py migrate


You can access the admin by going to

http://localhost:8000/admin/

and you peform the crud operations there.