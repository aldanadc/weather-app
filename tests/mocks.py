"""This file contains mocked objects to be used in unit testing."""


mocked_get_coordinates_value = [{
    'name': 'Dublin',
    'local_names': {
        'ug': 'دۇبلىن', 'nl': 'Dublin',
        'ms': 'Dublin', 'br': 'Dulenn', 'tr': 'Dublin',
        'pt': 'Dublin', 'eu': 'Dublin', 'th': 'ดับลิน', 'e en': 'Dublin',
        'af': 'Dublin', 'ce': 'Дублин', 'cu': 'Доублинъ', 'pl': 'Dublin',
        'yi': 'דובלין', 'it': 'Dublino', 'uz': 'Dublin', 'tg': 'Дублин',
        'hi': 'डबलिन', 'cv': 'Дублин', 'az': 'Dublin', 'et': 'Dublin',
        'vo': 'Baile Átha Cliath', 'jv': 'Dublin', 'tt': 'Дублин',
        'ko': '더블린', 'ht': 'Diblin', 'bn': 'ডাবলিন', 'mt': 'Dublin',
        'ca': 'Dublín', 'fo': 'Dublin', 'ba': 'Дублин', 'so': 'Dublin',
        'cs': 'Dublin', 'el': 'Δουβλίνο', 'sh': 'Dublin', 'sq': 'Dublini',
        'fr': 'Dublin', 'av': 'Дублин', 'or': 'ଡବଲିନ', 'hu': 'Dublin',
        'fy': 'Dublin', 'mi': 'Tapurini', 'my': 'ဒပ်ဗလင်မြို့', 'sl': 'Dublin',
        'mk': 'Даблин', 'ga': 'Baile Átha Cliath', 'rm': 'Dublin',
        'id': 'D     Dublin', 'te': 'డబ్లిన్', 'ps': 'ډبلن', 'ee': 'Dublin',
                                    'de': 'Dublin', 'ia': 'Dublin', 'nv': 'Tóhodiłhił', 'lb': 'Dublin',
                                    'es': 'Dublín', 'bo': 'དུབ་ལིན།', 'an': 'Du    ublín', 'tl': 'Dublin',
                                    'hr': 'Dublin', 'ay': 'Dublin', 'om': 'Dubliin', 'ru': 'Дублин',
                                    'sc': 'Dublinu', 'wo': 'Dublin', 'sd': 'ڊبلن', 'ta': 'டப்லின்',
                                    'mn': 'Дублин', 'hy': 'Դուբլին', 'zh': '都柏林', 'ky': 'Дублин',
                                    'gd': 'Baile Àtha Cliath', 'na': 'Dublin', 'sr': 'Даблин', 'yo': 'Dublin',
                                    'gv': 'Divlyn', 'fa': 'دوبلین', 'da': 'Dublin', 'am': 'ደብሊን',
                                    'uk': 'Дублін', 'he': 'דבלין', 'ku': 'Dublîn', 'nn': 'Dublin',
                                    'bg': 'Дъблин', 'rw': 'Dublin', 'fi': 'Dublin', 'sn': 'Dublin',
                                    'mr': 'डब्लिन', "ur": 'ڈبلن', 'sk': 'Dublin', 'ro': 'Dublin',
                                    'be': 'Дублін', 'cy': 'Dulyn', 'bs': 'Dublin', 'vi': 'Dublin',
                                    'pa': 'ਡਬਲਿਨ', 'lt': 'Dublinas', 'la': 'Eblana', 'ml': 'ഡബ്ലിൻ',
                                    'qu': 'Baile Átha Cliath', 'gl': 'Dublín - Baile Átha Cliath',
                                    'sv': 'Dublin', 'is': 'Dyflinn', 'li': 'Dublin', 'ie': 'Dublin',
                                    'kk': 'Дублин', 'oc': 'Dublin', 'no': 'Dublin', 'os': 'Дублин',
                                    'eo': 'Dublino', 'kw': 'Dulyn', 'ka': 'დუბლინი', 'lv': 'Dublina',
                                    'se': 'Dublin', 'ln': 'Dublin', 'wa': 'Dublin', 'sw': 'Dublin',
                                    'ar': 'دبلن', 'ja': 'ダブリン', 'io': 'Dublin'},
    'lat': 53.3498006, 'lon': -6.2602964, 'country': 'IE'
}]


mocked_get_weather_value = '<?xml version="1.0" encoding="UTF-8"?>\n<current><city id="2962486" name="Mountjoy">\
                            <coord lon="-6.2603" lat="53.3498"></coord><country>IE</country><timezone>0</timezone>\
                            <sun rise="2024-01-29T08:15:33" set="2024-01-29T17:00:21"></sun></city><temperature\
                            value="5.16" min="4.62" max="5.54" unit="celsius"></temperature><feels_like value="1.47" unit="celsius">\
                            </feels_like><humidity value="91" unit="%"></humidity><pressure value="1022" unit="hPa">\
                            </pressure><wind><speed value="5.14" unit="m/s" name="Gentle Breeze"></speed><gusts></gusts>\
                            <direction value="320" code="NW" name="Northwest">\
                            </direction></wind><clouds value="75" name="broken clouds"></clouds><visibility value="10000">\
                            </visibility><precipitation value="0.74" mode="rain" unit="1h"></precipitation>\
                            <weather number="500" value="light rain" icon="10n"></weather><lastupdate value="2024-01-29T19:17:52">\
                            </lastupdate></current>'


mocked_get_forecast_value = {'cod': '200', 'message': 0, 'cnt': 40,
                             'list': [
                                 {'dt': 1706562000,
                                  'main': {'temp': 5.28, 'feels_like': 1.82, 'temp_min': 4.17, 'temp_max': 5.28,
                                           'pressure': 1022, 'sea_level': 1022, 'grnd_level': 1021, 'humidity': 90, 'temp_kf': 1.11},
                                  'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}],
                                  'clouds': {'all': 75}, 'wind': {'speed': 4.72, 'deg': 324, 'gust': 10.17},
                                  'visibility': 10000, 'pop': 0.28, 'sys': {'pod': 'n'}, 'dt_txt': '2024-01-29 21:00:00'},
                                 {'dt': 1706572800,
                                     'main': {'temp': 4.31, 'feels_like': 0.46, 'temp_min': 2.36,
                                              'temp_max': 4.31, 'pressure': 1023, 'sea_level': 1023, 'grnd_level': 1023,
                                              'humidity': 90, 'temp_kf': 1.95},
                                     'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds',
                                                  'icon': '04n'}], 'clouds': {'all': 73},
                                  'wind': {'speed': 5.02, 'deg': 305, 'gust': 12.57},
                                  'visibility': 10000, 'pop': 0.18, 'sys': {'pod': 'n'},
                                  'dt_txt': '2024-01-30 00:00:00'},
                                 {'dt': 1706583600,
                                  'main': {'temp': 2.4, 'feels_like': -1.09, 'temp_min': 0.96,
                                           'temp_max': 2.4, 'pressure': 1025, 'sea_level': 1025, 'grnd_level': 1024,
                                           'humidity': 92, 'temp_kf': 1.44},
                                  'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds',
                                              'icon': '03n'}], 'clouds': {'all': 30},
                                  'wind': {'speed': 3.63, 'deg': 279, 'gust': 7.63},
                                  'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'},
                                  'dt_txt': '2024-01-30 03:00:00'}],
                             'city': {'id': 2962486, 'name': 'Mountjoy',
                                      'coord': {'lat': 53.3494, 'lon': -6.2606},
                                      'country': 'IE', 'population': 0, 'timezone': 0,
                                      'sunrise': 1706516133, 'sunset': 1706547621}
                             }

mocked_get_weather_by_city_value = {'location_name': 'Dublin, IE', 'temperature_c': '5.16 °C',
                                    'temperature_f': '41.29 °F', 'wind': 'Gentle Breeze, 5.14m/s, northwest',
                                    'cloudiness': 'Broken clouds', 'pressure': '1022 hpa', 'humidity': '91%',
                                    'sunrise': '05:15', 'sunset': '14:00', 'geocoordinates': '[53.3498, -6.2603]',
                                    'requested_time': '2024-01-29, 18:31:52',
                                    'forecast': {'2024-01-29 18hs':
                                                 {'weather': 'Broken clouds', 'temperature_c': '5.28 °C',
                                                  'temperature_f': '41.5 °F', 'max_temperature_c': '5.28 °C',
                                                  'max_temperature_f': '41.5 °F', 'min_temperature_c': '4.17 °C',
                                                  'min_temperature_f': '39.51 °F', 'feels_like_c': '1.82 °C',
                                                  'feels_like_f': '35.28 °F', 'humidity': '90%', 'clouds': '75%',
                                                  'precipitation_probability': '28%', 'pressure': '1022 hpa',
                                                  'wind_speed': '4.72 m/s', 'visibility': '10000 m'},
                                                 '2024-01-29 21hs':
                                                 {'weather': 'Broken clouds', 'temperature_c': '4.31 °C',
                                                  'temperature_f': '39.76 °F', 'max_temperature_c': '4.31 °C',
                                                  'max_temperature_f': '39.76 °F', 'min_temperature_c': '2.36 °C',
                                                  'min_temperature_f': '36.25 °F', 'feels_like_c': '0.46 °C',
                                                  'feels_like_f': '32.83 °F', 'humidity': '90%', 'clouds': '73%',
                                                  'precipitation_probability': '18%', 'pressure': '1023 hpa',
                                                  'wind_speed': '5.02 m/s', 'visibility': '10000 m'},
                                                 '2024-01-30 00hs':
                                                 {'weather': 'Scattered clouds', 'temperature_c': '2.4 °C',
                                                  'temperature_f': '36.32 °F', 'max_temperature_c': '2.4 °C',
                                                  'max_temperature_f': '36.32 °F', 'min_temperature_c': '0.96 °C',
                                                  'min_temperature_f': '33.73 °F', 'feels_like_c': '-1.09 °C',
                                                  'feels_like_f': '30.04 °F', 'humidity': '92%', 'clouds': '30%',
                                                  'precipitation_probability': '0%', 'pressure': '1025 hpa',
                                                  'wind_speed': '3.63 m/s', 'visibility': '10000 m'}}}


mocked_invalid_city_response_value = {
    "cod": "404", "message": "city not found"}

mocked_invalid_lon_response_value = {
    "cod": "400", "message": "wrong longitude"}

mocked_invalid_lat_response_value = {"cod": "400", "message": "wrong latitude"}
