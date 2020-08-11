CREATE TABLE api_test_cases (
    id INT AUTO_INCREMENT PRIMARY KEY,
    api_endpoint VARCHAR(255),
    input_data VARCHAR(255),
    expect_result VARCHAR(255),
    validate_result INT,
    case_desc VARCHAR(255)
);


