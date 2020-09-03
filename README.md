# recipesNet

Red social para compartir recetas de cocina.

## Dependencias

* Python 3.0 >=
* Django 3.0.9
* Phython 3.6.9
* PostgreSQL 10

### Instalación de dependencias

```bash
$ python3 -m pip install Django
$ sudo apt-get install postgresql postgresql-contrib
$ sudo pip3 install psycopg2-binary
$ sudo pip install Pilow
```
### Configuración de la base de datos
```bash
$ sudo su postgres
$ psql
$ CREATE DATABASE recipesNet;
$ CREATE USER admin WITH PASSWORD "admin";
$ GRANT ALL PRIVILEGES ON DATABASE recipesNet to admin;
$ ALTER USER admin CREATEDB;
```


### Ejecución

```bash
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
August 04, 2020 - 02:23:37
Django version 3.0.9, using settings 'recipesNet.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

```

### Detalles pendientes

* Mejorar las vistas con CSS.
* Añadir los permisos de rol en cada función para cada rol.
* Añadir la opción de ver recetas favoritas.
