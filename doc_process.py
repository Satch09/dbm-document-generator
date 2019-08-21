import openpyxl as xl
from instrument import Instrument
from io_card import IO_Card
from io_rack import IO_Rack

wb = xl.load_workbook('MRC_Inst_List.xlsx', data_only=True)
sheet = wb['data']


def get_instruments(data):
    item = {}
    instruments = []
    for row in range(2, data.max_row):
        for col in range(1, data.max_column):
            key = data.cell(1, col).value
            value = data.cell(row, col).value
            result = {key: value}
            item.update(result)
        instruments.append(Instrument(item))
    return instruments


my_insts = get_instruments(sheet)

test = [IO_Card('1756-IB32', 'DIV'), IO_Card('1756-IB32', 'DIV'),
        IO_Card('1756-IB32', 'DIV'), IO_Card('1756-IB32', 'DIV'), ]

firstRange = my_insts[:32]
secondRange = my_insts[33:65]
thirdRange = my_insts[66:98]

c1 = IO_Card('1756-IB32', 'DIV')
c1.populate_card(
    (firstRange))
c2 = IO_Card('1756-IB32', 'DIV')
c2.populate_card((secondRange))
c3 = IO_Card('1756-IB32', 'DIV')
c3.populate_card((thirdRange))
c4 = IO_Card('1756-IB32', 'DIV')
c4.populate_card(('input 41', 'input 42', 'input 43'))
rack = IO_Rack(4, [c1, c2, c3, c4])
# rack = IO_Rack(4, test)
for r in rack.rack:
    print('-' * 100)
    for s in r.io_assignments:
        print("{}: {}".format(s, s.tag_description))
