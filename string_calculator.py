import re


class StringCalculator:
    __delimiter = '[,\n]'
    __local_numbers = ''
    __ignored_big_number = 1000

    def add(self, numbers: str):
        self.__local_numbers = numbers
        self.__set_delimiter()
        return self.__sum()

    def __set_delimiter(self):
        if self.__local_numbers.startswith('//'):
            delimiter_line = self.__local_numbers.splitlines()[0]
            self.__delimiter = delimiter_line[2:]
            self.__remove_delimiter_from_numbers(delimiter_line)

    def __remove_delimiter_from_numbers(self, delimiter_line):
        self.__local_numbers = self.__local_numbers[len(delimiter_line) + 1:]

    def __sum(self):
        result = 0
        for number in filter(lambda _number: len(_number) > 0, re.split(self.__delimiter, self.__local_numbers)):
            int_number = int(number)
            if int_number < 0:
                raise RuntimeError("negatives not allowed: " + number)
            if int_number > self.__ignored_big_number:
                continue
            result += int_number
        return result
