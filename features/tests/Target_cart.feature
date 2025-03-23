# Created by rekha at 3/22/25
Feature: # Click on Target Cart
  # Checking “Your cart is empty” message when clicking on cart icon

  Scenario: # Verifying “Your cart is empty” message
    Given Open target main page
    When Click on cart icon
    Then Verify  'Your cart is empty' message is shown