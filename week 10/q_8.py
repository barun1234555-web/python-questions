class Temperature:
    def celsius_to_fahrenheit(self, c):
        return (c * 9/5) + 32

    def fahrenheit_to_celsius(self, f):
        return (f - 32) * 5/9

temp = Temperature()
print(f"30°C to F: {temp.celsius_to_fahrenheit(30)}")
print(f"86°F to C: {temp.fahrenheit_to_celsius(86)}")