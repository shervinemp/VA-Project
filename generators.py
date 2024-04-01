import random
from abc import ABC, abstractmethod

class GeneratorBase(ABC):
    def __init__(self, values, seed=0):
        self._v = values
        self._seed = seed
    
    @abstractmethod
    def __call__(self):
        pass

class RandomGenerator(GeneratorBase):
    def __init__(self, values, seed=0):
        self._rng = random.Random(seed)
        super(RandomGenerator, self).__init__(values=values, seed=seed)
    
    def __call__(self):
        return self._rng.choice(self._v)

class RoundRobinGenerator(GeneratorBase):
    def __init__(self, values, seed=0):
        self._offset = 0
        super(RoundRobinGenerator, self).__init__(values=values, seed=seed)
    
    def __call__(self):
        self._offset += 1
        return self._v[(self._seed + self._offset - 1) % len(self._v)]