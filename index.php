<?php
/**
 * RetroDashboard Central Data Hub
 *  This is a small PHP site to place on a webhost of your choosing. 
 *  It has a simple API to get and set information to it. 
 *  Note: Don’t forget to include the .htaccess file for proper URL routing to take place.
 *
 * @author khinds
 * @license http://opensource.org/licenses/gpl-license.php GNU Public License
 */
include 'settings.php';

/**
 * check if a file is missing then create it if needed
 * @param $fileName
 */
function createFileIfMissing($fileName) {
	if (!file_exists($fileName)) touch($fileName);
}

/**
 * for any possible malicious behavior, 
 * 	sanitize the input from the GET / POST requests
 * @param $value
 */
function cleanInput($value) {
	return preg_replace("/[^a-zA-Z0-9\-\. ]/", "", $value);
}

/**
 * generate a file name with the given id inserted to the file name's provided template
 * @param $fileNameTemplate
 * @param $id
 */
function generateFileById($fileNameTemplate, $id) {
    $fileName = str_replace("{id}", $id, $fileNameTemplate);
    createFileIfMissing($fileName);
	return $fileName;
}

/**
 * for a given filename if the value is empty, the return a "default" value
 * @param $fileName
 * @param $default
 */
function getValueOrDefault($fileName, $default) {
	$value = file_get_contents($fileName);
	if (empty($value)) $value = $default;
	return $value;
}

/**
 * for a given filename if the value is empty, the return a "default" value
 * 	otherwise get the average of the last N number of readings
 * @param $fileName
 * @param $readingsAverageLimit
 * @param $default
 */
function getAverageOrDefault($fileName, $readingsAverageLimit, $default) {
	$valuesArray = preg_split("/,/", getValueOrDefault($fileName, $default));
	$total = 0;
	foreach ($valuesArray as $value) $total += $value;
	return round($total/$readingsAverageLimit, 0);
}

// set the basic JSON response with the default response object
header('Content-type: application/json');
$response = new stdClass();
$response->message = 'error: invalid request';

// define file names to set for values on the server
$valueFileFolder = 'values';
$messageFileName = $valueFileFolder.'/message.msg';
$readingsFilesNames = $valueFileFolder.'/reading{id}.avg';
$flagFilesNames = $valueFileFolder.'/flag{id}.flg';

// set readings average limit, the number of entries saved for each average value to be calculated against
$readingsAverageLimit = 5;

// process incoming request to map to the following actions below
$urlHost = $_SERVER['HTTP_HOST'];
$requestURI = $_SERVER['REQUEST_URI'];
$urlParts = parse_url("http://{$urlHost}{$requestURI}");

// get dashboard option
preg_match('/\/[a-zA-Z]+\/?/', $urlParts['path'], $matches);
$dashboardOption = '';
if (isset($matches[0])) $dashboardOption = trim($matches[0], '/');

// get id number for reading or flag if present
preg_match('/\/[0-9]\/?/', $urlParts['path'], $matches);
$idNumber = 0;
if (isset($matches[0])) $idNumber = trim($matches[0], '/');

// if we have a 'all' matched in the URL means, we should get ALL results for flag/reading
$getAll = false;
preg_match('/all/', $urlParts['path'], $matches);
if (isset($matches[0])) $getAll = true;

// get action value 'set'/'unset' for reading or flag if present
preg_match('/\/(set)|(unset)\/?/', $urlParts['path'], $matches);
$action = '';
if (isset($matches[0])) $action = trim($matches[0], '/');

// set action, we must check API secret key to continue
if ($action == 'set' || $action == 'unset') {
    $passed = false;
    foreach (getallheaders() as $name => $value) if ($name == 'api-key' && md5($secretAPIKey) == $value) $passed = true;
}
if (($action == 'set' || $action == 'unset') && !$passed) die('{"message":"error: invalid request"}');

// switch on the type of incoming request
switch ($dashboardOption) {

    case 'message':
    
	    createFileIfMissing($messageFileName);
		if ($action == 'set') {
			file_put_contents($messageFileName, cleanInput(file_get_contents("php://input")));
			$response->message = 'message contents has been updated';
			break;
		}
		$response->message = getValueOrDefault($messageFileName, '');
        break;
        
    case 'reading':
    
        // get/set individual reading
    	if (!empty($idNumber)) {
    		$readingsFile = generateFileById($readingsFilesNames, $idNumber);
			if ($action == 'set') {
			
				// keep a list of the last "readingsAverageLimit" number of values to later get the average of them
				$existingValuesArray = preg_split("/,/", getValueOrDefault($readingsFile, '0'));
				$existingValuesArray[] = cleanInput(file_get_contents("php://input"));
				file_put_contents($readingsFile, implode(',',array_slice($existingValuesArray, -$readingsAverageLimit, $readingsAverageLimit)));
				$response->message = 'reading value has been added to average';
				break;
			}
			$response->message = getAverageOrDefault($readingsFile, $readingsAverageLimit, '0');
		}
		
        // get all readings
		if ($getAll) {
    		$response->message = array();
		    for ($count=1; $count<5; $count++) {
                $readingsFile = generateFileById($readingsFilesNames, $count);
                $response->message[] = getAverageOrDefault($readingsFile, $readingsAverageLimit, '0');
		    }
		}
        break;

    case 'flag':
    
        // get/set individual flag
    	if (!empty($idNumber)) {
    		$flagFile = generateFileById($flagFilesNames, $idNumber);
    		
			// set boolean value of true/false based on incoming request URL
			if ($action == 'set' || $action == 'unset') {
				$flagValue = ($action == 'set') ? '1' : '0';
				file_put_contents($flagFile, $flagValue);
				$response->message = 'flag has been set';
				break;
			}
			$response->message = getValueOrDefault($flagFile, '0');
		}
		
        // get all flags
		if ($getAll) {
    		$response->message = array();
		    for ($count=1; $count<5; $count++) {
                $flagFile = generateFileById($flagFilesNames, $count);
                $response->message[] = getValueOrDefault($flagFile, '0');
		    }
		}
        break;
}

print json_encode($response);
