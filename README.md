# Micropython HTTP sensor server

Simple HTTP server to display temperature sensor readings.

Made for the WiPy, but should run on any micropython platform.

The WiPy does not support floating point operations, so a logarithmic lookup table is used for converting between ADC pin values and temperature.

The code has been tested and calibrated with a scavenged temperature sensor from a broken outdoor thermometer.

