import re
from scripts.testcase_db import MYSQLClient


class APITestInitializer:

    def __init__(self):
        self.mysql_client = MYSQLClient()

    def create_table_with_ddl(self, ddl_file):
        sql = self.get_sql_from_file(ddl_file)
        table_name = self.get_table_name(sql)
        if not self.mysql_client.table_exist(table_name):
            print("Starting to create table {}".format(table_name))
            self.mysql_client.create_table(sql)
        else:
            print("Table {} already exist!".format(table_name))
        return table_name

    def get_table_name(self, sql):
        part = re.search("^(CREATE TABLE)+\s+\w+\s+\(", sql)
        if not part is None:
            return part.group().replace("CREATE TABLE", '').replace("(", '').strip()

    def get_sql_from_file(self, ddl_file):
        with open('../ddl/' + ddl_file, 'r') as file:
            sql = file.read().replace('\n', '')
        return sql

    def initialize_test_cases(self, table_name, test_cases):
        insert_sql = 'INSERT INTO {} (api_endpoint,input_data,expect_result,case_desc) VALUES (%s,%s,%s,%s)'.format(
            table_name)
        self.mysql_client.insert_all(insert_sql, test_cases)

    # TODO：
    def get_mock_values(self):
        return [
            ('/bookings', '1', '[{"bookingid": 1}]', 'test case 1'),
            ('/bookings', '2', '[{"bookingid": 2}]', 'test case 2'),
            ('/bookings', '3', '[{"bookingid": 3}]', 'test case 3'),
            ('/bookings', '4', '[{"bookingid": 4}]', 'test case 4')
        ]


if __name__ == '__main__':
    constructor = APITestInitializer()
    table_name = constructor.create_table_with_ddl('api_test_cases_ddl.sql')
    constructor.initialize_test_cases(table_name, constructor.get_mock_values())
