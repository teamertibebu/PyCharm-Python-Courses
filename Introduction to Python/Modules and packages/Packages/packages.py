import functions.goodbye as bye
import functions.greeting.hello
from classes import calculator
import functions.greeting.official as official
import functions.greeting.hello as hello
import functions.goodbye as goodbye


print(hello.hello('Susan'))
print(goodbye.good_bye("Alex") )

c = calculator.Calculator()
c.add(2)
c.multiply(10)
print(c.get_current())

print(official.hello('Sam'))
