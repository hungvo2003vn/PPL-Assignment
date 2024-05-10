import os
import re

def update_test_numbers(file_name, start_number):
    file_path = os.path.join(os.getcwd(), 'test', file_name)
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Define a regular expression pattern to find test cases
    pattern = r'self\.assertTrue\(TestCodeGen\.test\(input, expect, (\d+)\)\)'

    # Define the function to be used for replacement
    def repl(match):
        nonlocal start_number
        start_number += 1
        return f'self.assertTrue(TestCodeGen.test(input, expect, {start_number}))'

    # Use re.sub to replace the test numbers
    updated_content = re.sub(pattern, repl, content)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)

# Provide the file name and starting number
file_name = 'CodeGenSuite.py'
start_number = 699  # Starting number to count from
update_test_numbers(file_name, start_number)