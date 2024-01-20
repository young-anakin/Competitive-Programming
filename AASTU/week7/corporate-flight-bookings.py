class Solution:
    def corpFlightBookings(self, bookings, n):
        zero = [0 for ind in range(n)]
        print(zero)
        for book in bookings:
            ind = book[0] - 1
            zero[ind] += book[2]
            if book[1] + 1 <= n:
                zero[book[1]] -= book[2]
        prefix = [0]
        print(zero)
        for ind in range(n):
            prefix.append(prefix[-1] + zero[ind])
        prefix.pop(0)
        return prefix