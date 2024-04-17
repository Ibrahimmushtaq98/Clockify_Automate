# Clockify Automate Script

  

For background, I got extremely lazy filling out my Clockify form, so I just created this instead :)

## How to use

I provided two example file, `example.env` and `time_entries_data.example.json` which needs to be filled out and renamed.

For `example.env` all you need to do is put your API key in and just rename the file to `.env`

    CLOCKIFY_API=YOURAPIKEYHERE
For `time_entries_data.example.json`, I have given an example content like so:
```json
{

	"time_entries": [{
		// The Weekdays 
		"WEEKDAY": [

		],
	"descriptions": "",
	"project_name": "",
	"billable": false,
	"time_start": "", // Time in GMT
	"time_end": "", // Time in GMT
	"type": ""
	}

]}
```
**Weekdays** are when you want this script to run on list of weekdays (Ex Monday, Tuesday Wednesday), as such the `WEEKDAY`array object should contain a list of string of weekday name. An example can be `"WEEKDAY": ["Monday", "Wednesday"]`

**Descriptions** are just a string that contains a descriptive field for your time entry

**Project_Name** is the name of the project on which you want the time entry to be under. Make sure sure to specify the exact project name as the script will try and find the Project Id associated to that name

**Time_Start** or **Time_End** is the timing for that particular time entry in `HH:mm:ss` in GMT/UTC time. This is important cause I accidentally set my script in EST time and found out really late. So make sure to convert the time from whatever time zone you are in, into GMT/UTC

**Billable** is just a boolean field telling if that project is a billable project or not.

**Type** is just a valid enum time entry type by Clockify. Enums:  `"REGULAR"  "BREAK"  "HOLIDAY"  "TIME_OFF"  "REGULAR"  "BREAK"`

After you have made these changes to that file, make sure to change the name of the json to `time_entries_data.json`

### Alright finally, how the heck do you use this thing?

This project uses docker, but it still have the crontab file for you to use. In terms of Isolated system, this uses docker system

Here is an example way to run this using docker

```bash
docker build -t python-clockify-cron:v1.0 .
docker run --name python-cron-clockify -it -d python-clockify-cron:v1.0
```

The cron job will run at 6PM EST in UTC, if you need to adjust the timing, just edit the crontab file to the specific timing that you would need.
