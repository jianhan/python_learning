coor = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)
for country, _ in traveler_ids:
    print(country)

# unpack
lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates
print(latitude, longitude)


# unpack with function call

def hello(first_name, last_name):
    print(first_name + " " + last_name)


hello(first_name="James", last_name="Smith")
fullname = ("James", "Smith")
hello(*fullname)
