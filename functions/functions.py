def get_vehicle_name(vehicle_type):
    vehicle_names = dict([('sz', '乗用車'), ('m', 'バイク'), ('b', 'バス'), ('t', '貨物車'), ('mk', '差別化された車')])
    return vehicle_names[vehicle_type]

def get_max_speed_for_vehicle_type(vehicle_type):
    vehicle_speeds = dict([('sz', 130), ('m', 130), ('b', 100), ('t', 80)])
    return vehicle_speeds[vehicle_type]

def print_result(speed_measurement, display_country_code, display_license_plate, display_location, display_vehicle_type, display_speed, display_time):
    str_result = ""

    for i in range(len(speed_measurement)):
        str_result += "===================================\n"
        if display_country_code:
            str_result += "車の国系：" + speed_measurement[i].get_country_code() + ", "

        if display_license_plate:
            str_result += "ナンバープレート：" + speed_measurement[i].get_license_plate() + ", "

        if display_location:
            str_result += "スピードカメラの識別子：" + speed_measurement[i].get_location() + ", "

        if display_vehicle_type:
            str_result += "車のタイプ：" + get_vehicle_name(speed_measurement[i].get_vehicle_type()) + ", "

        if display_speed:
            str_result += "速度：" + speed_measurement[i].get_measured_speed() + ", "

        if display_time:
            str_result += "時刻：" + speed_measurement[i].get_time() + ", "

        str_result = str_result[0:-2]  # 最後の２つ文字を削除する
        str_result += "\n===================================\n"


    print(str_result)