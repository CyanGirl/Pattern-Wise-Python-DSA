'''
a) Given on-call rotation schedule for multiple people by: their name, start time and end time of the rotation:

Abby 1 10
Ben 5 7
Carla 6 12
David 15, 17

and given t = 9, return a list of names who are on call at time t.
Expected output: [Abby, Carla]

b) Return a rotation table without overlapping periods representing who are on call during that time. Return "Start time", "End time" and list of names:

1 5 Abby
5 6 Abby, Ben
6 7 Abby, Ben, Carla
7 10 Abby, Carla
10 12 Carla
15 17 David
'''


# Solution to Part A
def findOnCalls(time,rotation):
    oncalls = []

    for name,start,end in rotation:
        if start<=time<=end:
            oncalls.append(name)

    return oncalls


# Solution to Part B
def findRotationTable(rotation):
    schedule = []
    for name, start, end in rotation:
        schedule.append((start,name,"start"))
        schedule.append((end,name,"end"))
    schedule.sort()

    prev_time = None
    oncalls=set()

    table = []

    for time,name,ttype in schedule:

        # we dont want to add when its first iteration or when the time is same as previous_time. 
        # This will mean some person is starting at the same time as previous, or ending at the same time as previous. 
        # So we dont want to append anything new to the table. we only add when the current time is greater than the last time
        if prev_time is not None and time > prev_time: 
            table.append((prev_time,time,",".join(list(oncalls))))
        if ttype=="start":
            oncalls.add(name)
        else:
            oncalls.remove(name)
        prev_time=time
    
    return table


        


# main
def main():
    rotation = [
    ("Abby", 1, 10),
    ("Ben", 5, 7),
    ("Carla", 6, 12),
    ("David", 15, 17)
]
    print(findOnCalls(9,rotation))
    print(findRotationTable(rotation))


    
main()


