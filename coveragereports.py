import unittest

class Coveragereports(unittest.TestCase):
    def test_function1(self):
        self.assertEqual(1, 0)

    def test_function2(self):
        self.assertNotEqual(2.1, 3)
        self.assertEqual((2.1  + 1.2), 3.3)

if __name__ == '__main__':
    unittest.main()


name: Tests
on: push

jobs:
  unit-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Setup python
        uses: actions/setup-python@v2
        with:
          python-version: 3.6

      - name: Install tools
        run: |
          python -m pip install --upgrade pip pytest
          pip install coverage                           #this is new

      - name: Test with unittest
        run: python3 -m unittest coveragereports.py
          
      - name: Check code coverage                        #new from here down
        run: |
          python3 -m coverage run -m unittest coveragereports.py
          python3 -m coverage report
          python3 -m coverage html
          
      - name: Archive code coverage HTML report
        uses: actions/upload-artifact@v2
        with:
           name: code-coverage-report
           path: htmlcov

git checkout -b coveragereports archive/<user_input>