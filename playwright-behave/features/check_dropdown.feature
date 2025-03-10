Feature: Check dropdown of country region

  @change-region
  Scenario: Change the country region
   Given User hovers on the language dropdown
   When User clicks on change country region
   And Selects a country in which he wants to change the country
   Then The country flag is shown on the home page