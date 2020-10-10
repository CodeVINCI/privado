# Privado Backend Engineer Task

## Description

The project is made upon Docker with Django, Python and mongodb.

## How to run the project

1. Goto base directory privadoproj, Build the docker image.

```
* docker-compose build
```

2. Start the servers.

```
* docker-compose up
```

3. Insert Initial templates to DB.

```
docker-compose run web /usr/local/bin/python manage.py initdb
```

4. Run the tests.

```
docker-compose run web /usr/local/bin/python manage.py test te
```

5. The project is up and running.


