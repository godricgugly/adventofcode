#puzzle 1:

with open ("puzzle1") as file:
    puzzle=[int(line.strip()) for line in file]

counter = 0
for n in range(len(puzzle)-1) :
    if puzzle[n]<puzzle[n+1] :
        counter = counter + 1
print("Solution to part 1:", counter)

window1 = 0
window2 = 0
counters = 0
for n in range(len(puzzle)-3) :
    window1 = puzzle[n] + puzzle[n+1] + puzzle[n+2]
    window2 = puzzle[n+1] + puzzle[n+2] + puzzle[n+3]
    if window1 < window2:
        counters = counters +1
print("Solution to part 2:", counters)

#After solving it, I kept looking for different / better ways to solve it.

#Part 1:

increments = [b-a for a,b in zip(puzzle,puzzle[1:]) if b>a]
print("Part 1, alternative method", len(increments))

#Part 2:

from collections import deque

def sliding_window_sum(theList, size):
  out     = []
  the_sum = 0
  q       = deque()
  for i in theList:
    if len(q)==size:
      the_sum -= q[0]
      q.popleft()
    q.append(i)
    the_sum += i
    if len(q)==size:
      out.append(the_sum)
  return out

windowSum = sliding_window_sum(puzzle, 3)

result = [b-a for a,b in zip(windowSum,windowSum[1:]) if b>a]
print ("Part 2, alternative method", len(result))

