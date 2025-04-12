import statistics

class CalculatorService():

    @staticmethod
    def calculate_median(number_list):
        if not number_list:
            return None
        return statistics.median(number_list)

    @staticmethod
    def calculate_average(number_list):
        if not number_list:
            return None
        return sum(number_list) / len(number_list)
