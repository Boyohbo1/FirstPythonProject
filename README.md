# First Python Project

This Python project was written for the sake of learning the language. It takes `.json` files from the internet using a url
and converts them into a list, which can then be sorted using keys. Within the module there are three functions:

## `tester'
This is used as a test script for the code used throughout the module. It has a list with embedded dictionaries (keys are 
"year", "size", and "landed", but they do not mean anything), which are then sorted by their keys and printed.

## `websearch`
This is used to pull `.json` files from the internet using a url and convert them into a list and display the keys (the argument
in this function is not currently implemented, but will be with the next commit).

## `puller'
This function is used to sort lists based on their keys, both of which come from the `websearch` function (there are currently 
some problems with certain keys in some datasets, but it is being looked at).

>[!NOTE]
>The `websearch` function must be executed before `puller`, otherwise it will not function.
>All arguments must be written in quotes, otherwise it will not recognize the string.
