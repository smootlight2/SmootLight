from PixelEvent import PixelEvent
class StepEvent(PixelEvent):
    def initEvent(self):
        self.validateArgs('StepEvent.params')
    def lightState(self,timeDelay):
        if timeDelay < self['LightTime'] or self['LightTime'] == -1:
            return self['Color']
        else:
            return None
    @staticmethod
    def generate(onTime, color):
        args = {'LightTime': onTime, 'Color': color}
        return StepEvent(args)

