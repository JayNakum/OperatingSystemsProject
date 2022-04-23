# add the values to gantt chart
def generateGanttChart(rawGanttChart: list) -> list:
    gtTime = 0
    ganttChart = []
    gantt = {'Process ID': rawGanttChart[0], 'Start Time':gtTime, 'Exit Time': gtTime + 1} # where Start time  = gtTime and Exit time  = gtTime + 1
    ganttChart.append(gantt) 
    gt = 0
    gtTime += 1
    
    for g in range(1, len(rawGanttChart)):
        if rawGanttChart[g] == ganttChart[gt]['Process ID']:
            ganttChart[gt]['Exit Time'] += 1
        else:
            ganttChart.append({'Process ID': rawGanttChart[g], 'Start Time': gtTime, 'Exit Time': gtTime + 1})
            gt += 1
        gtTime += 1
    
    return ganttChart

# method to calculate TAT, WT and average of TAT and WT
def waitingTime(process, wt):
    n = len(process)
    rt = [0] * n
    rawGanttChart = []

    complete = 0
    short = 0
    current_time = 0
    min_time = 999999999
    flag = False
    # Process until all processes gets
    # completed
    while (complete != n):
          # Find process with minimum remaining  time among the processes that arrives till the current time`
        for i in range(n):
            if process[i]['Arrival Time'] <= current_time and process[i]['Burst Time'] < min_time:
                min_time = process[i]['Burst Time']
                short = i
               

        rawGanttChart.append(process[short]['Process ID'])
        
        min_time = process[short]['Burst Time']


        # Update minimum
        if (min_time == 0):
            min_time = 999999999
            
        complete += 1
        current_time=current_time + min_time
        completion_time = current_time 

        # calculating Waiting time
        wt[short] = completion_time - process[short]['Arrival Time'] - process[short]['Burst Time']
        # wt = tat-bt or  (ct-at)-bt

        if wt[short] < 0:
              wt[short] = 0

    # completion time For Each Process
    print(rawGanttChart)
    ganttChart = generateGanttChart(rawGanttChart)
    for gantt in ganttChart:
        for p in process:
            if p['Process ID'] == gantt['Process ID']:
                p['Completion Time'] = gantt['Exit Time']
            # # note the 'Response Time' of each process
            # if 'Response Time' in process.keys():
            #     pass
            # else:
            #     process['Response Time'] = ( - process['Arrival Time'])
    #             print(gantt['Exit Time'])
    # print(process)
    
    # note the 'Response Time' of each process
    
# Function to calculate turn around time
def turnAroundtime(process, wt, tat):
# Calculating turnaround time
    for i in range(len(process)):
        tat[i] = process[i]['Burst Time'] + wt[i]

# Function to calculate average waiting and turn-around times.
def avgTime(process):
    n = len(process)
    wt = [0] * n
    tat = [0] * n
    total_wt = 0
    total_tat = 0

    waitingTime(process, wt) # Function to find waiting time of all processes
    turnAroundtime(process, wt, tat)# Function to find turn around time for all processes

    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]

    avg_wt = total_wt / n
    avg_tat = total_tat / n

    display(process, wt, tat, avg_wt, avg_tat)

# Time Complexity of Algorithm is O(n^2)
def display(process, wt, tat, avg_wt, avg_tat):
    print(
        'Process\t Arrival Time\t Burst Time\t Waiting Time\t Turn Around Time\t completion Time'
    )
#  Display processes along with all details in table
    for i in range(len(process)):
        print('{}\t {}\t\t {}\t\t {}\t\t {}\t\t\t'.format(process[i]['Process ID'],
                                                    process[i]['Arrival Time'],
                                                    process[i]['Burst Time'],
                                                    wt[i], tat[i]))

    print('\nAverage Waiting Time: ', avg_wt)
    print('Average Turn Around: ', avg_tat)
    output = []
#  Display processes along with all details in dict
    for i in range(len(process)):
        output.append({
            'Process ID': process[i]['Process ID'],
            'Arrival Time': process[i]['Arrival Time'],
            'Burst Time': process[i]['Burst Time'],
            # 'Completion Time': process[i]['Completion Time'],
            'Turn Around Time': tat[i],
            'Waiting Time': wt[i]
        })
    output.sort(key=lambda process: process['Arrival Time'])

    print('\n', output)



process = [{
    'Process ID': 1,
    'Arrival Time': 0,
    'Burst Time': 8
}, {
    'Process ID': 2,
    'Arrival Time': 1,
    'Burst Time': 4
}, {
    'Process ID': 3,
    'Arrival Time': 2,
    'Burst Time': 2
}, {
    'Process ID': 4,
    'Arrival Time': 3,
    'Burst Time': 1
}, {
    'Process ID': 5,
    'Arrival Time': 4,
    'Burst Time': 3
}, {
    'Process ID': 6,
    'Arrival Time': 5,
    'Burst Time': 2
}]

avgTime(process)