from typing import List, Dict, Optional
from pydantic import BaseModel, validator

class Examples(BaseModel):
    positive: List[str] = []
    negative: List[str] = []
    
    def __init__(self, **data):
        super().__init__(**data)
        self._pos_gen = DefaultGenerator(self.positive)
        self._neg_gen = DefaultGenerator(self.negative)

    def set_generator(self, generator, positive_case=True):
        if positive_case:
            self._pos_gen = generator
        else:
            self._neg_gen = generator

    def get(self, positive_case=True):
        return self._pos_gen() if positive_case else self._neg_gen()

    def __call__(self, positive_case):
        return self.get(self, positive_case=positive_case)

class TemplateItem(ABC):
    description: Optional[str] = None
    examples: Examples

    @validator('examples', pre=True)
    def _split_examples(cls, v):
        if isinstance(v, list):
            return {'positive': v}
        return v

class Intent(Template):
    pass

class Variable(Template):
    pass

class RootSchema(BaseModel):
    variables: Dict[str, Variable]
    intents: Dict[str, Intent]