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
        mat = Matrix(
                4,
                5,
                [
                    ["A", "B", "C", "D", "E"],
                    ["F", "G", "H", "J", "I", "J"],
                    ["K", "L", "M", "N", "O"],
                    [None, 1, 2, 3, None],
                ],
            )
        # logger.info(mat.get_moves(1, 1))
        # logger.info(mat.get_moves(2, 2))
        # logger.info(mat.get_moves(0, 0))
        # logger.info(mat.get_moves(2, 4))
        logger.info(mat.gen_seq(1,0))
    except ValueError as val_err:
        logger.exception(val_err)


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
