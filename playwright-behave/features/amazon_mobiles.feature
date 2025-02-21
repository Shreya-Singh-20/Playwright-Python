Feature: Amazon Mobile Store Flow

  @AddProductsDynamic
  Scenario Outline: Add products from subtabs
    Given I click on the "<BigTab>" tab
    When I hover on "<subTab>"
    Then I click on "<middleTab>" First product should be selected and added to cart
    Examples:
      | BigTab  | subTab                  |   middleTab   |
      | Mobiles | Laptops & Accessories |   Apple       |
      | Electronics | Audio            |   Mivi       |

#  @Lenovo
#  Scenario: Lenovo Tab Opens
#    Given I click on the mobile tab
#    When I hover on Laptops and Accessories
#    Then Lenovo should be selected
#    And A specified product of Lenovo is added to cart