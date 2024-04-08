class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # 0 = 方形, 1 = 圓形
        # i = 0 是 stack.top()
        
        # 直到沒有任何 student queue 的人想要把上面的拿起來吃
        # [1, 1, 0, 0] and [0, 1, 0, 1]
        # => 1 不要, 排回 queue [1, 0, 0, 1]
        # => 1 不要, 排回 queue [0, 0, 1, 1]
        # => 0 要, 拿走 stack 的 0 sandwich 變 [1, 0, 1], student queue 成 [0, 1, 1]
        # ...

        try_count = 0
        students, sandwiches = deque(students), deque(sandwiches)
        
        while students and sandwiches:
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
                try_count = 0
            else: # 繼續排
                students.append(students.popleft()) 
                try_count += 1
            
            # 檢查我們是否已經遍歷完所有學生而沒有人可以吃飯
            if try_count == len(students):
                break

        return len(students)
