Feature: Testing the E2E Functionality

  @e2e_final
  Scenario Outline: Test E2E Scenario
    Given I am on Sauce Demo Login Page
    When I enter username: <username>, password: <password>
    Then I should be able to see the Inventory Page
    When I add item to cart: <item_name>
    And I view my cart
    And I proceed to checkout
    And I enter my details and continue, first name: <f_name>, last name: <l_name>, zip_code: <zip_code>
    And I click on finish button
    Then I should be able to see the Pony Express Icon


  Examples:
    |username     |password        |item_name          |f_name|l_name|zip_code|
    |standard_user|valid_password  |Sauce Labs Backpack|Tony  |Stark |6127    |