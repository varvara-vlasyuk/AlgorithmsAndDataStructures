"""
Given N activities with start and end time. We need to select max number of activities
that can be performed by a single person, assuming that a person can only work on a single activity at a time.
"""
activities = [["A1", 0, 6],
              ["A2", 3, 4],
              ["A3", 1, 2],
              ["A4", 5, 8],
              ["A5", 5, 7],
              ["A6", 8, 9]
                ]

sorted_activities = sorted(activities, key=(lambda x: x[2]))
time = 0
perf = []           # last_end_time: list
for act in sorted_activities:
    if act[1] >= time:
        time = act[2]
        perf.append(act[0])

print(perf)
