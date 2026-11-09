"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_thai(self, number: int) -> str:
        if number < 0:
            return "number can not less than 0"
        if number > 10_000_000:
            return "number can not exceed 10000000"
        if number == 0:
            return "ศูนย์"
        digits = ["", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]
        places = ["", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน"]
        millions, rest = divmod(number, 1_000_000)
        parts = [self.number_to_thai(millions) + "ล้าน"] if millions else []
        for power in range(5, -1, -1):
            digit = rest // (10 ** power) % 10
            if not digit:
                continue
            word = digits[digit]
            if power == 1 and digit <= 2:
                word = "" if digit == 1 else "ยี่"
            elif power == 0 and digit == 1 and number > 1:
                word = "เอ็ด"
            parts.append(word + places[power])
        return "".join(parts)
