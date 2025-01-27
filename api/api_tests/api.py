import requests

class PublicApi:
     def get_something(self, base_url, endpoint):
         response = requests.get(f"{base_url}/{endpoint}")
         return response

     def get_somthing_by_id(self, base_url, endpoint, id):
         response = requests.get(f"{base_url}/{endpoint}/{id}")
         return response

     def post_something(self, base_url, endpoint, data):
         response = requests.post(f"{base_url}/{endpoint}", json=data)
         return response

     def put_something(self, base_url, endpoint, data):
         response = requests.put(f"{base_url}/{endpoint}", data=data)
         return response

     def delete_something(self, base_url, endpoint, id):
         response = requests.delete(f"{base_url}/{endpoint}/{id}")
         return response