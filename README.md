# stepper-clock
24 hour stepper clock based on https://timhutton.github.io/2014/01/28/36976.html

## bill of materials
- Raspberry Pi Model 3 B+
- Adafruit DC & Stepper Motor HAT - https://www.adafruit.com/product/2348
- IR photogate (from an old Xerox printer)
- NEMA 23 stepper motor - from https://www.surplusgizmos.com/
- foamcore & aluminum for the structure

## implementation notes
use chrontab to run the script every fifteen minutes to update clock position.

## map image / clock face
use NASA program, rotate so my longitude is at the top of the circle.

## possible future upgrades / improvements
- leds or other way to indicate minutes / seconds in more accuracy is desired
- additional photogates to reduce stepper travel / homing routine
- rebuild / build enclosure and/or base for the works
