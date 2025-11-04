import pytest
import requests

class TestApi:

   @pytest.fixture()
   def obj_id(self):
      payload = {
         "name": "Apple MacBook Pro 16",
         "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
         }
      }
      response = requests.post('https://api.restful-api.dev/objects', json=payload)
      object_id = response.json()['id']
      yield object_id
      requests.delete('https://api.restful-api.dev/objects/{}'.format(object_id))


   def test_create_object(self,obj_id):
      payload  = {
      "name": "Apple MacBook Pro 16",
      "data": {
         "year": 2019,
         "price": 1849.99,
         "CPU model": "Intel Core i9",
         "Hard disk size": "1 TB"
      }
      }

      response = requests.post('https://api.restful-api.dev/objects',json=payload)
      self.object_id = response.json()['id']
      assert response.status_code == 200


   def test_get_object(self,obj_id):
      response = requests.get('https://api.restful-api.dev/objects/{}'.format(obj_id))
      assert response.status_code == 200

   def test_put_object(self,obj_id):
      payload = {
         "name": "Apple MacBook Pro 16",
         "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
         }
      }
      response = requests.put('https://api.restful-api.dev/objects/{}'.format(obj_id), json=payload)
      assert response.status_code == 200


   def test_delete_object(self,obj_id):
      response = requests.delete('https://api.restful-api.dev/objects/{}'.format(obj_id))
      assert response.status_code == 200
      get_response = requests.get('https://api.restful-api.dev/objects/{}'.format(obj_id))
      assert get_response.status_code == 404

