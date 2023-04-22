import gspread
from oauth2client.service_account import ServiceAccountCredentials

scopes={
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
}

creds=ServiceAccountCredentials.from_json_keyfile_name("C:\\rasa2.o\\botrushchatbot-59e97e76d71a.json",scopes=scopes)

file=gspread.authorize(creds)
workbook=file.open("Final Evaluation Schedule(Match and engage)")
sheet=workbook.sheet1
# print(sheet.range('B5:B12'))
data = sheet.get_all_values()

print(data)

# teams = {'bot squad': '7:30 - 7:35pm', 'delivery_droids': '7:35 - 7:40pm', 'itm^2': '7:40 - 7:45pm', 'nerdobots': '7:45 - 7:50pm', 'pirates': '7:50 - 7:55pm', 'technotrons': '7:55 - 8:00pm', 'the warriors': '8:00 - 8:05pm', 'wizdroid': '8:05 - 8:10pm'}

# start_time_str = input("Enter start time (e.g. 7pm or 7:30pm): ")

# # If the user input doesn't have minutes, add ':00'
# if len(start_time_str) == 2:
#     start_time_str += ':00'

# for team, time_range in teams.items():
#     start_time, end_time = time_range.split(' - ')
#     start_time = start_time.replace('pm', '').replace('am', '') + 'pm'
#     end_time = end_time.replace('pm', '').replace('am', '') + 'pm'

#     if start_time_str == start_time:
#         print(f"{team} match starts at {start_time}.")
#         break
#     elif start_time_str == end_time:
#         print(f"{team} match ends at {end_time}.")
#         break
# else:
#     print(f"No team alloted at {start_time_str}.")




