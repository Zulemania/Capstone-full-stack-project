import os
import unittest
import sys, json 
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
    
    #binds the app to the current context
    with self.app.app_context():
        self.db = SQLAlchemy()
        self.db.init(self.app)
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
        self.assertEqual(data['message'], 'Alive!!!')

#Make the tests convieniently executable
if __name__ == "__main__":
    unittest.main()
