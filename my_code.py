# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  

continent_and_country = {}

while True:
    continent = input("Enter a continent name: ")
    country =  input("Enter a country name: ")
    continent_and_country[continent] = country
    print("Do you want to put annother entry?")
    x = input("Enter yes or no: ")
    if x == 'yes':
        continue 
    else:
        break
for key, value in continent_and_country.items():
    print(key, value)
