from typing import Any, get_type_hints

from h8core import EntityBaseMetaclass


class EntityBase(metaclass=EntityBaseMetaclass):
    def __init__(self, /, **kwargs: Any) -> None:
        for name, _ in get_type_hints(self).items():  # pylint: disable=no-member
            in_arguments = name in kwargs

            if not in_arguments:
                raise ValueError(f"{self.__class__.__name__} constructor key argument '{name}' is missing.")

            else:
                setattr(self, name, kwargs[name])
