from data_structures import speed_measurement
from functions import file_handling
import speed_checkpoint_data
from functions import functions

def task1(checkpoint_data):
    # チェックポイントAで制限速度を超えるのバイクは何台ですか
    bikes_over_limit = checkpoint_data.get_vehicles_per_type("A", "m")
    print("制限速度を超えるのバイクの数： {0}".format(len(bikes_over_limit)))

def task2(checkpoint_data):
    # チェックポイントBで制限速度を超える車とバスと貨物車を表示する
    cars_over_limit = checkpoint_data.get_vehicles_per_type("B", "sz")
    buses_over_limit = checkpoint_data.get_vehicles_per_type("B", "b")
    trucks_over_limit = checkpoint_data.get_vehicles_per_type("B", "t")

    results = cars_over_limit + buses_over_limit + trucks_over_limit

    functions.print_result(results, True, True, False, True, True, False, False, False)

def task3(checkpoint_data):
    print(checkpoint_data.get_max_speed_at_location("A"))
    results = checkpoint_data.get_vehicles_over_limit("A")
    functions.print_result(results, True, True, False, True, False, True, True, False)

def task4(checkpoint_data):
    results = checkpoint_data.get_vehicles_by_country_code("H")
    print(len(results))

def task5(checkpoint_data):
    results = checkpoint_data.limited_speed_between_time("C", "09:00:00", "13:00:00", 110, "sz")
    functions.print_result(results, True, True, False, False, True, False, False, False)

def task6(checkpoint_data, cam_locs):
    pass

def task7(checkpoint_data):
    results = checkpoint_data.get_cars_between_all_points()
    functions.print_result(results, True, True, False, False, False, False, False, False)


def task8(checkpoint_data):
    license_plate = input("ナンバープレートを入力してください")
    checkpoint_data.get_vehicles_abusing_license_plate(license_plate)

def task9(checkpoint_data):
    results = checkpoint_data.get_invalid_license_plates()
    functions.print_result(results, False, True, False, False, False, False, False, False)

def main():
    data_source = input("データソースを入力してください")
    data_arr = file_handling.deserialize_file(data_source)
    objects = speed_measurement.convert_to_objects(data_arr[1:len(data_arr)])
    checkpoint_data = speed_checkpoint_data.SpeedCheckpointData(objects)
    #初期化終了

    task1(checkpoint_data)
    task2(checkpoint_data)
    task3(checkpoint_data)
    task4(checkpoint_data)
    task5(checkpoint_data)
    task7(checkpoint_data)
    task8(checkpoint_data)
    task9(checkpoint_data)

if __name__ == '__main__':
    main()
