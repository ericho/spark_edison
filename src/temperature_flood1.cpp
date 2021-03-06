* Author: Ivan De Cesaris <ivan.de.cesaris@intel.com>
 * Copyright (c) 2015 Intel Corporation.
 *
 * Permission is hereby granted, free of charge, to any person obtaining
 * a copy of this software and associated documentation files (the
 * "Software"), to deal in the Software without restriction, including
 * without limitation the rights to use, copy, modify, merge, publish,
 * distribute, sublicense, and/or sell copies of the Software, and to
 * permit persons to whom the Software is furnished to do so, subject to
 * the following conditions:
 *
 * The above copyright notice and this permission notice shall be
 * included in all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
 * MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 * NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS 
BE
 * LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN 
ACTION
 * OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
 * WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 */
#include "grove.h" include "jhd1313m1.h" include <climits> include 
#<iostream> include <sstream> include <unistd.h>
/*
 * Grove Starter Kit example
 *
 * Demonstrate the usage of various component types using the UPM 
library.
 *
 * - digital in: GroveButton connected to the Grove Base Shield Port D2
 * - analog in: GroveTemp connected to the Grove Base Shield Port A1
 * - I2C: Jhd1313m1 LCD connected to any I2C on the Grove Base Shield
 *
 * Additional linker flags: -lupm-i2clcd -lupm-grove
 */ /*
 * Update the temperature values and reflect the changes on the LCD
 * - change LCD backlight color based on the measured temperature,
 * a cooler color for low temperatures, a warmer one for high 
temperatures
 * - display current temperature
 * - record and display MIN and MAX temperatures
 * - reset MIN and MAX values if the button is being pushed
 * - blink the led to show the temperature was measured and data updated
 */ void temperature_update(upm::GroveTemp* temperature_sensor, 
upm::GroveButton* button, upm::Jhd1313m1 *lcd) {
	// minimum and maximum temperatures registered, the initial 
values will be
	// replaced after the first read
	static int min_temperature = INT_MAX;
	static int max_temperature = INT_MIN;
	// the temperature range in degrees Celsius,
	// adapt to your room temperature for a nicer effect!
	const int TEMPERATURE_RANGE_MIN_VAL = 18;
	const int TEMPERATURE_RANGE_MAX_VAL = 31;
	// other helper variables
	int temperature; // temperature sensor value in degrees Celsius
	float fade; // fade value [0.0 .. 1.0]
	uint8_t r, g, b; // resulting LCD backlight color components [0 
.. 255]
	std::stringstream row_1, row_2; // LCD rows
	// update the min and max temperature values, reset them if the 
button is
	// being pushed
	temperature = temperature_sensor->value();
	if (button->value() == 1) {
		min_temperature = temperature;
		max_temperature = temperature;
	} else {
		if (temperature < min_temperature) {
			min_temperature = temperature;
		}
		if (temperature > max_temperature) {
			max_temperature = temperature;
		}
	}
	// display the temperature values on the LCD
	row_1 << "Temp " << temperature << " ";
	row_2 << "Min " << min_temperature << " Max " << max_temperature 
<< " ";
	lcd->setCursor(0,0);
	lcd->write(row_1.str());
	lcd->setCursor(1,0);
	lcd->write(row_2.str());
	// set the fade value depending on where we are in the 
temperature range
	if (temperature <= TEMPERATURE_RANGE_MIN_VAL) {
		fade = 0.0;
	} else if (temperature >= TEMPERATURE_RANGE_MAX_VAL) {
		fade = 1.0;
	} else {
		fade = (float)(temperature - TEMPERATURE_RANGE_MIN_VAL) 
/
				(TEMPERATURE_RANGE_MAX_VAL - 
TEMPERATURE_RANGE_MIN_VAL);
	}
	// fade the color components separately
	r = (int)(255 * fade);
	g = (int)(64 * fade);
	b = (int)(255 * (1 - fade));
	// apply the calculated result
	lcd->setColor(r, g, b);
}
int main() {
	// check that we are running on Galileo or Edison
	mraa_platform_t platform = mraa_get_platform_type();
	if ((platform != MRAA_INTEL_GALILEO_GEN1) &&
			(platform != MRAA_INTEL_GALILEO_GEN2) &&
			(platform != MRAA_INTEL_EDISON_FAB_C)) {
		std::cerr << "Unsupported platform, exiting" << 
std::endl;
		return MRAA_ERROR_INVALID_PLATFORM;
	}
	// button connected to D2 (digital in)
	upm::GroveButton* button = new upm::GroveButton(2);
	// temperature sensor connected to A1 (analog in)
	upm::GroveTemp* temp_sensor = new upm::GroveTemp(1);
	// LCD connected to the default I2C bus
	upm::Jhd1313m1* lcd = new upm::Jhd1313m1(0);
	// simple error checking
	if ((button == NULL) || (temp_sensor == NULL) || (lcd == NULL)) 
{
		std::cerr << "Can't create all objects, exiting" << 
std::endl;
		return MRAA_ERROR_UNSPECIFIED;
	}
	// loop forever updating the temperature values every second
	for (;;) {
		temperature_update(temp_sensor, button, lcd);
		sleep(1);
	}
	return MRAA_SUCCESS;
}
