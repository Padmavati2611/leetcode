class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:

        people.sort(key=lambda x: (-x[0], x[1]))

        result = []

        for person in people:
            result.insert(person[1], person)

        return result