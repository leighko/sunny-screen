
# Practice with classes -- will not be used in the final implementation
class Sunscreen:
    def __init__(
        self,
        name: str,
        spf: int,
        category: int,
        pa_rating: str,
        special: list,
        active: list,
        inactive: list,
    ):
        self._name = name
        self._spf = spf
        self._category = category
        self._pa_rating = pa_rating
        self._special_categories = special
        self._active_ingredients = active
        self._inactive_ingredients = inactive

    def which_category(self):
        if self._category == 1:
            self._category = "face"
        elif self._category == 2:
            self._category = "body"
        elif self._category == 3:
            self._category = "face/body"
        else:
            raise ValueError("Incorrect Category.")
        return self._category

    def sunscreen_dict(self):
        self.sunscreen_dictionary = {
            "Name": self._name,
            "SPF": self._spf,
            "Category": self._category,
            "PA Rating": self._pa_rating,
            "Special categories": self._special_categories,
            "Active ingredients": self._active_ingredients,
            "Inactive ingredients": self._inactive_ingredients,
        }
        return self.sunscreen_dictionary

    def __str__(self):
        return self._name

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    @property
    def pa_rating(self):
        return self._pa_rating

    @property
    def special_categories(self):
        return self._special_categories

    @property
    def active_ingredients(self):
        return self._active_ingredients

    @property
    def inactive_ingredients(self):
        return self._inactive_ingredients

    @property
    def spf(self):
        return self._spf
