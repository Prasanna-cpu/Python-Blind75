def eraseOverlapIntervals(intervals):
    if not intervals:
        return 0

    # Sort intervals by their end time
    intervals.sort(key=lambda x: x[1])

    # Initialize the count of intervals to remove
    remove_count = 0

    # Initialize the end time of the last added interval to the non-overlapping set
    end = intervals[0][1]

    for i in range(1, len(intervals)):
        # If the current interval starts before the end of the last added interval, they overlap
        if intervals[i][0] < end:
            remove_count += 1
        else:
            # Update the end time to the current interval's end time
            end = intervals[i][1]

    return remove_count