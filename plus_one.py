class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum_numbers = 0
        for i in range(len(digits)):
            sum_numbers = sum_numbers + digits[-i - 1] * (10 ** i)

        sum_numbers += 1
        print(sum_numbers)

        output_list = []
        for i in range(len(digits)):
            next_digit = sum_numbers % 10
            sum_numbers = sum_numbers // 10
            output_list.append(next_digit)

        if sum_numbers == 1:
            output_list.append(1)

        output_list.reverse()

        return output_list
