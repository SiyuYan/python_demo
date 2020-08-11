import json
import unittest
from scripts.api.api_caller import APICaller
from scripts.api.utils import generate_user


class TestAPI(unittest.TestCase):

    def setUp(self):
        print("start test")
        self.apiCaller = APICaller()
        self.payload = {"first_name": "Brian",
                        "last_name": "Ratke",
                        "gender": "male",
                        "email": "",
                        "status": "active"}
        # use one static test account
        self.user_id = 28934
        self.user = generate_user(self.payload)

    def testGetUsers(self):
        response = self.apiCaller.get_users()
        assert response["_meta"]["code"] == 200

    def testCreateUser(self):
        response = json.loads(self.apiCaller.create_user(self.user))

        self.user_id = response["result"]["id"]
        print(self.user_id)

        assert response["_meta"]["code"] == 200
        assert response["result"]["first_name"] == "Brian"
        assert response["result"]["last_name"] == "Ratke"
        assert response["result"]["gender"] == "male"

    def testUpdateUsers(self):
        self.user['id'] = self.user_id
        self.user['first_name'] = 'new_name'
        response = json.loads(self.apiCaller.update_user(self.user))
        assert response["_meta"]["code"] == 200
        assert response["_meta"]["code"] != "Brian"
        assert response["result"]["first_name"] == "new_name"

        # change back
        self.user['first_name'] = 'Brian'
        response = json.loads(self.apiCaller.update_user(self.user))
        assert response["_meta"]["code"] == 200
        assert response["result"]["first_name"] != "new_name"
        assert response["result"]["first_name"] == "Brian"

    def testDeleteUsers(self):
        response = self.apiCaller.delete_user_by_id(self.user_id)
        print(response)
        assert response["_meta"]["code"] == 204
        assert response["_meta"]["success"] is True


if __name__ == '__main__':
    unittest.main()
