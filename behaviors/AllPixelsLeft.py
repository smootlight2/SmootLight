from operationscore.Behavior import *
import util.ComponentRegistry as compReg
import pdb
class AllPixelsLeft(Behavior):
    def processResponse(self, sensorInputs, recursiveInputs):
        for sensory in sensorInputs:
            xLoc = sensory['Location'][0] 
            if type(xLoc) == type(tuple()):
                pdb.set_trace()
            sensory['Location'] = '[{x}<' + str(xLoc) + ']'
        return (sensorInputs, recursiveInputs)
