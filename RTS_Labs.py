from typing import List, Dict


class RTSLabsChallenge:

    @staticmethod
    def aboveBelow(input_list: List[int], comparison_number: int) -> Dict:
        """
            Take a list and an integer and give the number of values above and below that value.
            Assumption that I should ignore equal to.

        :param input_list:  An unsorted collection of integers (the list)
        :param comparison_number: an integer (the comparison value)
        :return: a hash/object/map/etc. with the keys "above" and "below" with the corresponding count of integers
        from the list that are above or below the comparison value
        """
        output = {
            "above": 0,
            "below": 0
        }
        for element in input_list:
            if element < comparison_number:
                output["below"] = output["below"] + 1
            elif element > comparison_number:
                output["above"] = output["above"] + 1
        return output

    @staticmethod
    def aboveBelowEqual(input_list: List[int], comparison_number: int) -> Dict:
        """
            Take a list and an integer and returns the number of values above, below or Equal to that value.
            (Corrects the assumption above.)

        :param input_list:  An unsorted collection of integers (the list)
        :param comparison_number: an integer (the comparison value)
        :return: a hash/object/map/etc. with the keys "above" and "below" with the corresponding count of integers
        from the list that are above or below the comparison value
        """
        output = {
            "above": 0,
            "below": 0,
            "equal": 0
        }
        for element in input_list:
            if element < comparison_number:
                output["below"] = output["below"] + 1
            elif element > comparison_number:
                output["above"] = output["above"] + 1
            else:
                output["equal"] = output["equal"] + 1
        return output

    @staticmethod
    def stringRotation(input_string: str, rotation_amount: int) -> str:
        """
            Takes a String string and rotates the string to the right by the rotation amount. The overflow of the original string becomes the start of the new string.
        :param input_string: a string (the original string)
        :param rotation_amount: a positive integer (the rotation amount)
        :return: a new string, rotating the characters in the original string to the right by the rotation amount and have the overflow appear at the beginning
        """
        if rotation_amount < 0:
            raise ValueError("Value should be above 0.")
        if not input_string:
            return ""

        rotation_amount = rotation_amount % len(input_string)

        end_of_string = input_string[-rotation_amount:]
        start_of_string = input_string[:-rotation_amount]

        return end_of_string + start_of_string

