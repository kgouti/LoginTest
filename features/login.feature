# Created by KARTIK at 15-02-2022
Feature: Login
  # Enter feature description here

  Scenario: Login with valid credentials
  Given login url is opened
    When user enters valid username test@qa-experience.com and password Password1
    And clicks login button
    Then login is successful

    Scenario: Login with invalid credentials
    Given login url is opened
    When user enters invalid username invalid@user.com and password invalid_password
    And clicks login button
#    Then login is unsuccessful

    Scenario: Login with empty username
      Given login url is opened
      When user clicks login button
#      Then login is unsuccessful
