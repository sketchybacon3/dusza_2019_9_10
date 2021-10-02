def deserialize_file(source_name):
    try:
        file = open(source_name, 'r')
        arr = file.readlines()
        arr2 = []
        for i in range(len(arr)):
            arr2.append(arr[i].replace("\n", "").split(","))
        return arr2
    except FileNotFoundError:
        print("データソースが見つけませんでした。")
        exit()

