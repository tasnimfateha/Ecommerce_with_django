Feature: searching products
    Scenario: searching for a product
        Given we want to search for a product
        When we enter "python" in the search field
        And we submit the search form
        Then we see a list of products containing "python"
