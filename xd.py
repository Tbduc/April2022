import unittest
import ast
import inspect
from assessment import *

def are_all_numbers_positive(numbers):
    for n in numbers:
        if n < 1:
            return False
    return True


def are_all_numbers_in_range(numbers):
    min_range = 1
    max_range = 49
    for n in numbers:
        if n < min_range or n > max_range:
            return False
    return True


def are_all_numbers_unique(numbers):
    if len(numbers) > len(set(numbers)):
        return False
    return True


def check_if_sorted_used(method):
    ex_ast = ast.parse(inspect.getsource(method))
    for node in ast.walk(ex_ast):
        if isinstance(node, ast.Name) and node.id == "sorted":
            return True
    return False


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.test_filename = "tests/test.csv"
        self.draws = [
            ["25-26-31-33-38-42", "January", "3", "Oliver", "8447145.81", "London"],
            ["09-10-11-27-29-35", "January", "12", "George", "3296450.43", "Aberdeen"],
            ["03-06-25-35-41-47", "February", "15", "Harry", "17985213.34", "Birmingham"],
            ["05-08-17-37-40-45", "February", "27", "Jack", "39526201.37", "Bristol"],
            ["01-05-17-31-37-48", "February", "31", "Jacob", "5875966.85", "Derby"],
            ["02-07-15-21-27-36", "February", "14", "Thomas", "19122725.33", "Coventry"],
            ["09-19-28-31-32-38", "February", "26", "Filip", "6104250.81", "Liverpool"],
            ["04-13-29-30-34-46", "March", "1", "Emily", "16452293.45", "Manchester"],
            ["05-07-08-29-40-43", "March", "3", "Oliver", "27645021.48", "Southampton"],
            ["05-17-31-34-46-48", "March", "13", "Thomas", "24066017.87", "London"]
        ]

    def test_get_draws_function(self):
        actual = get_draws(self.test_filename)
        self.assertListEqual(actual, self.draws)

    def test_get_draw_numbers(self):
        expected = [25, 26, 31, 33, 38, 42]
        actual = get_draw_numbers("25-26-31-33-38-42")
        self.assertListEqual(actual, expected)

    def test_count_draws(self):
        expected = len(self.draws)
        actual = count_draws(self.draws)
        self.assertEqual(actual, expected)

    def test_get_all_unique_drawn_numbers(self):
        expected = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17, 19, 21, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
                    36, 37, 38, 40, 41, 42, 43, 45, 46, 47, 48}
        actual = get_all_unique_drawn_numbers(self.draws)
        self.assertSetEqual(actual, expected)

    def test_get_all_never_winning_numbers(self):
        expected = {12, 14, 16, 18, 20, 22, 23, 24, 39, 44, 49}
        actual = get_all_never_winning_numbers(self.draws)
        self.assertSetEqual(actual, expected)

    def test_get_dictionary_with_occurrences_of_drawn_numbers(self):
        expected = {1: 1, 2: 1, 3: 1, 4: 1, 5: 4, 6: 1, 7: 2, 8: 2, 9: 2, 10: 1, 11: 1, 13: 1, 15: 1, 17: 3, 19: 1,
                    21: 1, 25: 2, 26: 1, 27: 2, 28: 1, 29: 3, 30: 1, 31: 4, 32: 1, 33: 1, 34: 2, 35: 2, 36: 1, 37: 2,
                    38: 2, 40: 2, 41: 1, 42: 1, 43: 1, 45: 1, 46: 2, 47: 1, 48: 2}
        actual = get_dictionary_with_occurrences_of_drawn_numbers(self.draws)
        self.assertDictEqual(actual, expected)

    def test_get_most_winning_number(self):
        expected = 31
        actual = get_most_winning_number(self.draws)
        self.assertEqual(actual, expected)

    def test_get_all_numbers(self):
        expected = [25, 26, 31, 33, 38, 42, 9, 10, 11, 27, 29, 35, 3, 6, 25, 35, 41, 47, 5, 8, 17, 37, 40, 45, 1, 5, 17,
                    31, 37, 48, 2, 7, 15, 21, 27, 36, 9, 19, 28, 31, 32, 38, 4, 13, 29, 30, 34, 46, 5, 7, 8, 29, 40, 43,
                    5, 17, 31, 34, 46, 48]
        actual = get_all_numbers(self.draws)
        self.assertListEqual(actual, expected)

    def test_get_highest_prize(self):
        expected = 39526201.37
        actual = get_highest_prize(self.draws)
        self.assertEqual(actual, expected)

    def test_get_average_prize(self):
        expected = 16852128.67
        actual = get_average_prize(self.draws)
        self.assertEqual(actual, expected)

    def test_get_sorted_list_of_unique_winners_names(self):
        expected = ['Emily', 'Filip', 'George', 'Harry', 'Jack', 'Jacob', 'Oliver', 'Thomas']
        actual = get_sorted_list_of_unique_winners_names(self.draws)
        self.assertListEqual(actual, expected)

    def test_bubble_sort(self):
        expected = ["A", "B", "C", "D", "E"]
        actual = bubble_sort(["A", "C", "E", "B", "D"])
        self.assertListEqual(actual, expected)

    def test_check_if_number_ever_been_drawn_true_condition(self):
        expected = True
        actual = check_if_number_ever_been_drawn(self.draws, 1)
        self.assertEqual(actual, expected)

    def test_check_if_number_ever_been_drawn_false_condition(self):
        expected = False
        actual = check_if_number_ever_been_drawn(self.draws, 12)
        self.assertEqual(actual, expected)

    def test_if_check_if_number_ever_been_drawn_raise_error_when_given_number_out_of_range_lower_boundaries(self):
        self.assertRaisesRegex(ValueError, 'This number does not take part in the draw',
                               check_if_number_ever_been_drawn, self.draws, 0)

    def test_if_check_if_number_ever_been_drawn_raise_error_when_given_number_out_of_range_upper_boundaries(self):
        self.assertRaisesRegex(ValueError, 'This number does not take part in the draw',
                               check_if_number_ever_been_drawn, self.draws, 50)

    def test_if_generate_random_numbers_return_positive_numbers(self):
        expected = True
        numbers = generate_random_numbers()
        actual = are_all_numbers_positive(numbers)
        self.assertEqual(actual, expected)

    def test_if_generate_random_numbers_return_numbers_in_range(self):
        expected = True
        numbers = generate_random_numbers()
        actual = are_all_numbers_in_range(numbers)
        self.assertEqual(actual, expected)

    def test_if_generate_random_numbers_return_list_with_distinct_numbers(self):
        expected = True
        numbers = generate_random_numbers()
        actual = are_all_numbers_positive(numbers)
        self.assertEqual(actual, expected)

    def test_if_get_list_of_draws_in_month_return_list_for_valid_month_name(self):
        expected = [['25-26-31-33-38-42', 'January', '3', 'Oliver', '8447145.81', 'London'],
                    ['09-10-11-27-29-35', 'January', '12', 'George', '3296450.43', 'Aberdeen']]
        actual = get_list_of_draws_in_month(self.draws, "january")
        self.assertListEqual(actual, expected)

    def test_if_get_list_of_draws_in_month_return_empty_list_for_invalid_month_name(self):
        expected = []
        actual = get_list_of_draws_in_month(self.draws, "july")
        self.assertListEqual(actual, expected)

    def test_if_get_list_of_draws_in_month_raise_error_list_for_invalid_month_name(self):
        self.assertRaisesRegex(ValueError, 'Such month does not exists',
                               get_list_of_draws_in_month, self.draws, "not_existing_month")

    def test_get_month_with_most_number_of_winnings(self):
        expected = "february"
        actual = get_month_with_most_number_of_winnings(self.draws)
        self.assertEqual(actual, expected)

    def test_get_dict_with_cities_and_number_of_wins_in_them(self):
        expected = {
            'Aberdeen': 1,
            'Birmingham': 1,
            'Bristol': 1,
            'Coventry': 1,
            'Derby': 1,
            'Liverpool': 1,
            'London': 2,
            'Manchester': 1,
            'Southampton': 1
        }
        actual = get_dict_with_cities_and_number_of_wins_in_them(self.draws)
        self.assertDictEqual(actual, expected)

    def test_get_list_with_top_5_winnings_in_last_year_descending(self):
        expected = [39526201.37, 27645021.48, 24066017.87, 19122725.33, 17985213.34]
        actual = get_list_with_top_5_winnings_in_last_year_descending(self.draws)
        self.assertListEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
