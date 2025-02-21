Feature: Adding Multiple Products to Cart

  @Multiple
  Scenario: Add multiple products to the cart and checkout
    Given I click on the search box of amazon
    When I enter the following product names and add them to the cart
      | productsToAdd|
      | Shirt   |
      | Earphones |
      | Speakers  |
    Then I verify that all products are in the cart
    And I proceed to checkout
