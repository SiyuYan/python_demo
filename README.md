## API Test
`api folder`:
 - api_test.py is the CRUD api test
 - api_caller.py is the real CRUD api method
 - utils.py is the function method needed.(The fake_login_api_return_token is demo to show if we have one login api and get the login token credential)


- Reference used API:
Used the Online REST API for Testing and Prototyping(https://gorest.co.in/)

```
GET /public-api/users: list all users.
GET /public-api/users/123: return the details of the user 123.
POST /public-api/users: create a new user.
PUT /public-api/users/123: update the user 123.
DELETE /public-api/users/123: delete the user 123.
```

#### Run instruction
`python3 api_test.py`

### Database connection method

`db` db database operation class
- `mysql_client.py` used for mysql database operation, it contains create/get/update/delete interfaces
- `api_test_initialize.py` init mysql table (api_test_cases) which each record is an API test case
- `api_test_validator.py` connect to mysql and query all the test cases which didn't run. Call the endpoint
and  validate the result with expected result which saved in database

`mock_server` used to start a mock server to simulate the port forwarding scenario.

### Port forwarding connection method
`port_forward` use sshtunnel to write a demo about port forwarding. 

- we have an API server which running behind the firewall.
- The firewall only open SSH 22 port. 
- We will use port forwarding which implemented by sshtunnel to let outside connect to API server

The sample code located at api_ssh_client.py
