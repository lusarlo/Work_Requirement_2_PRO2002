class TemperatureConverter:
    # Constants used in the fahrenheit to celsius formula
    FAHRENHEIT_OFFSET = 32
    CONVERSION_FACTOR = 5 / 9

    def fahrenheit_to_celsius(self, fahrenheit_value):
        # Subtract the offset and apply the conversion factor
        return (fahrenheit_value - self.FAHRENHEIT_OFFSET) * self.CONVERSION_FACTOR

# Convert 212 degrees Fahrenheit to Celsius
result = TemperatureConverter().fahrenheit_to_celsius(212)

print(result) # Output: temperature in Celsius