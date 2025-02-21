Feature: User Login

  @OrangeHRM
  Scenario: Successful Login
    Given I navigate to the login page
    When I enter valid credentials
    And I submit the form
    Then I should see a success message

  @OrangeHRM
  Scenario: Add New Employee
    Given I navigate to the login page
    And I enter valid credentials
    When I click on PIM and then Add option
    And I enter valid details of the new employee
    Then a new employee should be added

  @OrangeHRM
  Scenario: Registration with Invalid Email
    Given I navigate to the login page
    When I enter invalid details
    And I submit the form
    Then I should see an error message
