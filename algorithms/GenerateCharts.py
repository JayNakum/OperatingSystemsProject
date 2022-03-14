from matplotlib import pyplot as plt
from firebase_admin import storage    


def generateGanttChart(ganttChart: list) -> str:

    fig, gnt = plt.subplots()

    gnt.set_ylim(0, 1)

    gnt.set_xlim(0, ganttChart[(len(ganttChart) - 1)]['Exit Time'] + 1)

    gnt.set_xlabel('Time')
    gnt.set_ylabel('Process ID')

    gnt.set_yticks([10, 20])

    gnt.set_yticklabels(['', ''])

    isOrange = True
    for gantt in ganttChart:
        isOrange = not isOrange
        if(isOrange):
            gnt.broken_barh([(gantt['Start Time'], (gantt['Exit Time'] -
                            gantt['Start Time']))], (8, 4), facecolors=('tab:green'))
        else:
            gnt.broken_barh(
                [(gantt['Start Time'], (gantt['Exit Time'] - gantt['Start Time']))], (8, 4))
        gnt.annotate(gantt['Process ID'], (gantt['Start Time'] + 0.2, 9.7))

    plt.savefig('./algorithms/output/ganttchart.png')
    fileName = 'algorithms/output/ganttchart.png'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)
    blob.make_public()
    print(blob.public_url)
    return blob.public_url


def generateOutput(outputProcesses: list, avgWT: int, avgTAT: int) -> str:

    columnLables = [
        'Process ID',
        'Arrival Time',
        'Burst Time',
        'Waiting Time',
        'Completion Time',
        'Turn Around Time',
        'Response Time'
    ]

    values = [list(process.values())for process in outputProcesses]

    plt.rcParams["figure.figsize"] = [11.0, 3.0]
    plt.rcParams["figure.autolayout"] = True

    fig, ax = plt.subplots()
    ax.set_axis_off()
    table = ax.table(
        cellText=values,
        colLabels=columnLables,
        cellLoc='center',
        loc='center')

    table.scale(1.5, 1.5)

    ax.set_title('Average Waiting Time = ' + str(avgWT) +
                 '\nAverage Turn Around Time = ' + str(avgTAT))

    plt.savefig('./algorithms/output/outputTable.png')
    fileName = 'algorithms/output/outputTable.png'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)
    blob.make_public()
    print(blob.public_url)
    return blob.public_url
