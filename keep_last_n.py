# keep the last N items in memory

from collections import deque

q = deque(maxlen=2)
q.append(1)
q.append(2)
print(q)        # deque([1,2],maxlen=2)
q.append(3)     # deque([2,3],maxlen=2)
q.pop()         # removes element from right
print(q)        # deque([2],maxlen=2)
q.popleft()     # removes element from left
print(q)        # deque([],maxlen=2)
q.append(5)     # add element x from right side
print(q)        # deque([5],maxlen=2)
q.appendleft(0) # add element x from left side
print(q)        # deque([0, 5],maxlen=2)


# below is a sample program to print previous N lines after finding a pattern in file

def search(lines, pattern, history=3):
    prev_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, prev_lines
        prev_lines.append(line)

with open(r'test_data\sample1.txt') as f:
    for line, prev_lines in search(f, 'python', 3):
        for pline in prev_lines:
            print(pline, end='')
        print(line, end='')


    