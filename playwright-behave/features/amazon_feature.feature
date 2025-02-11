
Feature: Amazon Feature Functionality

    @amazon
    Scenario: Product desired by user exists
        Given I click on the search box
        When I enter the product details
        Then The product details are provided 

    @amazon
    Scenario: Product desired by user does not exists
        Given I click on the search box
        When I enter the details of a product
        Then It should give me an error message

    @add_to_cart
    Scenario: A product is added to cart
        Given I click on the search box
        When I enter the product details and select it
        Then The product is added to cart

#    @add_to_cart
#    Scenario: To checkout products
#        Given The product is added to cart
#        When I click on proceed to buy items
#        Then I should see the sign up page
