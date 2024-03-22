# my_module.py

from ncm import *
import time
import os
import re

def show_current_time():
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    print("Current time:", current_time)

def show_compilation_time():
    start_time = time.time()
    # Simulate some code execution
    time.sleep(1)
    end_time = time.time()
    compilation_time = end_time - start_time
    print("Compilation time:", compilation_time, "seconds")

def show_file_location():
    file_location = os.path.abspath(__file__)
    print("File location:", file_location)

def show_file_type(file_name):
    file_type = os.path.splitext(file_name)[1]
    print("File type:", file_type)

def count_total_characters(file_name):
    with open(file_name, 'r') as file:
        total_characters = len(file.read())
    print("Total characters:", total_characters)

def count_total_words(file_name):
    with open(file_name, 'r') as file:
        total_words = len(re.findall(r'\w+', file.read()))
    print("Total words:", total_words)

def run_it(my_file_name):
    my_file = file_to_array(my_file_name)
    header_file = file_to_array("lib/header_lib/header.lib")

    # Check if there is a match between the files
    match_header = check_match_value(my_file, header_file)

    # Get the index of the matched value in the header file
    match_value_index = get_match_value_index(my_file, header_file)

    # Read the value from the index in the matched value in the header file
    match_index_value = read_value_by_index(my_file, match_value_index)
    match_index_value = array_to_word(match_index_value)
    match_index_value = f"lib/tag_lib/{match_index_value}"

    # Convert the matched value to a word
    tag_file = file_to_array(match_index_value)
   
    # Check if there is a match between the files using the tag file
    check_match_tag_file = check_match_value(my_file, tag_file)

    # Get the index of the matched value in the tag file
    match_file_index_1 = get_match_value_index(tag_file, my_file)

    # Read the value from the index in the tag file
    match_file_value = read_value_by_index(tag_file, match_file_index_1)

    # Get the index of the next word after the matched value in the tag file
    next_index = match_file_index_1 + 1

    # Read the value from the next index in the tag file
    next_value = read_value_by_index(tag_file, next_index)

    # Get the index of the matched value in the my file using the tag file
    match_value_index_2 = get_match_value_index(my_file, tag_file)

    # Replace the matched value in my file with the next value from tag file
    my_file[match_value_index_2:match_value_index_2+len(tag_file)] = []
    my_file[match_value_index_2:match_value_index_2] = tag_file
    my_file = array_to_sentence(my_file)

    # Write the corrected file back
    with open(f"{my_file_name}.epp", "w") as file:
        file.write(my_file)

    # Additional functionalities
    print("________________________")
    print("Additional Function:")
    show_current_time()
    show_compilation_time()
    show_file_location()
    show_file_type(my_file_name)
    count_total_characters(my_file_name)
    count_total_words(my_file_name)
    print("VER 2.")
    print("PixelPage Mark Up Language.")
    print("Powerd by Carbon Softwere Lab,Abdun Nur Porag")
