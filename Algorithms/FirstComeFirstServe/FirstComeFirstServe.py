# CPU Scheduling Algorithms: First Come First Serve

import json

def readFromJson() -> list:
    # TODO: change this path for application
    with open('./json/testcase.json', 'r') as inputFile:
        input = inputFile.read()

    processes = json.loads(input)

    # print(processes)
    return processes['Processes']

class FCFS:

    def __init__(self, processes: list) -> None:
        self.processes = processes
        self.time = 0 # time value

    def _executeProcess(self, process: dict) -> dict:
        remainingBurstTime = process['Burst Time']
        
        startTime = self.time
        
        # add the Response Time
        if 'Response Time' in process.keys():
            pass
        else:
            process['Response Time'] = startTime - process['Arrival Time']

        # simulate the execution
        while(remainingBurstTime > 0):
            remainingBurstTime -= 1
            self.time += 1
        
        endTime = self.time
        
        gantt = {'Process ID': process['Process ID'], 'Start Time': startTime, 'Exit Time': endTime}
        
        # print(gantt)
        return gantt

    def _ganttChart(self) -> list:
        ganttChart = []

        # execute each process and generate ganttChart
        for process in self.processes:
            
            # Check if there is an empty state
            while(process['Arrival Time'] > self.time):
                self.time += 1 # keep CPU empty
            
            gantt = self._executeProcess(process)
            ganttChart.append(gantt)

            # add the completion time
            process['Completion Time'] = gantt['Exit Time']

        # print(ganttChart)
        return ganttChart
    
    def _calculateTimes(self) -> int:
        sum = 0
        
        for process in self.processes:
            # Turn Around Time = Completion Time – Arrival Time || Turn Around Time = Exit time - Arrival time
            process['Turn Around Time'] = process['Completion Time'] - process['Arrival Time']
            # Waiting Time = Turn Around Time – Burst Time
            process['Waiting Time'] = process['Turn Around Time'] - process['Burst Time']
            
            # Sum of Average Waiting Time
            sum += process['Waiting Time']
        
        # Average Waiting Time
        avg = (sum / len(self.processes))
        return avg

    def simulate(self) -> dict:
        output = {}

        ganttChart = self._ganttChart()
        averageWaitingTime = self._calculateTimes()
        
        output['Processes'] = self.processes
        output['Gantt Chart'] = ganttChart
        output['Average Waiting Time'] = averageWaitingTime

        # print(output)
        return output

def writeIntoJson(outputJson) -> None:
    # TODO: change this path for application
    with open("./json/FirstComeFirstServe.json", "w") as outfile:
        outfile.write(outputJson)

# Driver Code
if __name__ == "__main__":
    processes = readFromJson()
    processes.sort(key=lambda process: process['Arrival Time'])
    output = FCFS(processes).simulate()
    writeIntoJson(json.dumps(output))
