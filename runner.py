import sys
import puzzle_12.part_1 as puzzle
import time

start = time.time()
ans = puzzle.solution(sys.argv[1])
print(ans)
end = time.time()
print("Duration: " + str(end - start))

