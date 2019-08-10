import openpyxl as xl
import re
from openpyxl.chart import BarChart, Reference


class dbm_instrument:
    def __init__(self, tag_name, tag_description, tag_io_type, tag_location):
        self.tag_name = tag_name
        self.tag_description = tag_description
        self.tag_io_type = tag_io_type
        self.tag_location = tag_location
        self.all = {
            'tag_name': self.tag_name,
            'tag_description': self.tag_description,
            'tag_io_type': self.tag_io_type,
            'tag_location': self.tag_location,
        }


def create_io(input_filename):
    allIO = []
    wb = xl.load_workbook(input_filename, data_only=True)
    sheet = wb['Instrument List']
    for row in range(19, sheet.max_row + 1):
        # Try to get the column range in the row to check which io type it is and record tag_io_type as such
        """ row_range = str("P{}:V{}".format(row, row))
        print(sheet.cell(row_range)) """

        if str(sheet.cell(row, 5).value).startswith("C1"):
            tag_name = sheet.cell(row, 5).value
            tag_description = str.strip(sheet.cell(row, 6).value)
            tag_location = str.strip(sheet.cell(row, 7).value)
            # remove any whitespace
            cleaned_tag_name = re.sub('[\s+]', '', tag_name)
            # print(cleaned_cell)
            ob = dbm_instrument(
                cleaned_tag_name, tag_description, 'DI', tag_location)
            ob_obj = {
                "tag_name": cleaned_tag_name,
                "tag_description": tag_description,
                "tag_io_type": 'DI',
                "tag_location": 'here'
            }
            # print(ob.tag_description)
            allIO.append(ob)
    print(allIO[1].all)
    sort_all_io = sorted(
        allIO, key=lambda x: x.tag_name, reverse=False)
    for i in sort_all_io:
        print(i.tag_description)
    print(allIO[1].all)


create_io('inst_list.xlsx')
