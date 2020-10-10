# Privado Backend Engineer Task

## Description

The project is made upon Docker with Django, Python and mongodb.

## Prerequisite

Docker installed
Python3.6

## How to run the project

1. Clone the project and Goto base directory privadoproj, Build the docker image.

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

5. The project is up and running. Curls to try are given below.

```
curl --location --request GET 'http://localhost:8000/te/customer/999/templates'

curl --location --request GET 'http://localhost:8000/te/customer/111/templates'

curl --location --request GET 'http://localhost:8000/te/customer/222/templates'

curl --location --request POST 'http://localhost:8000/te/customer/333/templates'

curl --location --request GET 'http://localhost:8000/te/customer/222/templates'
```

