# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 10/23/2024
# Description: Modify insertion sort to sort a list of strings instead of numbers.
def string_sort(string_list):
    """
    Sorts a list of strings in place using insertion sort.
    """
    for i in range(1, len(string_list)):
        current_string = string_list[i]
        j = i -1
        while j >= 0 and string_list[j].lower() > current_string.lower():
            string_list[j+1] = string_list[j]
            j -= 1
            string_list[j+1] = current_string