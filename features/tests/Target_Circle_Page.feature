# Created by rekha at 3/23/25
Feature: Target circle page
  Checking at least 10 benefit cells in Target circle

  Scenario: Check the Target circle page
    Given Open Target page
    When Navigate to Target circle
    Then Verify at least 10 {link_amount} benefits links shown inside Target circle


