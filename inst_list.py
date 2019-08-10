import openpyxl as xl
import re
from openpyxl.chart import BarChart, Reference


class oi_class:
    def __init__(self, tag_name, tag_description, tag_io_type, tag_location):
        self.tag_name = tag_name
        self.tag_description = tag_description
        self.tag_io_type = tag_io_type
        self.tag_location = tag_location


def process_workbook(input_filename):
    allIO = []
    wb = xl.load_workbook(input_filename, data_only=True)
    sheet = wb['Instrument List']
    for row in range(19, sheet.max_row + 1):
        #print(sheet.cell(row, 5).value)
        if str(sheet.cell(row, 5).value).startswith("C1"):
            tag_name = sheet.cell(row, 5).value
            tag_description = str.strip(sheet.cell(row, 6).value)
            # remove any whitespace
            cleaned_tag_name = re.sub('[\s+]', '', tag_name)
            # print(cleaned_cell)
            ob = oi_class(cleaned_tag_name, tag_description, 'DI', 'here')
            ob_obj = {
                "tag_name": cleaned_tag_name,
                "tag_description": tag_description,
                "tag_io_type": 'DI',
                "tag_location": 'here'
            }
            # print(ob.tag_description)
            allIO.append(ob)
    print(allIO[1].tag_name)


process_workbook('inst_list.xlsx')
