Feature: User Login

    Scenario: Successful Login
        Given I navigate to the login page
        When I enter valid details
        And I submit the form
        Then I should see a success message

    Scenario: Registration with Invalid Email
        Given I navigate to the login page
        When I enter the invalid details
        And I submit the form
        Then I should see an error message
