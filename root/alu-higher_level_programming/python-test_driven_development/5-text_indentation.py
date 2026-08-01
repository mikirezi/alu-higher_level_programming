#!/usr/bin/python3
"""Module that prints a text with indentation after ., ? and :"""


def text_indentation(text):
    """Print text, adding 2 new lines after each ., ? or :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    i = 0
    for i, char in enumerate(text):
        result += char
        if char in ".?:" and (i + 1 >= len(text) or text[i + 1] == " "):
            result += "\n\n"
    lines = result.split("\n")
    for line in lines:
        print(line.strip())
