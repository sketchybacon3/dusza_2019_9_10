from data_structures import speed_measurement
from functions import file_handling
import speed_checkpoint_data
from functions import functions

def task1(checkpoint_data):
    # チェックポイントAで制限速度を超えるのバイクは何台ですか
    bikes_over_limit = checkpoint_data.get_vehicles_over_limit("m", "A")
    print("制限速度を超えるのバイクの数： {0}".format(len(bikes_over_limit)))

def task2(checkpoint_data):
    # チェックポイントBで制限速度を超える車とバスと貨物車を表示する
    cars_over_limit = checkpoint_data.get_vehicles_over_limit("sz", "B")
    buses_over_limit = checkpoint_data.get_vehicles_over_limit("b", "B")
    trucks_over_limit = checkpoint_data.get_vehicles_over_limit("t", "B")

    results = cars_over_limit + buses_over_limit + trucks_over_limit

    functions.print_result(results, True, True, False, True, True, False)

def main():
    data_source = input("データソースを入力してください")
    data_arr = file_handling.deserialize_file(data_source)
    objects = speed_measurement.convert_to_objects(data_arr[1:len(data_arr)])
    checkpoint_data = speed_checkpoint_data.SpeedCheckpointData(objects)
    #初期化終了

    task1(checkpoint_data)
    task2(checkpoint_data)


if __name__ == '__main__':
    main()
