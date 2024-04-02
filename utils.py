from typing import Generic, TypeVar, Optional


T1 = TypeVar('T1')
class Ref(Generic[T1]):
    def __init__(self, id_: str, val: Optional[T1]=None):
        self._id = id_
        self._val = val

    def assign(val: T1) -> None:
        self._val = val

    @property
    def free(self) -> bool:
        return self._obj is None

    def __call__(self) -> T1:
        return self._val

    def __repr__(self):
        return f'Ref[{type(self._val).__name__}]({self._val})'


T2 = TypeVar('T2')
class RefManager(Generic[T2]):
    def __init__(self):
        self._items: dict[str, Ref[T2]] = {}

    def register_ref(self, ref: Ref[T2]) -> str:
        self._items[ref.id_] = ref
        return ref.id_

    def register_item(self, id_: str, item: T2) -> None:
        if id_ in self._items:
            ref_: Ref[T2] = self._items[id_]
        else:
            ref_: Ref[T2] = Ref(id_=id_, val=item)
        if ref_.free:
            ref_.assign(entity=entity)
        elif not item is ref_():
            raise KeyError()

    def remove(self, id_: str) -> None:
        del self._items[id_]

    def validate(self) -> bool:
        return not any(e.free for e in self._items.values())