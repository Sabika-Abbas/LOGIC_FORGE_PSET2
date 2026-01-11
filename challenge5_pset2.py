def min_cancelled_meetings(meetings):
    if not meetings:
        return 0
    
    meetings.sort(key=lambda x:(x[1]))

    meetings_cancelled=0
    last_end=meetings[0][1]

    for i in range(1,len(meetings)):
        start,end=meetings[i]
        if start<last_end:
            meetings_cancelled+=1
        else:
            last_end=end

    return meetings_cancelled

meetings=[[1,3], [2,4], [3,5], [4,6]]
count=min_cancelled_meetings(meetings)
print("Total meetings cancelled", count)