import os
import unittest
import sys, json 
import requests as r

from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Actor, Movie




class CapstoneTestCase(unittest.TestCase):
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = os.environ['DATABASE_URL']
        self.EXECUTIVE_PRODUCER = os.environ['EXECUTIVE_PRODUCER']
        self.CASTING_DIRECTOR = os.environ['CASTING_DIRECTOR']
        self.CASTING_ASSISTANT = os.environ['CASTING_ASSISTANT']
    
    #binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
    #create all tables
            self.db.create_all()

    def teardown(self):
        """Executed after each test"""
        pass

    def test_health(self):
        #Test for GET health endpoint
        res = self.client().get('/')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['message'], 'Finally, it works!!!')

    ##TEST FOR ACTORS

    def test_get_actors_without_token(self):
        #res = self.client().get('http://localhost:5000/actors')
        res = r.get('http://localhost:5000/actors')
        print(res)
        #data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        #self.assertEqual(data['success'], False)
       

    def test_get_actors_with_valid_token(self):
        res = self.client().get(
            '/actors',
            headers={
                "Authorization": "Bearer" + self.CASTING_ASSISTANT
            }
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_get_particular_actor_without_token(self):
        res = self.client().get('/actors/5')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_get_particular_actor_with_valid_token(self):
        res = self.client().get(
            '/actors/5',
            headers={
                "Authorization": "Bearer" + self.CASTING_ASSISTANT
            }
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_create_actors_without_token(self):
        self.new_actor = {
            "name": "new name",
            "age": "new age",
            "gender": "gender"
        }
        res = self.client().post('/actors/')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_create_actor_with_valid_token(self):
        self.new_actor = {
            "name": "new name",
            "age": "new age",
            "gender": "gender"
        }
        res = self.client().post(
            '/actors/7',
            headers={
                "Authorization": "Bearer" + self.CASTING_DIRECTOR
            }
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_patch_actors_without_token(self):
        self.new_actor = {
            "name": "new name",
            "age": "new age",
            "gender": "gender"
        }
        res = self.client().patch('/actors/4')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_patch_actor_with_valid_token(self):
        self.new_actor = {
            "name": "new name",
            "age": "new age",
            "gender": "gender"
        }
        res = self.client().patch(
            '/actors/4',
            headers={
                "Authorization": "Bearer" + self.CASTING_DIRECTOR
            }
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_actor_without_token(self):
        res = self.client().delete('/actors/3')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_delete_actor_with_valid_token(self):
        res = self.client().delete(
            '/actors/3',
            headers={
                "Authorization": "Bearer" + self.CASTING_DIRECTOR
            }
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    #### TESTS FOR MOVIES

    def test_get_movies_without_token(self):
        res = self.client().get('/movies/')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_get_movies_with_valid_token(self):
        res = self.client().get(
            '/movies',
            headers={
                "Authorization": "Bearer" + self.CASTING_ASSISTANT
            }
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_get_particular_movie_without_token(self):
        res = self.client().get('/movies/5')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_get_particular_movie_with_valid_token(self):
        res = self.client().get(
            '/movies/5',
            headers={
                "Authorization": "Bearer" + self.CASTING_DIRECTOR
            }
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_create_movies_without_token(self):
        self.new_movie = {
            "title": "new title",
            "release_year": "year"
        }
        res = self.client().post('/moviess/')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_create_movie_with_valid_token(self):
        self.new_movie = {
            "title": "new title",
            "release_year": "year"
        }
        res = self.client().post(
            '/movies/7',
            headers={
                "Authorization": "Bearer" + self.EXECUTIVE_PRODUCER
            }
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_patch_movies_without_token(self):
        self.new_movie = {
            "title": "new title",
            "release_year": "year"
        }
        res = self.client().patch('/movies/1')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_patch_movie_with_valid_token(self):
        self.new_movie = {
            "title": "new title",
            "release_year": "year"
        }
        res = self.client().patch(
            '/movies/4',
            headers={
                "Authorization": "Bearer" + self.EXECUTIVE_PRODUCER
            }
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_movie_without_token(self):
        res = self.client().delete('/movies/3')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_delete_movie_with_valid_token(self):
        res = self.client().delete(
            '/moviess/3',
            headers={
                "Authorization": "Bearer" + self.EXECUTIVE_PRODUCER
            }
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main(verbosity=2)




    


    

    
