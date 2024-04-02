from enum import Enum
from typing import Union


Comparator = Enum('Comparator', ['NOT_EQUAL', 'LESS', 'LESS_EQUAL', 'GREATER', 'GREATER_EQUAL', 'EQUAL'])
VisibilityStat = Enum('VisibilityStat', ['PUBLIC', 'PRIVATE'])
LogicModifier = Enum('LogicModifier', ['NOT'])
LogicOperator = Enum('LogicOperator', ['OR', 'AND'])
AttribModifier = Enum('AttribModifier', ['LIVE', 'PREV'])

ValueType = Union[int, float, bool, str]
MetaDataType = dict[str, ValueType]