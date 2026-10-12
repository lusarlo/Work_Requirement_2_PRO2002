# PRO2002: Work Requirement 2

- Analyze what makes the code problematic and suggest concrete improvements. 
- Refactor the code where appropriate and explain your refactoring choices.
- Explain the problems in each case, the improvements you have made and why.

## The Undocumented Converter
The original code was difficult to understand because the class name Converter did not explain what was being converted. The values 5/9 and -32 * 5/9 were magic numbers, and the method and variable names were too generic.
I renamed the class to TemperatureConverter and the method to fahrenheit_to_celsius to make their purpose clearer. I also replaced the magic numbers with constants with names (FAHRENHEIT_OFFSET and CONVERSION_FACTOR), and I added comments explaining the formula.

## The Tightly couple Order class
The original Order class depended directly on the internal structure of the User object and the database schema. It also mixed order information with database operations, making the code harder to maintain and test. The hardcoded order ID was also a problem.
I refactored the code so that Order receives the required user information directly and stores the order items. I also introduced an OrderRepository class with a placeholder save method to separate order data from persistence logic. This reduces coupling and makes the code easier to maintain and test.

## The Duplicated Discount Logic
The original code duplicated the discount calculation in both apply_discount_to_cart and generate_invoice. Both functions applied a 10% discount when the total exceeded 5000 cents (50 NOK). This violates the Don't Repeat Yourself (DRY) principle because the same business rule is implemented in multiple places. If the discount threshold or percentage changes, both functions must be updated, which increases the risk of inconsistent behavior.
I refactored the code by extracting the discount calculation into a shared apply_discount function. Both functions now call this function instead of implementing the discount logic themselves. I also introduced named constants, DISCOUNT_THRESHOLD_CENTS and DISCOUNT_RATE, to replace magic numbers. This makes the code easier to understand, maintain, and test. 

## The process_order Method
The original process_order method handled several responsibilities, including calculating the order total, applying discounts, saving the order, and notifying the user. This made the method harder to understand and maintain.
I refactored the code by extracting these responsibilities into separate functions. I also created an OrderRepository with a placeholder save method so that the order-processing logic does not need to contain database details. The discount codes are mapped to their corresponding discount functions in DISCOUNT_RULES, which avoids a long chain of if/elif statements and makes it easier to add new discount rules.

## Reflection 
The most problematic challenge for me was the converter, not because it was difficult to refactor, but because it showed how missing information and poor documentation can make code almost impossible to understand. The other examples were perhaps harder to refactor because I had to think more carefully about what was needed and what could be separated. However, I found it easier to understand their purpose. The converter showed me that clear names and documentation are important even when the code itself is relatively simple. They make code easier to understand, maintain, and update, especially when someone else needs to work on it. Without them, it is difficult to know what the code is meant to do or how to improve it.
