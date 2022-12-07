import subprocess
import random



def run_one (num1: int, num2: int) -> None:
    i1 = str (num1)
    i2 = str (num2)
    assert int(
        subprocess.run(['python', 'add.py', i1, i2], capture_output=True).stdout.decode('Utf-8')
    ) == num1 + num2


if __name__ == '__main__':
    # This is the first test case
    test_count = 0
    while test_count < 100:
        run_one(random.randint (1, 10000), random.randint (1, 10000))
        test_count += 1
    print("All finished fine!")