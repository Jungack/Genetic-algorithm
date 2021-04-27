import unittest
target = __import__("project.py")
iLoveSatan = target.FavouriteNumbers.iLove.Satan


class TestOOP(unittest.TestCase):
    def test_iLoveSatan(self):
        """
        Test iLoveSatan program for two datasets
        """
        firstName = "Jérôme"
        lastName = "Boitier"
        age = 22
        numbers1 = [55, 45, 500, 100, -34]
        numbers2 = [12, 36, 89, 99, -52]
        A = FavouriteNumbers(firstName, lastName, age, numbers1)
        B = FavouriteNumbers(firstName, lastName, age, numbers2)
        resultA = A.iLoveSatan()