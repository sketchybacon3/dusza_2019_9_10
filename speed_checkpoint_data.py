import datetime
from functions import functions
from data_structures import timestamp

class SpeedCheckpointData:
    def __init__(self, obj):
        self.data = obj

    def get_vehicles_at_location(self, location):
        arr = []
        for i in range(len(self.data)):
            if self.data[i].get_location() == location:
                arr.append(self.data[i])
        return arr

    def get_vehicles_over_limit(self, location):
        arr = []
        vehicles = self.get_vehicles_at_location(location)
        for i in range(len(vehicles)):
            if int(vehicles[i].get_measured_speed()) > functions.get_max_speed_for_vehicle_type(vehicles[i].get_vehicle_type()):
                arr.append(vehicles[i])
        return arr

    def get_vehicles_per_type(self, location, vehicle_type):
        arr = []
        vehicles = self.get_vehicles_over_limit(location)
        for i in range(len(vehicles)):
            if vehicles[i].get_vehicle_type() == vehicle_type:
                arr.append(vehicles[i])
        return arr

    def get_max_speed_at_location(self, location):
        max_speed = 0
        for i in range(len(self.data)):
            if max_speed < int(self.data[i].get_measured_speed()) and self.data[i].get_location() == location:
                max_speed = int(self.data[i].get_measured_speed())
        return max_speed

    def get_vehicles_by_country_code(self, country_code):
        already_checked_vehicles = []
        for i in range(len(self.data)):
            if already_checked_vehicles.count(self.data[i]) == 0 and self.data[i].get_country_code() == country_code:
                already_checked_vehicles.append(self.data[i])

        return already_checked_vehicles

    def get_vehicles_by_plate(self, license_plate):
        arr = []
        for i in range(len(self.data)):
            if self.data[i].get_license_plate() == license_plate:
                arr.append(self.data[i])

        return arr

    def limited_speed_between_time(self, location, time_start, time_end, changed_speed_limit, type_of_vehicle):
        start_time = timestamp.TimeStamp(time_start)
        end_time = timestamp.TimeStamp(time_end)
        arr = []

        for i in range(len(self.data)):
            time_of_measurement = timestamp.TimeStamp(self.data[i].get_time())
            if start_time.get_hour() <= time_of_measurement.get_hour() <= end_time.get_hour():
                if (int(self.data[i].get_measured_speed()) > changed_speed_limit and
                            self.data[i].get_location() == location and
                            int(self.data[i].get_measured_speed()) < functions.get_max_speed_for_vehicle_type(self.data[i].get_vehicle_type()) and
                            self.data[i].get_vehicle_type() == type_of_vehicle):
                    arr.append(self.data[i])
        return arr

    def get_cars_between_all_points(self):
        data_arr = self.data
        arr = []
        for i in range(len(data_arr)):
            for k in range(len(data_arr)):
                for l in range(len(data_arr)):
                    license_a = data_arr[i].get_license_plate()
                    license_b = data_arr[k].get_license_plate()
                    license_c = data_arr[l].get_license_plate()

                    if license_a == license_b and license_b == license_c:
                        if data_arr[i].get_location() == "A" and data_arr[k].get_location() == "B" and data_arr[l].get_location() == "C":
                            has_vehicle_added = False

                            for x in range(len(arr)):
                                if arr[x].get_license_plate() == data_arr[i].get_license_plate():
                                    has_vehicle_added = True
                            if has_vehicle_added == False:
                                arr.append(data_arr[i])

        return arr

    def get_vehicles_abusing_license_plate(self, license_plate):
        arr = []
        vehicles_with_that_plate = self.get_vehicles_by_plate(license_plate.upper())
        if len(vehicles_with_that_plate) == 0:
            print("そんなナンバープレートはありません。")
            exit()
        for i in range(len(vehicles_with_that_plate)):
            if int(vehicles_with_that_plate[i].get_measured_speed()) > functions.get_max_speed_for_vehicle_type(vehicles_with_that_plate[i].get_vehicle_type()):
                arr.append(vehicles_with_that_plate[i])

        if len(arr) == 0:
            print("制限速度をこえていませんでした。")
        else:
            functions.print_result(arr, True, True, True, True, True, False, True, False)