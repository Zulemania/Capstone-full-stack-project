## CASTING AGENCY API

## Introduction

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies.  The Casting agency API supports the agency by allowing users to query the database for movies and actors. There are three different roles and each has a set of related permissions attached to them.

These Roles include:
1. Casting Assistant
    - Can view actors and movies
2. Casting Director
    - All permiissions a Casting Assistant has and...
    -  Add or delete an actor from the database
    - Modify actors or movies
3. Executive Producer
    - All permissions the Casting Director has and...
    - Add or delete a movie from the database

I developed this project to use all the concepts and skill that I acquired in this programme to build an API and host it. By doing so, I gained more confidence in these skills.

## Capstone Project for Udacity's Full Stack Developer Nanodegree

Heroku link: https://film-magic.herokuapp.com/

Local host link: http://127.0.0.1:5000/

##SETUP

## Installinq Dependencies

1. **Python 3.9.8** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


2. **Virtual Environment** - We recommend working within a Virtual environment whenever using Python for projects. This keeps the dependencies for each project seperate and organized. Instructions for setting up a virtual environment can be found in [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once you have your virtual environment setup and running, install dependencies by runnung:
```bash
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.


4. **Key Dependencies**
 - [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

 - [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

 - [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

### Deploy on Heroku
 - Create app in heroku
 - Set your environment variables
 - Define your Procfile
 - Push your code to github
 - Connect your repository to heroku
 - Click on deploy option

### Running the server

First, you have to start the postgresql swrvice by running the following command

```bash
brew services start postgresql
```

Then, createdb by running
```
dropdb capstone
createdb capstone
```

From within the ./capstone directory first ensure you are working within your created virtual environment.

Each time you open a new terminal session, run:

```bash
export DATABASE_URL=postgresql:cynthiachisom@localhost:5432/capstone
export FLASK_APP=app.py;
export AUTH0_DOMAIN='capstone-projekt.us.auth0.com'
export ALGORITHMS=['RS256']
export API_AUDIENCE='magic'
export CLIENT_ID='06lGES4xRP9Z7cZu6Uyj52iyK7bCq5Pw'
```

To run the server, execute:

```bash
export FLASK_ENV=development
flask run
```

The `FLASK_ENV` variable to `development` flag will detect file changes and restart server automatically.


## Endpoints

GET '\'
- root endpoint
- requires no authentication
- Example request: https://film-magic.herokuapp.com/
- Example response
{
    "success": true,
    "message":"Finally, it works!!!"
}
```