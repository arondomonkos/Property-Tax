# Property Tax
# Author: Áron Domonkos
# Year: 2024

# Function 1
data = []
with open('street.txt') as file:
    header = file.readline()
    for line in file:
        line = line.strip().split()
        data.append(line)

print('\nFunction 2')
plot_count = len(data)
print(f'The sample contains {plot_count} plots.')

print('\nFunction 3')
input_id = "68396"  # input_id = input('Owner ID: ')
not_found = True

for line in data:
    owner_id, street, house_number, zone, area = line
    if input_id == owner_id:
        print(f'{street} street {house_number}')
        not_found = False

if not_found:
    print('Not found in the dataset.')

# Function 4
def tax(zone, area):
    rate = 800
    if zone == "B":
        rate = 600
    if zone == "C":
        rate = 100
    payable = rate * int(area)
    if payable < 10000:
        payable = 0
    return payable

print('\nFunction 5')
zone_a = []
zone_b = []
zone_c = []

for line in data:
    owner_id, street, house_number, zone, area = line
    t = tax(zone, area)
    if zone == "A":
        zone_a.append(t)
    if zone == "B":
        zone_b.append(t)
    if zone == "C":
        zone_c.append(t)

print(f"A zone: {len(zone_a)} plots, total tax: {sum(zone_a)} Ft.")
print(f"B zone: {len(zone_b)} plots, total tax: {sum(zone_b)} Ft.")
print(f"C zone: {len(zone_c)} plots, total tax: {sum(zone_c)} Ft.")

print('\nFunction 6')
print('Streets with multiple zones:')
streets = []
zones = []
for line in data:
    if line[1] not in streets:
        streets.append(line[1])
        zones.append(line[3])

mixed_zone = []
for index, street in enumerate(streets):
    for line in data:
        if line[1] == street and line[3] != zones[index] and street not in mixed_zone:
            mixed_zone.append(street)

for s in mixed_zone:
    print(s)

# Function 7
owners = []
for line in data:
    owner_id, street, house_number, zone, area = line
    if owner_id not in owners:
        owners.append(owner_id)

owner_tax = []
for owner in owners:
    owner_tax.append(0)
    for line in data:
        owner_id, street, house_number, zone, area = line
        if owner == owner_id:
            owner_tax[-1] += tax(zone, int(area))

with open("tax.txt", "w") as output_file:
    for i, owner in enumerate(owners):
        output_file.write(f'{owner} {owner_tax[i]}\n')