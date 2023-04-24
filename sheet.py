# Подключаем библиотеки
import httplib2 
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
from KosmeticsBot import google_sheet

CREDENTIALS_FILE = 'courses.json'  # Имя файла с закрытым ключом, вы должны подставить свое

# Читаем ключи из файла
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])

httpAuth = credentials.authorize(httplib2.Http()) # Авторизуемся в системе
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth) # Выбираем работу с таблицами и 4 версию API 

spreadsheetId = '1RM7f67tIk_cfua6vN1pauR7VhEiS62zFsLgWj-i9gYc'

body = {
    'values' : [
        ["Azzrael Code", "YouTube Channel"], # строка
        ["check it",       "RIGHT NOW !!!"], # строка
    ]
}

results = service.spreadsheets().values().append(
    spreadsheetId=spreadsheetId,
    range="Лист1!A1:B2",
    valueInputOption="RAW",
    body=body
).execute()




