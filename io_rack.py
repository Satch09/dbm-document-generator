class IO_Rack:

    def __init__(self, rack_size, cards):
        self.rack = [None] * rack_size
        if len(cards) > len(self.rack):
            print('Too many cards for the rack')
        else:
            counter = 0
            for card in cards:
                self.rack[counter] = card
                counter = counter + 1
        # print(self.rack)
