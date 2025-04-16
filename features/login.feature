Feature: Login Functionalities

  @valid_login
  Scenario Outline: Valid Login
    Given I am on Sauce Demo Login Page
    When I enter username: <username>, password: <password>
    Then I should be able to see the Inventory Page


  Examples:
    |username     |password        |
    |standard_user|valid_password  |