class Solution(object):
    def minMovesToSeat(self, seats, students):
        seats.sort()
        students.sort()
        c = 0
        for i in range(len(seats)):
            c = c+abs(seats[i]-students[i])
        return c
