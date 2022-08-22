class RomanNumerals:

    def to_roman(val):
        number_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbol_list = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        result = ''
        for i in range(len(number_list)):
            result += val // number_list[i] * symbol_list[i]
            val %= number_list[i]
        return result

    def from_roman(roman_num):
        number_list = []
        symbols = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            "L" : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        for i in roman_num:
            number_list.append(symbols[i])
        max_symbol = 0
        result = 0
        for i in range(1, len(number_list)+1):
            if number_list[-i] >= max_symbol:
                max_symbol = number_list[-i]
                result += number_list[-i]
            elif number_list[-i] < max_symbol:
                result -= number_list[-i]
        return result

    def direction(text):
        arabic = [str(i) for i in list(range(10))]
        roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        text = text.upper()
        text_type_arabic = True
        text_type_roman = True
        for i in text:
            if i not in arabic:
                text_type_arabic = False
        for i in text:
            if i not in roman:
                text_type_roman = False
        if text_type_arabic == True and text_type_roman == False:
            text = int(text)
            if text < 4000:
                return RomanNumerals.to_roman(text)
            else:
                return 'Error'
        elif text_type_arabic == False and text_type_roman == True:
            return RomanNumerals.from_roman(text)
        else:
            return 'Error'
