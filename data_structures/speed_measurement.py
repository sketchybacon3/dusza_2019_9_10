class SpeedMeasurement:
    def __init__(self, arr):
        self.country_code = arr[0]
        self.license_plate = arr[1]
        self.location = arr[2]
        self.vehicle_type = arr[3]
        self.measured_speed = arr[4]
        self.time = arr[5]

    def get_country_code(self):
        return self.country_code

    def get_license_plate(self):
        return self.license_plate

    def get_location(self):
        return self.location

    def get_vehicle_type(self):
        return self.vehicle_type

    def get_measured_speed(self):
        return self.measured_speed

    def get_time(self):
        return self.time


def convert_to_objects(arr):
    obj_arr = []
    for i in range(len(arr)):
        obj_arr.append(SpeedMeasurement(arr[i]))
    return obj_arr