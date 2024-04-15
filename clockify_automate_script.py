from clockify_client import ClockifyClient
from dotenv import load_dotenv
import datetime
import os
import json

# Function that read file
def readFile(filepath):
    with open(filepath, 'r') as file:
        file_content = file.read()
    return file_content

# Function that grabs the project object based on project name
def find_project_by_name(projects, name):
    for project in projects:
        if project["name"] == name:
            return project
    return None  # Return None if no project with the given name is found

# Format the time_start/end which only contains hh:mm:sss, to 
# current date, to yyyy-MM-ddThh:mm:ssZ
def format_datetime(time_str):

    today = datetime.datetime.now().date()

    # Parse the time
    time = datetime.datetime.strptime(time_str, '%H:%M:%S').time()
    # Combine date and time
    datetime_obj = datetime.datetime.combine(today, time)
    # Format as ISO 8601 with 'Z' (indicative of UTC)
    return datetime_obj.strftime('%Y-%m-%dT%H:%M:%SZ')


def find_entries_by_weekday(entries, weekday):
    return [entry for entry in entries if weekday in entry['WEEKDAY']]

load_dotenv()

PROJECT_FILTER = "Labourly"
TIME_ENTRIES_FILE = "time_entries_data.json"
api_key = os.getenv('CLOCKIFY_APY')

client = ClockifyClient(api_key)
respUserData = client.get_user_data();
activeWorkspace = respUserData['activeWorkspace']

# Parse the time entries json
time_entries_json= json.loads(readFile(TIME_ENTRIES_FILE))

# Get the current Weekday in uppercase
today = datetime.datetime.now()
current_weekday_name = today.strftime('%A').upper() 

entries_today = find_entries_by_weekday(time_entries_json['time_entries'], current_weekday_name)
entry_to_insert = []

for entry in entries_today:
    projectData =  find_project_by_name(client.get_project_data(activeWorkspace, entry['project_name']), 
                                        entry['project_name'])
    dataJson = {
        "billable": entry['billable'],
        "description": entry["descriptions"],
        "projectId": projectData["id"],
        "start": format_datetime(entry['time_start']),
        "end": format_datetime(entry['time_end']),
        "type": entry['type']
    }

    entry_to_insert.append(dataJson)

for entry in entry_to_insert:
    resp = client.add_time_entry(activeWorkspace, data=entry)
    print(resp.status_code)