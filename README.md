# Micropython HTTP sensor server

Simple HTTP server to display temperature sensor readings.

Made for the WiPy, but should run on any micropython platform.

The WiPy does not support floating point operations, so a logarithmic lookup table is used for converting between ADC pin values and temperature.

The code has been tested and calibrated with a scavenged temperature sensor from a broken outdoor thermometer.

Example output:

```
I have been alive for 6703 s.

The temperature is -5.5 C.

Best regards,
WiPy
```
