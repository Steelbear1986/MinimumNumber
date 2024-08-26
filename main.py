class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        students=sorted(students)
        seats=sorted(seats)
        answer=[ abs(x-y)  for x,y in zip(students,seats)]
        return sum(answer)