from flask import Flask, url_for, render_template
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

app.secret_key = "BBTSSSECRET"

# Webpages
@app.route('/')
def index():
    projects = get_projects()
    return render_template('index.html', projects=projects)

# Retrieve projects from Google Sheets
def get_projects():
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('Portfolio Projects').sheet1
    data = sheet.get_all_records()
    return data

if __name__ == "__main__":
    app.run(debug=True)