"""
molssi_math.py
best practices workshop

Handles the primary functions
"""


def mean(my_list):
    """
    return the mean of a list

    Parameters
    ----------
    my_list : list of numbers to take average of

    Returns
    -------
    average : flt
        The mean of the list

    Examples
    --------
    >>>md.mean([1.0, 2.0, 3.0])
    2.0
    """

    if not isinstance(my_list, list):
        raise TypeError("Mean:  {} is not a list".format(my_list))
    if len(my_list) == 0:
        raise ZeroDivisionError("Mean: the input list contains no elements")
        
    average = sum(my_list) / len(my_list)

    return average


def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format)

    Replace this function and doc string for your own project

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
