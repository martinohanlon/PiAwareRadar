#Pi Aware Radar
##Martin O'Hanlon (martin@ohanlonweb.com)
##http://www.stuffaboutcode.com

##Description
A radar for PiAware showing the aircraft being picked up around your gps position.
[http://www.stuffaboutcode.com/2015/11/piaware-radar.html](http://www.stuffaboutcode.com/2015/11/piaware-radar.html)

##Structure
* piawareradar
  * piawareradar.py - main program which creates a radar based on data from Piaware
  * flightdata.py - python module to read data from pi aware
  * gpsutils.py - gps utilities
  * radar.py - a python module to create a radar using pygame
  * const_normal.py - the constants which are used for the normal screen
  * const_touch.py - the constants which are used for the touch screen
* LICENSE - license information
* README.md - this file

##Install

    git clone https://github.com/martinohanlon/PiAwareRadar

##Usage

    usage: piawareradar.py [-h] [--piawareip PIAWAREIP] [--screen SCREEN] [--fullscreen] lat lon
    
    PiAware Flight Radar
    
    positional arguments:
      lat                   The latitude of the receiver
      lon                   The longitude of the receiver

    optional arguments:
      -h, --help            show this help message and exit
      --piawareip PIAWAREIP The ip address of the piaware server
      --screen SCREEN       The screen config to use [normal / touch]
      --fullscreen          Fullscreen radar
    
##Run

    python3 PiAwareRadar/piawareradar/piawareradar.py 12.3456 -12.3456

##Version history
* 0.1 - Initial stable version
