"""
Main
"""
import logging
# import argparse
from matrix import Matrix

def main():
    """
    Main function
    """
    logger = logger_setup()
    try:
        # _parser = argparse.ArgumentParser(description="Input to start with")

        # for _i in range(10):
        row = int(input('Enter row index : '))
        col = int(input('Enter col index : '))
        for _i in range(10):
            mat = new_mat()
            logger.info(mat.gen_seq(row, col))
    except ValueError as val_err:
        logger.exception(val_err)

def new_mat():
    """
    Construct a new matrix
    """
    mat = Matrix(
                4,
                5,
                [
                    ["A", "B", "C", "D", "E"],
                    ["F", "G", "H", "I", "J"],
                    ["K", "L", "M", "N", "O"],
                    [None, 1, 2, 3, None],
                ],
            )
    return mat


def logger_setup():
    """
    A function for basic logger setup
    """
    logger = logging.getLogger('mylogger')
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())
    return logger


if __name__ == "__main__":
    main()
