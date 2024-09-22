__all__ = [
    "ModuleBaseMetaclass",
]


class ModuleBaseMetaclass(type):
    def __init__(cls, name, bases, clsdict) -> None:
        if bases and len(bases) > 1:
            raise TypeError(
                f"You cannot declare multiple inheritance of a module class. Please check implementation of {name}"
            )

        if bases:
            base: type = bases[0]

            validation_list = [
                # ("adapters", AdaptersSetupBase),
                # ("middlewares", MiddlewaresSetupBase),
            ]

            for attr_name, clsbase in validation_list:
                if not hasattr(cls, name):
                    raise AttributeError(
                        f"Property '{attr_name}' must be defined in the class '{name}' derived from '{base.__name__}'"
                    )

                if not isinstance(getattr(cls, attr_name), clsbase):
                    raise AttributeError(f"Property '{attr_name}' must be an instance of {clsbase}.")

        super(ModuleBaseMetaclass, cls).__init__(name, bases, clsdict)
