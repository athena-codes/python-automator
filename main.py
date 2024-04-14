#  interaction w/ google sheets
import gspread
from google.oauth2.service_account import Credentials

# create new list for scopes
scopes = [
    "https://www.googleapis.com/auth/spreadsheets"
          ]

# create credentials
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)

# client has access to the google sheets
client = gspread.authorize(creds)

# create variable for sheet url id
sheet_id = "1JtowMyctcYQPK5oz5eW3u8OSF_anP9dSlgbqVxlyrLc"
workbook = client.open_by_key(sheet_id)

# access and return row values from linked sheet
values_list = workbook.sheet1.row_values(1)
# print(values_list)  # Prints ['a1', 'b1']

# sheets = map(lambda x: x.title, workbook.worksheets())
# print(list(sheets))
sheet = workbook.worksheet('New Title')
# sheet.update_title('New Title')

# update text of cell
sheet.update_cell(1, 1, 'Hello world')
# update boldness of cell text 1
sheet.format("A1", {"textFormat": {"bold": True}})

# --------------- MINI PROJECT -------------------

values = [
    ["Name", "Price", "Quanity"],
    ["Basketball", 29.99, 1],
    ["Jeans", 39.99, 4],
    ["Soap", 7.99, 3],

]

# create a new worksheet if the one we want doesnt already

worksheet_list = map(lambda x: x.title, workbook.worksheets())
new_worksheet_name = 'Values'

if new_worksheet_name in worksheet_list:
    sheet = workbook.worksheet(new_worksheet_name)
else:
    sheet = workbook.add_worksheet(new_worksheet_name, rows=10, cols=10)

sheet.clear()

# add values into sheet using for loop
for i, row in enumerate(values):
    for j, value in enumerate(row):
        sheet.update_cell(i + 1, j + 1, value)
