Feature: Test navigation between pages
  more comments
  if needed

  Scenario: home page can go to Blog
    Given I am on the home page
    When I click on the "Go to blog" link
    Then I am on the blog page

  Scenario: blog page can go to homepage
    Given I am on the blog page
    When I click on the "Go to home" link
    Then I am on the home page