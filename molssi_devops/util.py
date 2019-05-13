"""
util.py
A sample repository for the MolSSI Python package development workshop

Misc. utility functions
"""


def title_case(sentence):
    """
    Convert a string to title case.

    Title case means that the first letter of each word is capitalized, and all other letters in the word are lowercase.

    Parameters
    ----------
    sentence: str
      String to be converted to title case

    Returns
    -------
    ret: str
      String converted to title case.

    Example
    -------
    >>> title_case('ThIS is a STRinG to BE ConVerTeD.')
    'This Is A String To Be Converted.'
    """
    # Check that input is string
    if not isinstance(sentence, str):
        raise TypeError('Invalid input, type %s - Input must be type string' %(type(sentence)))

  # Capitalize first letter
    ret = sentence[0].upper()

# Loop through the rest of the characters
    for i in range(1, len(sentence)):
        if sentence[i - 1] == ' ':
            ret = ret + sentence[i].upper()
        else:
            ret = ret + sentence[i].lower()

    return ret
