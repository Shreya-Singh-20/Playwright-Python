Feature: Amazon Login

  @Amazon-login
  Scenario: Login Amazon successfully
    Given User visits amazon.in
    Then User goes to login page
    When User enters mobile number and click continue
    And User enters password and click continue
    Then User should be on homepage