import ex5_1
import ex5_2
import ex5_3
import ex5_4


if __name__ == "__main__":
    ex5_1.show_files_by_pattern(r"c:\\", ex5_1.FILES_DEEP_PATTERN)
    ex5_1.check_if_monday(ex5_1.get_random_date(ex5_1.read_date(ex5_1.INPUT_DATE_MESSAGE),
                                                ex5_1.read_date(ex5_1.INPUT_DATE_MESSAGE)), ex5_1.MONDAY_MESSAGE)
    print(ex5_2.join([5], [4, 7], [3, 7, 8], seperator='-'))
    print(ex5_2.get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=300, milk=100))
    print(ex5_2.get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300, milk=100))
    ex5_3.find_binary_string(r"C:\Users\idanb\Downloads\Notebooks-master\Notebooks-master\week05\resources\logo.jpg",
                             ex5_3.BINARY_PATTERN)
    print(list(ex5_4.interleave('abc', [1, 2, 3, 4], [12, 12])))
