import unittest

class Character:
    def __init__(self, name, animal):
        self.name = name
        self.animal = animal.lower()

class TestCharacterComprehensive(unittest.TestCase):

    def test_init_sets_name_correctly(self):
        char = Character("Arthur", "dog")
        self.assertEqual(char.name, "Arthur")

    def test_init_sets_animal_correctly(self):
        char = Character("Arthur", "dog")
        self.assertEqual(char.animal, "dog")

    def test_init_with_keyword_arguments(self):
        char = Character(name="Buster", animal="rabbit")
        self.assertEqual(char.name, "Buster")
        self.assertEqual(char.animal, "rabbit")

    def test_init_with_positional_arguments(self):
        char = Character("Francine", "monkey")
        self.assertEqual(char.name, "Francine")
        self.assertEqual(char.animal, "monkey")

    def test_animal_all_uppercase_is_lowercased(self):
        char = Character("Muffy", "CHIMPANZEE")
        self.assertEqual(char.animal, "chimpanzee")

    def test_animal_mixed_case_is_lowercased(self):
        char = Character("Brain", "AnTeAtEr")
        self.assertEqual(char.animal, "anteater")

    def test_animal_already_lowercase_remains_lowercase(self):
        char = Character("Binky", "bulldog")
        self.assertEqual(char.animal, "bulldog")

    def test_name_casing_is_preserved_uppercase(self):
        char = Character("D.W.", "aardvark")
        self.assertEqual(char.name, "D.W.")

    def test_name_casing_is_preserved_lowercase(self):
        char = Character("prunella", "rat")
        self.assertEqual(char.name, "prunella")

    def test_empty_string_name(self):
        char = Character("", "cat")
        self.assertEqual(char.name, "")

    def test_empty_string_animal(self):
        char = Character("Sue Ellen", "")
        self.assertEqual(char.animal, "")

    def test_special_characters_in_name(self):
        char = Character("René-François", "fox")
        self.assertEqual(char.name, "René-François")

    def test_special_characters_in_animal(self):
        char = Character("Alien", "xenomorph-32!")
        self.assertEqual(char.animal, "xenomorph-32!")

    def test_numeric_string_name(self):
        char = Character("12345", "robot")
        self.assertEqual(char.name, "12345")

    def test_numeric_string_animal(self):
        char = Character("R2D2", "42")
        self.assertEqual(char.animal, "42")

    def test_whitespace_only_name(self):
        char = Character("   ", "ghost")
        self.assertEqual(char.name, "   ")

    def test_whitespace_in_animal_preserved_but_lowercased(self):
        char = Character("George", "  GIRAFfe  ")
        self.assertEqual(char.animal, "  giraffe  ")

    def test_missing_arguments_raises_type_error(self):
        with self.assertRaises(TypeError):
            Character("Missing Animal")

    def test_passing_none_to_animal_raises_attribute_error(self):
        with self.assertRaises(AttributeError):
            Character("Fern", None)

    def test_passing_integer_to_animal_raises_attribute_error(self):
        with self.assertRaises(AttributeError):
            Character("Ladonna", 123)


if __name__ == "__main__":
    unittest.main()