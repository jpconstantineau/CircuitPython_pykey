# SPDX-FileCopyrightText: Copyright (c) 2021 Pierre Constantineau
#
# SPDX-License-Identifier: MIT
"""
module docstring
"""
from digitalio import DigitalInOut, Direction


class KB_LEDMatrix:
    """
    Class Docstring
    """
    # LEDMatrix(row_pins: Sequence[microcontroller.Pin], 
    # column_pins: Sequence[microcontroller.Pin], columns_to_anodes: bool = True)


    def __init__(self, row_pins, column_pins, columns_to_anodes: bool = True):
        """
        docstring
        """
        self.row_pins = row_pins
        self.column_pins = column_pins
        self.columns_to_anodes = columns_to_anodes
        self.column_io = []
        self.row_io = []
        for col_p in self.column_pins:
            self.column_io.append(DigitalInOut(col_p))
        for row_p in self.row_pins:
            self.row_io.append(DigitalInOut(row_p))

    def reset_leds(self):
        """
        docstring
        """
        for pin in self.row_io:
            pin.direction = Direction.OUTPUT
            pin.value = False
        for pin in self.column_io:
            pin.direction = Direction.OUTPUT
            pin.value = False

    def led_ON(self, led_number):  # pylint: disable=invalid-name
        """
        doctrsing
        """
        self.reset_leds()
        colcount=len(self.column_io)
        colIO_LED = self.column_io[0]  # pylint: disable=invalid-name
        rowIO_LED = self.row_io[0]  # pylint: disable=invalid-name
        for rownum, row_pin in enumerate(self.row_io):
            for colnum, col_pin in enumerate(self.column_io):
                if led_number == (rownum * colcount + colnum):
                    colIO_LED = col_pin  # pylint: disable=invalid-name
                    rowIO_LED = row_pin  # pylint: disable=invalid-name
                if self.columns_to_anodes:
                    col_pin.value = False
                    row_pin.value = True
                else:
                    col_pin.value = True
                    row_pin.value = False
        if self.columns_to_anodes:
            colIO_LED.value = True
            rowIO_LED.value = False
        else:
            colIO_LED.value = False
            rowIO_LED.value = True

    def led_OFF(self):  # pylint: disable=invalid-name
        """
        docstrings
        """
        self.reset_leds()

