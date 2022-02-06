#exampleOfStringSlicing

a = "Pithon"
stringSlicing = a[:1] + "y" + a[2:]
print(stringSlicing)


#practicingForFormat

a = f'{"python":!^12}'
print(a)

a = "{0:!^12}".format('python')
print(a)

a = "Life is {0} short. You need {1}".format('too', 'Python')
print(a)

a = "{0:=>10}".format('hi')
print(a)

a = "{0:!^10}".format("hi")
print(a)