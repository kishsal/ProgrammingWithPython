import numpy

# Speeds
# 1. School Zones: 25
# 2. Residential: 35
# 3. Major roads: 45 or 50
# 4. Highways: 65
# 5. Smaller highways: 55

lst = [25, 35, 45, 65, 55]

speed = numpy.mean(lst)

print(speed)