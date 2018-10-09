from NMEA0183 import NMEA0183
import time

serial_location = 'COM9'
serial_baudrate = 38400
serial_timeout = 5

# Provides the required serial device info
nmea = NMEA0183(serial_location, serial_baudrate, serial_timeout)

# Starts the serial connection
nmea.start()

# Checks if there is a valid connection
if nmea.exit == False:
    print('Connection!')

    # More info on data names below
    # Different data types require different devices...obviously...
    # Some examples...

    # GPS data
    # Holux does:
    ''''
    $GPRMC,211223.591,V,5011.0534,N,00835.2361,E,,,071018,,,N*7A
    $GPVTG,,T,,M,,N,,K,N*2C
    $GPGGA,211224.591,5011.0231,N,00835.2481,E,0,03,,-47.9,M,47.9,M,,0000*62
    $GPGSA,A,1,28,24,30,,,,,,,,,,,,*11
    $GPGSV,3,3,12,03,07,029,,19,06,142,19,10,04,334,19,11,02,046,16*7A
    '''
    while True:
        print('Lat {:f} Lon {:f} Alt {:f} Sats {:d}/{:d} hdop {:1.2f} vdop {:1.2f} {:1} Speed {:1.2f} Track {:1.2f}'.format(
            nmea.data_gps['lat'], nmea.data_gps['lon'], nmea.data_gps['alt'], nmea.data_gps['sats'],
            nmea.data_gps['vsats'], nmea.data_gps['hdop'], nmea.data_gps['vdop'], nmea.data_gps['q'],
            nmea.data_gps['speed'], nmea.data_gps['track']))
        time.sleep(1.0)

    # Depth data
    # print nmea.data_depth['feet']

    # Weather data
    # print nmea.data_weather['wind_angle']
    # print nmea.data_weather['water_temp']

    # Rudder data
    # print nmea.data_rudder['stbd_angle']

    # Quit the NMEA connection
    nmea.quit()

else:
    print('No connection!')