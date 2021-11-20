import os
import unittest
import json 
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Actor, Movie

class CapstoneTestCase(unittest.TestCase):
    def setUp(self):
        self.CASTING_ASSISTANT = os.environ['CASTING_ASSISTANT']
        self.CASTING_DIRECTOR = os.environ['CASTING_DIRECTOR']
        self.EXECUTIVE_PRODUCER = os.environ['EXECUTIVE_PRODUCER']

        self.app = create_app()
        self.client = self.app.test_client
        setup_db(self.app)

        self.new_actor = {
            "name": "Denzel",
            "age": 66,
            "gender": 'M'
        }

        self.new_movie = {
            "title": "The Equalizer",
            "realease_year": 2014
        }

    with self.app.app_context():
        self.db = SQLAlchemy()
        self.db.init(self.app)

        self.db.create_all()

    def teardown(self):
        pass

    def test_health(self):
        res = self.client().get('/')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['message'], 'Alive!!!')

## TESTS FOR ACTORS

    def test_get_actors_without_token(self):
        res = self.client().get('/actors')
        self.assertEqual(res.status_code, 401)

    def test_get_actors_with_valid_token(self):
        res = self.client().get('/actors', 
        headers={
            "Authorizaton": f"Bearer {self.CASTING_DIRECTOR}"})
        self.assertEqual(res.status_code, 200)

    def test_get_particular_actor_without_token(self):
        res = self.client().get('/actors/3')
        self.assertEqual(res.status_code, 401)

    def test_get_particular_actor_with_valid_token(self):
        res = self.client().get('/actors', 
        headers={
            "Authorizaton": f"Bearer {self.CASTING_DIRECTOR}"})
        self.assertEqual(res.status_code, 200)

    def test_create_actors_without_token(self):
        res = self.client().post('/actors', json=self.new_actor)
        self.assertEqual(res.status_code, 401)

    def test_create_actors_with_valid_token(self):
        res = self.client().post('/actors', 
        headers={
            "Authorizaton": f"Bearer {self.CASTING_DIRECTOR}"}, 
            json=self.new_actor)
        self.assertEqual(res.status_code, 200)

    def test_patch_actors_without_token(self):
        res = self.client().patch('/actors/3', json=self.new_actor)
        self.assertEqual(res.status_code, 401)

    def test_patch_actors_with_valid_token(self):
        res = self.client().patch('/actors/3', 
        headers={
            "Authorizaton": f"Bearer {self.CASTING_DIRECTOR}"}, 
            json=self.new_actor)
        self.assertEqual(res.status_code, 200)

    def test_delete_actors_without_token(self):
        res = self.client().delete('/actors/5')
        self.assertEqual(res.status_code, 401)

    def test_delete_actors_with_valid_token(self):
        res = self.client().delete('/actors/5', 
        headers={
            "Authorizaton": f"Bearer {self.CASTING_DIRECTOR}"})
        self.assertEqual(res.status_code, 200)


## TESTS FOR MOVIES




    

    

    

    


    




    
