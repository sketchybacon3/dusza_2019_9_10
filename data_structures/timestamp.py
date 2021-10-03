class TimeStamp:
    def __init__(self, str_input):
        self.arr = str_input.split(":")
        self.hour = int(self.arr[0])
        self.minute = int(self.arr[1])
        self.seconds = int(self.arr[2])

    def get_full_timestamp(self):
        return self.arr

    def get_hour(self):
        return self.hour

    def get_minute(self):
        return self.minute

    def get_seconds(self):
        return self.seconds
