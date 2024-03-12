from sunscreen_subclasses import Innisfree, SuperGoop


def main():
    make_sunscreen_file(name="innisfree", sunscreen_class=Innisfree)
    make_sunscreen_file(name="supergoop", sunscreen_class=SuperGoop)


def make_sunscreen_file(name, sunscreen_class):
    name = sunscreen_class()
    name.which_category()
    with open(f"{name}.csv", "w") as file:
        for key in name.sunscreen_dict():
            file.write(f"{key}: {name.sunscreen_dict()[key]}\n")


if __name__ == "__main__":
    main()
