import requests
import json
from scripts.api.utils import fake_login_api_return_token


class APICaller:
    __BASEURL = 'https://gorest.co.in/public-api'

    def get_header(self):
        token = fake_login_api_return_token()
        return {'Authorization': 'Bearer {}'.format(token),
                'Content-Type': 'application/json',
                'Accept': 'application/json'}

    def _get(self, path, params=None, headers=None):
        if params is None:
            params = {}
        resp = requests.get(self.__BASEURL + path, params=params,
                            headers=headers)
        if resp.status_code == 200:
            return json.loads(resp.content)
        return resp

    def _delete(self, path, params=None, headers=None):
        if params is None:
            params = {}
        resp = requests.delete(self.__BASEURL + path, params=params,
                               headers=headers)
        if resp.status_code == 200:
            return json.loads(resp.content)
        return resp

    def _post(self, path, json=None, headers=None):
        resp = requests.post(self.__BASEURL + path,
                             json=json,
                             headers=headers)
        if resp.status_code == 200:
            return resp.content
        return resp

    def _put(self, path, json=None, headers=None):
        resp = requests.put(self.__BASEURL + path,
                            json=json,
                            headers=headers)
        if resp.status_code == 200:
            return resp.content
        return resp

    def get_users(self, params=None):
        headers = self.get_header()
        return self._get("/users", headers=headers, params=params)

    def get_user_by_id(self, user_id):
        headers = self.get_header()
        return self._get("/users/{}".format(user_id), headers=headers)

    def delete_user_by_id(self, user_id):
        headers = self.get_header()
        return self._delete("/users/{}".format(user_id), headers=headers)

    def create_user(self, user):
        headers = self.get_header()
        return self._post("/users", json=user, headers=headers)

    def update_user(self, user):
        headers = self.get_header()
        return self._put("/users/{}".format(user['id']),
                         json=user,
                         headers=headers)
