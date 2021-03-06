import util.TimeOps as clock
import random
import util.Geo as Geo
import util.Strings as Strings
from operationscore.Input import *
class RandomLocs(Input):
    """RandomLocs is an Input that generates RandomLocations at a preset time interval.  Just a
    prototype, some assembly required."""

    def inputInit(self):
        self['LastEvent'] = clock.time()
    def sensingLoop(self): #TODO: move to params
        currentTime = clock.time()
        if currentTime - self['LastEvent'] > 2000:
            self.respond({Strings.LOCATION: Geo.randomLoc((50,50))})
            self['LastEvent'] = currentTime
