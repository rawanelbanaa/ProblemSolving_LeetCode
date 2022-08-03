class MyCalendar:

      def __init__(self):
             self.calendar = []
    
      def book(self, start: int, end: int) -> bool:

        def binary_search(start):
            n, r  = 0, len(self.calendar)
            while n < r:
                mid = (n+r)//2
                if self.calendar[mid][0] > start:
                    r = mid
                else:
                    n = mid + 1                    
            return n
        

        index = binary_search(start)
        
        if index < len(self.calendar) and end > self.calendar[index][0]:
            return False
        if index > 0 and start < self.calendar[index-1][1]:
            return False

        self.calendar.insert(index, [start, end])
        return True