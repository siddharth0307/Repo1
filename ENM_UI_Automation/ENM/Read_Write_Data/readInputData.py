import xlrd


class ReadInputData:

    def __init__(self):
        self.input_file_path = "C:\Siddharth\Automation\ENM_Automation\Input\ENM_Data.xlsx"

    def read_ENM_User_Name(self):
        read_file_location = xlrd.open_workbook(self.input_file_path)
        sheet = read_file_location.sheet_by_index(0)
        name = sheet.cell(1, 0)
        return name.value

    def read_ENM_User_Pass(self):
        read_file_location = xlrd.open_workbook(self.input_file_path)
        sheet = read_file_location.sheet_by_index(0)
        password = sheet.cell(1, 1)
        return password.value

    def read_ENM_Node(self):
        read_file_location = xlrd.open_workbook(self.input_file_path)
        sheet = read_file_location.sheet_by_index(0)
        node_name = sheet.cell(1, 2)
        return node_name.value

    def read_alarm_sync_required(self):
        read_file_location = xlrd.open_workbook(self.input_file_path)
        sheet = read_file_location.sheet_by_index(0)
        alarm_sync = sheet.cell(1, 3)
        return alarm_sync.value

    def read_fdn_value_to_compare(self):
        read_file_location = xlrd.open_workbook(self.input_file_path)
        sheet = read_file_location.sheet_by_index(0)
        fdn_name = sheet.cell(1, 4)
        return fdn_name.value
