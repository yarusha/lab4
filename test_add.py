import io
import unittest
import json
import random
import unittest.mock
from add import add, main


class AddWorksCorrectly(unittest.TestCase):
    def setUp(self) -> None:
        print("setUp")
        #Load the test data
        with open("numbers.json", "r") as f:
            self.numbers = json.load(f)
            # print(self.numbers)

    def tearDown(self) -> None:
        print("tearDown")

    def test_add_two_numbers(self) -> None:
        for item in self.numbers:
            self.assertEqual(add(item['num1'], item['num2']), item['result'])

    def test_add_two_numbers_1(self) -> None:
        for item in self.numbers:
            self.assertEqual(add(item['num1'], item['num2']), item['result'])

    def test_add_two_numbers_2(self) -> None:
        t = 0
        while t < 100000:
            num1 = random.randint(1, 10000)
            num2 = random.randint(1, 10000)
            result = num1 + num2
            self.assertEqual(add(num1, num2), result)
            t += 1


class MainWorksCorrectly(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_main(self, mock_stdout: io.StringIO) -> None:
        main('1', '2')
        self.assertEqual("3\n", mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_main_raises(self, mock_stdout: io.StringIO) -> None:
        with self.assertRaises(ValueError):
            main('a', 'b')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_main_raises(self, mock_stdout: io.StringIO) -> None:
        with self.assertRaises(ValueError):
            main('1', 'b')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_main_raises(self, mock_stdout: io.StringIO) -> None:
        with self.assertRaises(ValueError):
            main('a', '2')