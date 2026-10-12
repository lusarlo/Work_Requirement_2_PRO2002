# PRO2002: Work Requirement 2

- Analyze what makes the code problematic and suggest concrete improvements. 
- Refactor the code where appropriate and explain your refactoring choices.
- Explain the problems in each case, the improvements you have made and why.

## The Undocumented Converter
The original code was difficult to understand because the class name Converter did not explain what was being converted. The values 5/9 and -32 * 5/9 were magic numbers, and the method and variable names were too generic.
I renamed the class to TemperatureConverter and the method to fahrenheit_to_celsius to make their purpose clearer. I also replaced the magic numbers with constants with names (FAHRENHEIT_OFFSET and CONVERSION_FACTOR), and I added comments explaining the formula.
## The Tightly couple Order class

## The Duplicated Discount Logic

## The process_order Method

## Reflection 
A short reflection (~100words) on which of these challenges you personally find most problematic and why



