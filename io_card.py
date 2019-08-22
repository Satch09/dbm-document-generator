class IO_Card:
    """
    Creates IO card bassed on the part number specified

    IO Types:
        DIV: Digital Input, Voltage
        DOV: Digital Output, Voltage
        AIC: Analog Input, Current
        AIV: Analog Input, Voltage
        AOC: Analog Output, Current
        AOV: Analog Output, Voltage
        SSI: Synchronous Serial Interleave
        RTD: Resistive Temperature Differential
    """

    def __init__(self, card_part_number, card_io_type, instruments):
        cards = [
            {'card_name': '1756-IB32', 'io_count': 32, 'io_type': 'DIV'},
            {'card_name': '1756-OB32', 'io_count': 32, 'io_type': 'DOV'},
            {'card_name': '1756-IF16', 'io_count': 16, 'io_type': 'AIC'},
            {'card_name': '1756-OF16', 'io_count': 16,
                'io_type': ('AOC', 'AOV')},
            {'card_name': '1756-IRT12', 'io_count': 12, 'io_type': 'RTD'},
        ]

        for card in cards:
            if card['card_name'] == card_part_number:
                self.part_number = card['card_name']
                self.io_count = card['io_count']
                self.io_assignments = [None] * card['io_count']
                if len(card['io_type']) > 1 and card_io_type in card['io_type']:
                    for io in card['io_type']:
                        if io == card_io_type:
                            self.io_type = io
                    populate_card(instruments)
                else:
                    print('error in assigning io to card')

    def populate_card(self, instruments):
        counter = 0
        for instrument in instruments:
            if counter < len(self.io_assignments):
                self.io_assignments[counter] = instrument
                counter = counter + 1
        return self.io_assignments

    def __str__(self):
        return self.card_io_type

    if __name__ == "__main__":
        pass
