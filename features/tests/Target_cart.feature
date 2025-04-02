# Created by rekha at 3/22/25
Feature: # Click on Target Cart
  # Checking “Your cart is empty” message when clicking on cart icon

  Scenario: # Verifying “Your cart is empty” message
#    Given Open target main page
#    When Click on cart icon


  Scenario: User can add a product to cart
    Given Open target main page
    Then Click on Add to Cart button
    And Store product name
    When Open cart page
    #When Search for mug
    Then Verify cart has correct product
    And Confirm Add to Cart button from side navigation
    Then Verify cart has 1 item(s)
    Then Verify {link_amount} links shown
    Then Verify  'Your cart is empty' message is shown
    Then Verify correct search results shown for {expected_result}