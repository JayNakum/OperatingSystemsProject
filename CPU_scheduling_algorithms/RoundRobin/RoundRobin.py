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


class RoundRobin:
    def __init__(self, processes) -> None:
        self.processes = processes

    def ganttChart(self) -> list:
        isDone = False
        ganttChart = []
        startTime = 0
        i = 0
        while not isDone:
            if(i >= len(self.processes)):
                i = 0

            if(self.processes[(len(self.processes)-1)]['Burst Time'] == 0):
                isDone = True
            
            remainingBurstTime = self.processes[i]['Burst Time']
            
            if(remainingBurstTime == 0):
                i += 1
                continue
            
            ganttStart = startTime

            for execute in range(0, QUANTUM):
                remainingBurstTime -= 1
                startTime = startTime + 1
                if(remainingBurstTime == 0):
                    break
            
            ganttStop = startTime
            
            ganttChart.append({'Process ID': self.processes[i]['Process ID'], 'Start Time': ganttStart, 'Stop Time': ganttStop})
            self.processes[i]['Burst Time'] = remainingBurstTime

            i += 1
        return ganttChart
    
    def calculateCompletionTime(self, ganttChart) -> None:
        for i in range(0, len(output)):
            for j in range(0, len(ganttChart)):
                if(output[i]['Process ID'] == ganttChart[j]['Process ID']):
                    output[i]['Completion Time'] = ganttChart[j]['Stop Time']

    def calculateTurnAroundTime(self) -> None:
        for i in range(0, len(output)):
            output[i]['Turn Around Time'] = output[i]['Completion Time'] - output[i]['Arrival Time']
    
    def calculateWaitingTime(self) -> None:
        for i in range(0, len(output)):
            output[i]['Waiting Time'] = output[i]['Turn Around Time'] - output[i]['Burst Time']
    
    def calculateAverageWaitingTime(self) -> float:
        sum = 0
        for i in range(0, len(output)):
            sum = sum + output[i]['Waiting Time']
        return (sum / len(output))

def printGanttChart(list) -> None:
    ganttChartOutput = []
    processID = ''
    startTime = ''
    stopTime = ''
    for i in range(0, len(list)):
        processID = str(list[i]['Process ID'])
        startTime = str(list[i]['Start Time'])
        stopTime = str(list[i]['Stop Time'])
        # print('['+processID+', '+startTime+', '+stopTime+']')
        ganttChartOutput.append((processID, startTime, stopTime))
    print(ganttChartOutput)

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
    getDetails()
    sortByArrivalTime()
    
    algorithm = RoundRobin(processes)

    ganttChart = algorithm.ganttChart()
    print('\nGantt Chart: ')
    printGanttChart(ganttChart)
    algorithm.calculateCompletionTime(ganttChart)
    algorithm.calculateTurnAroundTime()
    algorithm.calculateWaitingTime()
    print('\n\nOutput: ')
    averageWaitingTime = algorithm.calculateAverageWaitingTime()
    printOutput(output)
    print('\nAverage Waiting Time: ')
    print(averageWaitingTime)