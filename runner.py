import sys
import puzzle_9.part_2 as puzzle
import time

start = time.time()
ans = puzzle.solution(sys.argv[1])
print(ans)
end = time.time()
print("Duration: " + str(end - start))

