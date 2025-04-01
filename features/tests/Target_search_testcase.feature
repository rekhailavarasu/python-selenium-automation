# Created by rekha at 3/22/25
Feature: Target 'Search' test cases
  # Searching various products in Target website

  Scenario: User search for 'coffee'
    Given Open target page
    When Search for coffee
    Then Verify the results shown is for coffee

  Scenario: User can search for 'tea'
   # Given Open target page
    When Search for tea
    Then Verify the results shown is for tea

  Scenario Outline: User can search for more products
   # Given Open target page
    When Search for <search_word>
    Then Verify correct search results shown for <expected_result>
    Examples:
      | search_word | expected_result |
      | pen         | pen             |
      | bread       | bread           |
      | ring        | ring            |
    Then Verify correct search results shown for {expected_result}

  Scenario: Add item in cart
    Given Open Target page
    When Search for sofa
    And Select an item to Add to cart
    And Continue to click on Add to cart
