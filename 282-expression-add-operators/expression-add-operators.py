
class Solution:
    def addOperators(self, num: str, target: int) -> list[str]:
        result = []

        def backtrack(index, expression, value, last):
            if index == len(num):
                if value == target:
                    result.append(expression)
                return

            for i in range(index, len(num)):
                if i > index and num[index] == '0':
                    break

                part = num[index:i + 1]
                current = int(part)

                if index == 0:
                    backtrack(i + 1, part, current, current)
                else:
                    backtrack(
                        i + 1,
                        expression + '+' + part,
                        value + current,
                        current
                    )

                    backtrack(
                        i + 1,
                        expression + '-' + part,
                        value - current,
                        -current
                    )

                    backtrack(
                        i + 1,
                        expression + '*' + part,
                        value - last + last * current,
                        last * current
                    )

        backtrack(0, "", 0, 0)
        return result
