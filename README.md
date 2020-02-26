# Casting Agency

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

Roles:

- Casting Assistant
  - Can view actors and movies
- Casting Director
  - All permissions a Casting Assistant has and…
  - Add or delete an actor from the database
  - Modify actors or movies
- Executive Producer
  - All permissions a Casting Director has and…
  - Add or delete a movie from the database

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework.
- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM.
- [DOT-ENV](https://pypi.org/project/python-dotenv/) extension handling reading .env variables.

## Production

- View application hosted on heroku. `https://arty-agency.herokuapp.com`.
- To test endpoints you could use [Postman](https://www.postman.com/) with the collection [agency.postman_collection.json](agency.postman_collection.json)
- To test api using live documentation click [here](https://documenter.getpostman.com/view/2022116/SzKYNbdD)

## Database Setup

- Create a database and complete the database URL in .env.
- Apply db migrations using the command. `python manage.py db upgrade`.

## Environment variables

Create a .env file in following the example (.env_example). Ensure to put database url for the app to use and for testing.

## Running the server

Ensure you are working using your created virtual environment.

To run the server, execute:

```bash
python manage.py runserver
```

## API Documentation

- To test endpoints you can use [Postman](https://www.postman.com/).
- Alteratively you can use the live documentation. `https://documenter.getpostman.com/view/2022116/SzKYNbdD`.
- Click [here](https://arty-casting-agency.auth0.com/authorize?audience=casting_agency&response_type=token&client_id=WfeW4jT6hkaViJq1vc9cFtYULfeWqzaI&redirect_uri=http://localhost:8080/login-results) to view login page.

Casting assistant credentials.

```txt
email: assistant@example.com
password: asG8Bwqg!#
```

Casting director credentials.

```txt
email: director@example.com
password: gaKGS234Gal!@
```

Executive producer

```txt
email: producer@example.com
password: stGS12gzLoi74@$E
```

### Get '/actors'

- Fetchs a list of actors from the database.
- Request Arguments: None
- Required permission: `get:actors`.

Example of expected output.

``` json
{
    "actors": [
        {
            "age": 20,
            "gender": "Female",
            "id": 1,
            "movies_in": [
                {
                    "id": 1,
                    "title": "Tebatusasula"
                }
            ],
            "name": "Julie Ivans"
        },
        {
            "age": 25,
            "gender": "Male",
            "id": 2,
            "movies_in": [
                {
                    "id": 1,
                    "title": "Tebatusasula"
                }
            ],
            "name": "Matthew Bam"
        }
    ],
    "success": true
}
```

### Post '/actors'

- Creates a new actor and returns the id of the new actor.
- Required fields: name, age, gender.
- Required permission: `create:actors`.

Example of json data to post.

``` json
{
    "name": "John Doe",
    "age": 35,
    "gender": "Male"
}

Example of output.

``` json
{
    "actors": [
        {
            "age": 20,
            "gender": "Female",
            "id": 1,
            "movies_in": [
                {
                    "id": 1,
                    "title": "Tebatusasula"
                }
            ],
            "name": "Julie Ivans"
        },
        {
            "age": 25,
            "gender": "Male",
            "id": 2,
            "movies_in": [
                {
                    "id": 1,
                    "title": "Tebatusasula"
                }
            ],
            "name": "Matthew Bam"
        },
        {
            "age": 25,
            "gender": "Male",
            "id": 5,
            "movies_in": [],
            "name": "John Doe"
        }
    ],
    "created": 5,
    "success": true,
    "total_actors": 3
}
```

### Delete '/actors/<actor_id>'

- Deletes an actor from the database whose id has been specified.
- Example request. http://127.0.0.1:5000/actors/5
- HTTP method: Delete
- Required permission: `delete:actors`.

Example of output.

``` json
{
    "actor_list": [
        {
            "age": 20,
            "gender": "Female",
            "id": 1,
            "movies_in": [
                {
                    "id": 1,
                    "title": "Tebatusasula"
                }
            ],
            "name": "Julie Ivans"
        },
        {
            "age": 25,
            "gender": "Male",
            "id": 2,
            "movies_in": [
                {
                    "id": 1,
                    "title": "Tebatusasula"
                }
            ],
            "name": "Matthew Bam"
        }
    ],
    "deleted": 5,
    "success": true
}

```

### Get '/movies'

- Fetches a list of movies. Each formated as a dictionary.
- Required permission: `get:movies`.

Example of output.

``` json
{
    "movies": [
        {
            "cast": [
                {
                    "id": 2,
                    "name": "Matthew Bam"
                },
                {
                    "id": 1,
                    "name": "Julie Ivans"
                }
            ],
            "id": 1,
            "release_date": "Mon, 19 Oct 2020 00:00:00 GMT",
            "title": "Tebatusasula"
        },
        {
            "cast": [],
            "id": 2,
            "release_date": "Sun, 19 Jan 2020 00:00:00 GMT",
            "title": "Who killed Captain Alex"
        },
        {
            "cast": [],
            "id": 3,
            "release_date": "Sun, 19 Jan 2020 00:00:00 GMT",
            "title": "Coming to America"
        }
    ],
    "success": true
}
```

### Post /movies

- Creates a new movie.
- Required fields: title, release_date
- Required permission: `create:movies`.

Example json data to send.

``` json
{
    "title": "Coming to America",
    "release_date": "2020-1-19"
}
```

Example of output.

``` json
{
    "created": 4,
    "movies": [
        {
            "cast": [
                {
                    "id": 2,
                    "name": "Matthew Bam"
                },
                {
                    "id": 1,
                    "name": "Julie Ivans"
                }
            ],
            "id": 1,
            "release_date": "Mon, 19 Oct 2020 00:00:00 GMT",
            "title": "Tebatusasula"
        },
        {
            "cast": [],
            "id": 2,
            "release_date": "Sun, 19 Jan 2020 00:00:00 GMT",
            "title": "Who killed Captain Alex"
        },
        {
            "cast": [],
            "id": 3,
            "release_date": "Thu, 25 Jan 2001 00:00:00 GMT",
            "title": "Going to America"
        },
        {
            "cast": [],
            "id": 4,
            "release_date": "Sun, 19 Jan 2020 00:00:00 GMT",
            "title": "Secret life of pets"
        }
    ],
    "success": true,
    "total_movies": 4
}
```

### Patch /movies/<movie_id>

- Edits a movie with given id.
- Possible fields to edit: title, release_date.
- Required permission: `patch:movies`.

Example of json data to send.

```json
{
    "release_date": "2001-1-25"
}
```

Example of output.

```json
{
    "movies": [
        {
            "cast": [
                {
                    "id": 2,
                    "name": "Matthew Bam"
                },
                {
                    "id": 1,
                    "name": "Julie Ivans"
                }
            ],
            "id": 1,
            "release_date": "Mon, 19 Oct 2020 00:00:00 GMT",
            "title": "Tebatusasula"
        },
        {
            "cast": [],
            "id": 2,
            "release_date": "Sun, 19 Jan 2020 00:00:00 GMT",
            "title": "Who killed Captain Alex"
        },
        {
            "cast": [],
            "id": 3,
            "release_date": "Thu, 25 Jan 2001 00:00:00 GMT",
            "title": "Going to America"
        },
        {
            "cast": [],
            "id": 4,
            "release_date": "Thu, 25 Jan 2001 00:00:00 GMT",
            "title": "Secret life of pets"
        }
    ],
    "success": true
}
```

### Possible errors

1. 400 - Bad request. Request missing a required field.
2. 401 - Unauthorized. Authentication needed.
3. 403 - Forbidden. User does not have rights to perform action.
4. 404 - Resource not found.
5. 405 - Method not allowed on given endpoint.
6. 422 -  Request unprocessable.
7. 500 - Internal server error.

## Running tests

- Tokens for each role are needed to run tests.
- Click [here](https://arty-casting-agency.auth0.com/authorize?audience=casting_agency&response_type=token&client_id=WfeW4jT6hkaViJq1vc9cFtYULfeWqzaI&redirect_uri=http://localhost:8080/login-results) to view login page.

Casting assistant credentials.

```txt
email: assistant@example.com
password: asG8Bwqg!#
```

Casting director credentials.

```txt
email: director@example.com
password: gaKGS234Gal!@
```

Executive producer

```txt
email: producer@example.com
password: stGS12gzLoi74@$E
```

- Add the tokens from each of the above to the .env file following the .env_example.
- Create a test database and its database url to the .env file.
- Now you can run the command `pytest` to run the tests.


### Authors

- Nangai Arthur

### Acknowledgements

- Irzelindo Joaquim S
- Udacity
