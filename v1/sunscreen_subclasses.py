from sunscreen_class import Sunscreen

# Practice using subclasses -- will not be used in the final implementation
class Innisfree(Sunscreen):
    def __init__(self):
        info_list = [
            "Innisfree",
            60,
            1,
            "++++",
            ["oil free", "non-comedogenic"],
            ["dflkjd", "deijf"],
            ["eowru", "werpoi"],
        ]
        super().__init__(*info_list)


class SuperGoop(Sunscreen):
    def __init__(self):
        info_list = [
            "SuperGoop",
            50,
            2,
            "++",
            ["non-comedogenic", "tinted", "oil free"],
            ["abscd", "sdlkjerio"],
            ["cvmneo", "qpoierd"],
        ]
        super().__init__(*info_list)
