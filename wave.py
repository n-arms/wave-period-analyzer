from math import sin, cos, pi

class Wave:
    def eval(self, x):
        pass
    def derivative(self, x):
        pass

class Sine(Wave):
    def __init__(self, frequency):
        self.freq = frequency
    def eval(self, x):
        return sin(2 * pi * self.freq * x)
    def derivative(self, x):
        return 2 * pi * self.freq * cos(2 * pi * self.freq * x)

class Sum(Wave):
    def __init__(self, waves):
        for wave in wave:
            assert(instanceof(wave, Wave))
        self.waves = waves
    def eval(self, x):
        return sum([wave.eval(x) for wave in self.waves])
    def derivative(self, x):
        return sum([wave.derivative(x) for wave in self.waves])
