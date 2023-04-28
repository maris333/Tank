class Tank:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

    def pour_water(self, volume):
        self.volume += volume
        return self.volume

    def pour_out_water(self, volume):
        self.volume -= volume
        return self.volume

    def transfer_water(self, from_where, volume):
        if from_where.volume >= volume:
            self.volume += volume
            from_where.volume -= volume
        else:
            print("There is not enough water in the from_where tank!")
        return self.volume

