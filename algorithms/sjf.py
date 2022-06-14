# -*- coding: utf-8 -*-
"""SJF.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aG8_l_5WTQMdoU7deBuwqKUUjuXhRht-

# Shortest Job First

## Setting up firebase
"""

# imports
import firebase_admin
from firebase_admin import credentials, firestore

# get the credential certificate from json file
cred = credentials.Certificate('jaynakum-experiments-88cc723f2db9.json')
# using the credentials initialize the firebase app
default_app = firebase_admin.initialize_app(cred, {'storageBucket': 'jaynakum-experiments.appspot.com'})
# initialize the database
db = firestore.client()

# initialize the main document reference
doc_ref = db.collection(u'CPU Scheduling')

"""## Generate gantt chart and output table"""

# imports
from matplotlib import pyplot as plt
from firebase_admin import storage

# method to generate gantt chart
def generateGanttChart(ganttChart: list) -> None:
  # create a figure and a set of subplots
  fig, gnt = plt.subplots()

  # set x-axis limit from 0 to the last entry of gantt chart
  gnt.set_xlim(0, ganttChart[(len(ganttChart) - 1)]['Exit Time'] + 1)
  # set y-axis limit to 1 because the chart is one line only
  gnt.set_ylim(0, 1)

  # set labels for both the axis
  gnt.set_xlabel('Time')
  gnt.set_ylabel('Process ID')

  # set y ticks and set labels = '' because there is no need to display it
  gnt.set_yticks([10, 20])
  gnt.set_yticklabels(['', ''])

  # the chart alternates between green and blue color
  # _isGreen flag is used to determine the color of broken_barh [broken bar horizontal]
  _isGreen = True
  for gantt in ganttChart:
    # _isGreen alternates between true and false
    _isGreen = not _isGreen
    # if true draw with green color else draw with blue
    if(_isGreen):
      # draw the broken_barh(start_time, duration_time)
      gnt.broken_barh([(gantt['Start Time'], (gantt['Exit Time'] - gantt['Start Time']))], (8, 4), facecolors=('tab:green'))
    else:
      # draw the broken_barh(start_time, duration_time)
      gnt.broken_barh([(gantt['Start Time'], (gantt['Exit Time'] - gantt['Start Time']))], (8, 4))
    # annotate the chart with the process' ID
    gnt.annotate(gantt['Process ID'], (gantt['Start Time'] + 0.2, 9.7))

  # save the output file
  plt.savefig('output/ganttChart.png')
  fileName = 'output/ganttChart.png'
  # print('Gantt Chart generated at: ' + fileName)

  # initialize the storage folder / bucket
  bucket = storage.bucket()
  # initialize the image blob
  blob = bucket.blob(fileName)
  # upload the image blob to firebase
  blob.upload_from_filename(fileName)

# method to generate output table
def generateOutput(outputProcesses: list, avgWT: int, avgTAT: int) -> None:
  # initializing a list of column lables
  columnLables = [
    'Process ID',
    'Arrival Time',
    'Burst Time',
    'Waiting Time',
    'Completion Time',
    'Turn Around Time',
    'Response Time'
  ]

  # making a list of each row(as list) from output 
  values = [[outputProcesses[i]['Process ID'], outputProcesses[i]['Arrival Time'], outputProcesses[i]['Burst Time'], outputProcesses[i]['Waiting Time'], outputProcesses[i]['Completion Time'], outputProcesses[i]['Turn Around Time'], outputProcesses[i]['Response Time']]for i in range(0, len(outputProcesses))]

  # set size and layout of output figure
  plt.rcParams["figure.figsize"] = [11.0, 3.0]
  plt.rcParams["figure.autolayout"] = True
  # create a figure and a set of subplots
  fig, table = plt.subplots()
  
  # turn off x and y axis
  table.set_axis_off()
  # enter the data into the table
  # cellText = values and colLabels = columnLabels with location center
  outputTable = table.table(cellText=values, colLabels=columnLables, cellLoc='center', loc='center')
  # scale the output image
  outputTable.scale(1.5, 1.5)
  # print 'Average Waiting Time' and 'Average Turn Around Time' in the image
  table.set_title('Average Waiting Time = ' + str(avgWT) + '\nAverage Turn Around Time = ' + str(avgTAT))

  # save the output file
  plt.savefig('output/outputTable.png')
  fileName = 'output/outputTable.png'
  # print('Output Table generated at: ' + fileName)

  # initialize the storage folder / bucket
  bucket = storage.bucket()
  # initialize the image blob
  blob = bucket.blob(fileName)
  # upload the image blob to firebase
  blob.upload_from_filename(fileName)

"""## Shortest Job First"""

#Function to derive average waiting time
#Time Complexity: O(n)
def avgWaitingTime(n, process) -> float:
  total_waiting_time=0
  for i in range (0, n):
    total_waiting_time=total_waiting_time + process[i]['Waiting Time']
  
  print("Average waiting time is ", (total_waiting_time/n))
  return (total_waiting_time/n)

#Function to derive average turn around time
#Time Complexity: O(n)
def avgTurnAroundTime(n, process) -> float:
  total_turnaround_time=0
  for i in range (0, n):
    total_turnaround_time=total_turnaround_time + process[i]['Turn Around Time']
  
  print("Average turn around time is ", (total_turnaround_time/n))
  return (total_turnaround_time/n)

#Function to sort all input process values according to arrival time
#Algorithm used: Bubble Sort 
#Time Complexity: O(n^2)
  #reason: 
    # - need to sort all dictionary values in the list according to one specific field (arrival time)
    # - other sorting algorithms (quick sort, merge sort) use recursion, divide and conquer methods which are difficult to implement in such cases
    # - time complexity for SJF algorithm comes down to O(n^2) so bubble sort will not increase the worst case time complexity
def arrangeArrival(n, process):
    for i in range(0, n):
        for j in range(i, n - i - 1):
            if process[j]['Arrival Time'] > process[j + 1]['Arrival Time']:
                process[j]['Arrival Time'], process[j + 1]['Arrival Time'] = process[j + 1]['Arrival Time'], process[j][
                    'Arrival Time']
                process[j]['Process ID'], process[j + 1]['Process ID'] = process[j + 1]['Process ID'], process[j][
                    'Process ID']
                process[j]['Burst Time'], process[j + 1]['Burst Time'] = process[j + 1]['Burst Time'], process[j][
                    'Burst Time']

#Algorithm to find Completion time, Turn around time and waiting time for each process
#Time Complexity : O(n^2)

def CompletionTime(n, process):
    value = 0
    process[0]['Completion Time'] = process[0]['Arrival Time'] + process[0]['Burst Time']
    process[0]['Turn Around Time'] = process[0]['Completion Time'] - process[0]['Arrival Time']
    process[0]['Waiting Time'] = process[0]['Turn Around Time'] - process[0]['Burst Time']
    for i in range(1, n):
        temp = process[i - 1]['Completion Time']
        mini = process[i]['Burst Time']
        for j in range(i, n):
            if temp >= process[j]['Arrival Time'] and mini >= process[j]['Burst Time']:
                mini = process[j]['Burst Time']
                value = j

        process[value]['Completion Time'] = temp + process[value]['Burst Time']
        process[value]['Turn Around Time'] = process[value]['Completion Time'] - process[value]['Arrival Time']
        process[value]['Waiting Time'] = process[value]['Turn Around Time'] - process[value]['Burst Time']


        process[value]['Process ID'], process[i]['Process ID'] = process[i]['Process ID'], process[value]['Process ID']
        process[value]['Burst Time'], process[i]['Burst Time'] = process[i]['Burst Time'], process[value]['Burst Time']
        process[value]['Arrival Time'], process[i]['Arrival Time'] = process[i]['Arrival Time'], process[value]['Arrival Time']
        process[value]['Waiting Time'], process[i]['Waiting Time'] = process[i]['Waiting Time'], process[value]['Waiting Time']
        process[value]['Turn Around Time'], process[i]['Turn Around Time'] = process[i]['Turn Around Time'], process[value]['Turn Around Time']
        process[value]['Completion Time'], process[i]['Completion Time'] = process[i]['Completion Time'], process[value][
        'Completion Time']

        


#Function to display all values in output
#Time Complexity: O(n)
def display(process):
    
    print(
        'Process\t Arrival Time\t Burst Time\t Waiting Time\t Turn Around Time\t completion Time'
    )
    for i in range(len(process)):
        print('{}\t {}\t\t {}\t\t {}\t\t {}\t\t\t {}'.format(process[i]['Process ID'],
                                                             process[i]['Arrival Time'],
                                                             process[i]['Burst Time'],
                                                             process[i]['Waiting Time'],
                                                             process[i]['Turn Around Time'],
                                                             process[i]['Completion Time']))

def main(inputProcesses):
  ganttChart = []
  for process in inputProcesses:
    process['Completion Time'] = 0
    process['Turn Around Time'] = 0
    process['Waiting Time'] = 0
  # simulation
  arrangeArrival(len(inputProcesses), inputProcesses)
  CompletionTime(len(inputProcesses), inputProcesses)
  display(inputProcesses)

  ganttChart.append({'Process ID': inputProcesses[0]['Process ID'], 'Start Time': inputProcesses[0]['Arrival Time'], 'Exit Time': inputProcesses[0]['Completion Time']})
  for i in range(1, len(inputProcesses)):
      ganttChart.append({'Process ID': inputProcesses[i]['Process ID'], 'Start Time': inputProcesses[i-1]['Completion Time'], 'Exit Time': inputProcesses[i-1]['Completion Time'] + inputProcesses[i]['Completion Time']})
  for process in inputProcesses:
      process['Response Time'] = process['Waiting Time']

  generateGanttChart(ganttChart)
  generateOutput(outputProcesses = inputProcesses, avgWT = avgWaitingTime(len(inputProcesses), inputProcesses), avgTAT = avgTurnAroundTime(len(inputProcesses), inputProcesses))

"""## Get input from firebase"""

# imports
import threading
import time

# Create an Event for notifying main thread.
callback_done = threading.Event()

# Create a callback on_snapshot function to capture changes
def on_snapshot(doc_snapshot, changes, read_time):
  for change in changes:
  # Check for a change in document
    if change.type.name == 'MODIFIED':
    # print(u'Change: {}'.format(change.document.id))
    # iterate through each document snapshot
      for doc in doc_snapshot:
        print(f'Received new document snapshot: {doc.id}')
        # initialize the input processes
        input = doc.to_dict()
        inputProcesses = input['Processes']
        print(inputProcesses)
        # dict containing the processes, gantt chart, average waiting time and average turn around time
        
        main(inputProcesses)

    # return the control to document watch
    callback_done.set()

# Watch the document
doc_watch = doc_ref.on_snapshot(on_snapshot)

# Keep the app running
while True:
    time.sleep(1)
    # print('watching')