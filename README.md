# PowerHub
Central data persistence hub for internet enabled light and outlets in your home

## API

	http://myhost/message
		(get the current message set)

	http://myhost/message/set
		(HTTP POST a raw string value to this URL to set a new message)
	
	http://myhost/flag/{id}
		(get the current boolean status of the flag by integer: {id})

	http://myhost/flag/all
		(get all the current boolean status of all the flags as an array)

	http://myhost/flag/{id}/set
		(set the current boolean status to 'true' for the flag by integer: {id})

	http://myhost/flag/{id}/unset
		(set the current boolean status to 'false' for the flag by integer: {id})
	
	http://myhost/reading/{id}
		(get the current averaged value for the reading by integer: {id})

	http://myhost/reading/all
		(get the current averaged value for all the readings as an array)

	http://myhost/reading/{id}/set
		(HTTP POST a raw numeric value to this URL to add a new value to the current calculated average)  
			-- see below for how many values in total are compiled to the average value

## Configuation

The 'readings' values are calculated as averages of a certain number of recent persisted reading numeric values. 
Set the following constant to how many of the most recent readings should be included to produce the average.

***$readingsAverageLimit = 5;***

## Datastore	
Server will persist values to simple files located by naming conventions below. 
Note: {id} will be replaced by the real integer presented by the incoming request's URL.

	$valueFileFolder = 'values' (name of the folder to contain the measurement files)
	$messageFileName = 'message.msg' (name of the message text file)
	$readingsFilesNames = 'reading{id}.avg' (name of the CSV averaged readings file)
	$flagFilesNames = 'flag{id}.flg' (name of the boolean flag value flag file)
	
	
REMEMBER TO CHMOD 777 THE values/* files!

@reboot python /home/pi/PowerHub/device/outlet/buttons.py
@reboot python /home/pi/PowerHub/device/outlet/relay.py



