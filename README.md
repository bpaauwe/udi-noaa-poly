
# NOAA weather service

This is a node server to pull weather data from the NOAA weather network and make it available to a [Universal Devices ISY994i](https://www.universal-devices.com/residential/ISY) [Polyglot interface](http://www.universal-devices.com/developers/polyglot/docs/) with  [Polyglot V2](https://github.com/Einstein42/udi-polyglotv2)

(c) 2020 Robert Paauwe

## Installation

1. Backup Your ISY in case of problems!
   * Really, do the backup, please
2. Go to the Polyglot Store in the UI and install.
3. Add NodeServer in Polyglot Web
   * After the install completes, Polyglot will reboot your ISY, you can watch the status in the main polyglot log.
4. Once your ISY is back up open the Admin Console.
5. Configure the node server per configuration section below.

### Node Settings
The settings for this node are:

#### Short Poll
   * How often to poll the NOAA weather service for current condition data (in seconds). 
#### Long Poll
	* How often to poll for alert data (in seconds)
#### Station
	* The weather station to use for for weather data. Go to https://w1.weather.gov/xml/current_obs/ to look up the station for your area.
#### Alert zone/county code
	* The code from alerts.weather.gov that specify the zone or county you want alerts for.  Look up the code on the site and enter it here, it will typically be a 6 character code.

## Node substitution variables
### Current condition node
 * sys.node.[address].ST      (Node sever online)
 * sys.node.[address].CLITEMP (current temperature)
 * sys.node.[address].CLIHUM  (current humidity)
 * sys.node.[address].DEWPT   (current dew point)
 * sys.node.[address].BARPRES (current barometric pressure)
 * sys.node.[address].SPEED   (current wind speed)
 * sys.node.[address].WINDDIR (current wind direction )
 * sys.node.[address].DISTANC (current visibility)
 * sys.node.[address].GV13    (current weather conditions)

 ### Alert infomation
 * sys.node.[address].GV21    (Alert text)
 * sys.node.[address].GV22    (Alert status)
 * sys.node.[address].GV23    (Alert message type)
 * sys.node.[address].GV24    (Alert category)
 * sys.node.[address].GV25    (Alert severity)
 * sys.node.[address].GV26    (Alert urgency)
 * sys.node.[address].GV27    (Alert certainy)

## Requirements
1. Polyglot V2.
2. ISY firmware 5.0.x or later

# Upgrading

Open the Polyglot web page, go to nodeserver store and click "Update" for "NOAA Weather".

Then restart the NOAA nodeserver by selecting it in the Polyglot dashboard and select Control -> Restart, then watch the log to make sure everything goes well.

The nodeserver keeps track of the version number and when a profile rebuild is necessary.  The profile/version.txt will contain the profile_version which is updated in server.json when the profile should be rebuilt.

# Release Notes

- 1.1.1 02/10/2021
   - Fix id for Winter Storm Warning
- 1.1.0 12/20/2020
   - Add alert data from alerts.weather.gov 
- 1.0.0 08/16/2020
   - Initial public release
