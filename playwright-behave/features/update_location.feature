Feature: Update the location of a user

  @location-update
  Scenario: User updates the location
    Given User is on the home page
    When User enters the new location
    Then The location must be updated