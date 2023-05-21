import minitorch


class ModuleA1(minitorch.Module):
    def __init__(self) -> None:
        super().__init__()
        self.p1 = minitorch.Parameter(5)
        self.non_param = 10
        self.a = ModuleA2()
        self.b = ModuleA3()

    def po(self):
        return [self]


class ModuleA2(minitorch.Module):
    def __init__(self) -> None:
        super().__init__()
        self.p2 = minitorch.Parameter(10)


class ModuleA3(minitorch.Module):
    def __init__(self) -> None:
        super().__init__()
        self.c = ModuleA4()


class ModuleA4(minitorch.Module):
    def __init__(self) -> None:
        super().__init__()
        self.p3 = minitorch.Parameter(15)


class OtherModule(minitorch.Module):
    pass


class MyModule(minitorch.Module):
    def __init__(self):
        super().__init__()
        self.parameters1 = minitorch.Parameter(15)
        self.data = 25
        self.sub_module = OtherModule()
        self.fly = ModuleA1()
        self.fly.a.add_parameter("po", 24)
        self.fly.fuhai = ModuleA3()


# mod = MyModule()
# print(mod.__dict__["_parameters"])
# mod.add_parameter("hongfu","lijing")
# setattr(mod.fly, "hongfu", ModuleA1())
# print(mod)


def work(f, *vals, arg=0, epsilon=1e-6):
    """
    if you could return,do you have to let it linger
    """
    arg_1 = [f(i) for i in vals]
    print(arg_1)


class MyClass:
    count = 0

    def __init__(self):
        MyClass.count += 10
        self.count = 1

    @classmethod
    def get_count(cls):
        return cls.count
