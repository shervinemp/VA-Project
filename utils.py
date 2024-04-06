from typing import Generic, TypeVar, Optional, Union, Any


T1 = TypeVar('T1')
class Ref(Generic[T1]):
    def __init__(self, value: Optional[T1]=None):
        self._value = value

    def assign(self, value: T1) -> None:
        self._value = value

    @property
    def is_empty(self) -> bool:
        return self._value is None

    def deref(self) -> Optional[T1]:
        return self._value

    def __call__(self) -> T1:
        return self.deref()

    def __repr__(self):
        return f'Ref[{type(self._value).__name__}]({self._value})'


class ConstRef(Ref):
    def assign(self, value: T1) -> Any:
        assert self.is_free
        return super(ConstRef, self).assign(value)


T2 = TypeVar('T2')
class RefDict(Generic[T2]):
    def __init__(self, *args, **kwargs):
        self._refs: dict[str, Ref[T2]] = {k: (v if isinstance(v, Ref) else Ref(v)) for k, v in dict(*args, **kwargs).items()}

    def __getitem__(self, key: str):
        return self._refs[key]

    def __setitem__(self, key: str, value: Optional[Union[Ref[T2], T2]]=None):
        if key in self._refs:
            self._refs.assign(value)
        else:
            self._refs[key] = value if isinstance(value, Ref) else Ref(value)

    def __delitem__(self, key):
        del self._refs[key]

    def __len__(self):
        return len(self._refs)

    def __iter__(self):
        return iter(self._refs)

    def __str__(self):
        return str(self._refs)

    def clear(self):
        self._refs.clear()

    def get(self, key, default=None):
        return self._refs.get(key, lambda: default).deref()

    def items(self):
        return map((lambda k, v: k, v.deref()),
                   self._refs.items())

    def keys(self):
        return self._refs.keys()

    def values(self):
        return map((lambda v: v.deref()),
                   self._refs.values())

    def pop(self, key, default=None):
        return self._refs.pop(key, default)

    def popitem(self):
        return self._refs.popitem()

    def update(self, *args, **kwargs):
        # self._refs.update(*args, **kwargs)
        raise NotImplementedError()

    def setdefault(self, key, default=None):
        return self._refs.setdefault(key, default)
    
    def to_dict(self):
        return {k: v.deref() for k, v in self._refs.items()}

    def dangling(self):
        return any(e.is_empty for e in self._refs.values())
