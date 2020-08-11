from random import Random


def fake_login_api_return_token():
    # login
    return "_iUerG81PgGvyLkh5goy8yWbh_A6rQOEzfZB"


def generate_email():
    random = Random()
    num = random.randint(1, 1000)
    return "lew{}@roberts.com".format(num)


def generate_user(data):
    email = generate_email()
    print(email)
    data["email"] = email
    return data
