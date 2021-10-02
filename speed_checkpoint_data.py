from functions import functions

class SpeedCheckpointData:
    def __init__(self, obj):
        self.data = obj

    def get_vehicles_at_location(self, vehicle_type, location):
        arr = []
        for i in range(len(self.data)):
            if self.data[i].get_location() == location and self.data[i].get_vehicle_type() == vehicle_type:
                arr.append(self.data[i])
        return arr

    def get_vehicles_over_limit(self, vehicle_type, location):
        arr = []
        vehicles = self.get_vehicles_at_location(vehicle_type, location)
        for i in range(len(vehicles)):
            if int(vehicles[i].get_measured_speed()) > functions.get_max_speed_for_vehicle_type(vehicle_type):
                arr.append(vehicles[i])
        return arr
