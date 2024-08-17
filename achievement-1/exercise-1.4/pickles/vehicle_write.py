import pickle

# vehicle = {
#     'brand': 'BMW',
#     'model': '530i',
#     'year' : 2015,
#     'color': 'Black Sapphire'
# }

# vehicle_file = open('vehicledetail.bin', 'wb')
# pickle.dump(vehicle, vehicle_file)
# vehicle_file.close()


with open('vehicledetail.bin', 'rb') as vehicle_file:
    loaded_vehicle = pickle.load(vehicle_file)

print("Vehicle details - ")
print("Name:  " + loaded_vehicle['brand'] + " " + loaded_vehicle['model'])
print("Year:  " + str(loaded_vehicle['year']))
print("Color: " + loaded_vehicle['color'])