def getDetails() -> None:
    process = {}  # each process is treated as dictionary
    numberOfProcesses = int(input('Enter number of processes: '))
    for i in range(0, numberOfProcesses):
        # reading data
        arrivalTime = int(input('Enter arrival time for process[%d] : ' %(i + 1)))
        burstTime = int(input('Enter burst time for process[%d] : ' %(i + 1)))
                
        processes.append({'Process ID': i, 'Arrival Time': arrivalTime, 'Burst Time': burstTime}) # putting data in the processes array
        output.append({'Process ID': i, 'Arrival Time': arrivalTime, 'Burst Time': burstTime,'Completion Time':0, 'Turn Around Time': 0, 'Waiting Time': 0})

# sort the processes by its arival time
def sortByArrivalTime() -> None:
    def sortBy(process):
        return process['Arrival Time']
    processes.sort(key=sortBy)

# Round Robin
class RoundRobin:
    def __init__(self, processes) -> None:
        self.processes = processes

    def ganttChart(self) -> list: # This method returns a ganttChart
        isDone = False
        ganttChart = [] # the main list which will contain the ganttChart 
        startTime = 0 # initial startTime
        i = 0 # starting with process[0]

        while not isDone:
            if(i >= len(self.processes)):
                i = 0

            if(self.processes[(len(self.processes)-1)]['Burst Time'] == 0): # if the remaining burst time of last process is zero
                isDone = True # then gantt chart is formed
            
            # remainingBurstTime is the time left to execute
            remainingBurstTime = self.processes[i]['Burst Time'] # initially the burst time will be the remainingBurstTime
            
            if(remainingBurstTime == 0): # if the remaining time is zero
                i += 1 # then we skip to the next process
                continue
            
            ganttStart = startTime # noting the start time

            # performing the execution of process
            for execute in range(0, QUANTUM): # executing the process for given Time-QUANTUM
                remainingBurstTime -= 1
                startTime = startTime + 1
                if(remainingBurstTime == 0): # if remainingBurstTime is 0
                    break # then the process is fully executed
            
            ganttStop = startTime # noting the stop time
            
            # add the 'Process ID', 'Start Time' and 'Stop Time' in ganttChart
            ganttChart.append({'Process ID': self.processes[i]['Process ID'], 'Start Time': ganttStart, 'Stop Time': ganttStop})
            # updating the process 'Burst Time' to remainingBurstTime
            self.processes[i]['Burst Time'] = remainingBurstTime

            i += 1 # next process
        return ganttChart # returning the final ganttChart list
        
    # this method calculates the completionTime of each process
    def calculateCompletionTime(self, ganttChart) -> None:
        for i in range(0, len(output)):
            for j in range(0, len(ganttChart)): # it reads the ganttChart
                if(output[i]['Process ID'] == ganttChart[j]['Process ID']): # and updates the values everytime both the 'Process Id' matches
                    output[i]['Completion Time'] = ganttChart[j]['Stop Time']

    # this method calculates the turnAroundTime of each process
    def calculateTurnAroundTime(self) -> None:
        for i in range(0, len(output)):
            # for each process, Turn Around Time = Completion Time - Arrival Time
            output[i]['Turn Around Time'] = output[i]['Completion Time'] - output[i]['Arrival Time']
    
    # this method calculates the waitingTime of each process
    def calculateWaitingTime(self) -> None:
        for i in range(0, len(output)):
            # for each process, Waiting Time = Turn Around Time - Burst Time
            output[i]['Waiting Time'] = output[i]['Turn Around Time'] - output[i]['Burst Time']
    
    # this method calculates the average of all waitingTimes
    def calculateAverageWaitingTime(self) -> float:
        sum = 0
        for i in range(0, len(output)):
            # calculating the sum
            sum = sum + output[i]['Waiting Time']
        # dividing by total processes
        return (sum / len(output)) # returning the average

# this method formats the gantt chart properly
def printGanttChart(list) -> None:
    ganttChartOutput = []
    processID = ''
    startTime = ''
    stopTime = ''
    for i in range(0, len(list)):
        processID = str(list[i]['Process ID'])
        startTime = str(list[i]['Start Time'])
        stopTime = str(list[i]['Stop Time'])
        ganttChartOutput.append((processID, startTime, stopTime))
    print(ganttChartOutput)

# this method formats the output properly
def printOutput(list) -> None:
    processID = ''
    arrivalTime = ''
    burstTime = ''
    completionTime = ''
    turnAroundTime = ''
    waitingTime = ''

    print('Process ID | Arrival Time | Burst Time | Completion Time | Turn Around Time | Waiting Time')
    for i in range(0, len(list)):
        processID = str(list[i]['Process ID'])
        arrivalTime = str(list[i]['Arrival Time'])
        burstTime = str(list[i]['Burst Time'])
        completionTime = str(list[i]['Completion Time'])
        turnAroundTime = str(list[i]['Turn Around Time'])
        waitingTime = str(list[i]['Waiting Time'])
        
        print(processID+'\t\t'+arrivalTime+'\t\t'+burstTime+'\t\t'+completionTime+'\t\t'+turnAroundTime+'\t\t'+waitingTime)

# DRIVER CODE
if __name__ == "__main__":
    QUANTUM = 3  # is the defined time for which any process will be executed
    processes = []  # is the process array in which all processes are stored
    output = []
    getDetails() # reading the details from user
    sortByArrivalTime() # sorting the processes by its arrival time
    
    algorithm = RoundRobin(processes)

    ganttChart = algorithm.ganttChart() # generate ganttChart
    print('\nGantt Chart: ')
    printGanttChart(ganttChart) # print ganttChart

    # Calculate 'Completion Time', 'Turn Around Time' and 'Waiting Time' of each process
    algorithm.calculateCompletionTime(ganttChart)
    algorithm.calculateTurnAroundTime()
    algorithm.calculateWaitingTime()
    
    print('\n\nOutput: ')
    printOutput(output) # print details of each process

    # Calculate the average of waiting times
    averageWaitingTime = algorithm.calculateAverageWaitingTime()
    print('\nAverage Waiting Time: ')
    print(averageWaitingTime) # and print averageWaitingTime