from scripts.testcase_db import MYSQLClient
from scripts.api.api_caller import APICaller


class APIValidator:

    def __init__(self):
        self.mysql_client = MYSQLClient()
        self.api_caller = APICaller()

    def validate_untested_api_cases(self):
        table_name = "api_test_cases"
        cases = self.query_untested_cases(table_name)
        print("query {} cases!".format(len(cases)))
        for case in cases:
            flag, validate_result = self.validate_untest_api_case(case)
            print("case {} validate result is {}".format(case[0], flag))
            self.update_result(table_name, case[0], flag, validate_result)

    def query_untested_cases(self, table_name):
        sql = "SELECT * FROM {} WHERE validate_result IS NULL".format(table_name)
        return self.mysql_client.query_all(sql)

    def validate_untest_api_case(self, case):
        endpoint = case[1]
        data = case[2]
        res = self.api_caller.get_users(endpoint, data)
        if data == case[3]:
            return 1, res
        return 0, res

    def update_result(self, table_name, id, flag, validate_result):
        sql = "UPDATE {} SET validate_result = %s WHERE id = %s".format(table_name)
        print(sql)
        val = (flag, id)
        self.mysql_client.update_all(sql, val)


if __name__ == '__main__':
    validator = APIValidator()
    validator.validate_untested_api_cases()
