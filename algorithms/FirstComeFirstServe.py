from matplotlib import pyplot as plt
import firebase_admin
from firebase_admin import storage, credentials, firestore


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
    # blob.make_public()
    print(blob.public_url)
    # return blob.public_url


def generateOutput(outputProcesses: list, avgWT: int, avgTAT: int) -> None:

    columnLables = [
        'Process ID',
        'Arrival Time',
        'Burst Time',
        'Waiting Time',
        'Completion Time',
        'Turn Around Time',
        'Response Time'
    ]

    values = [[outputProcesses[i]['Process ID'], outputProcesses[i]['Arrival Time'], outputProcesses[i]['Burst Time'], outputProcesses[i]['Waiting Time'],
               outputProcesses[i]['Completion Time'], outputProcesses[i]['Turn Around Time'], outputProcesses[i]['Response Time']]for i in range(0, len(outputProcesses))]

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
    # blob.make_public()
    print(blob.public_url)
    # return blob.public_url


class FCFS:
    def __init__(self, processes: list) -> None:
        self.time = 0
        self.processes = processes
        self.numberOfProcesses = len(processes)

    def simulate(self) -> None:
        ganttChart = []
        for process in self.processes:

            if(process['Arrival Time'] > self.time):

                self.time += (process['Arrival Time'] - self.time)

            if 'Response Time' in process.keys():
                pass
            else:
                process['Response Time'] = (
                    self.time - process['Arrival Time'])

            ganttChart.append(
                {'Process ID': process['Process ID'], 'Start Time': self.time, 'Exit Time': self.time + process['Burst Time']})

            self.time += process['Burst Time']

            process['Completion Time'] = self.time
        
        generateGanttChart(ganttChart)

    def calculateTimes(self) -> int:
        sumTAT = 0
        sumWT = 0

        for process in self.processes:

            process['Turn Around Time'] = process['Completion Time'] - process['Arrival Time']

            process['Waiting Time'] = process['Turn Around Time'] - process['Burst Time']

            sumTAT += process['Turn Around Time']

            sumWT += process['Waiting Time']

        avgWT = (sumWT / self.numberOfProcesses)

        avgTAT = (sumTAT / self.numberOfProcesses)


        generateOutput(self.processes, avgWT, avgTAT)

def printFormattedOutput() -> None:

    print()
    print('PID = Process ID')
    print('ST = Start Time')
    print('ET = Exit Time')

    print()
    print('PID\tST\tET')
    for gantt in output['Gantt Chart']:
        id = str(gantt['Process ID'])
        st = str(gantt['Start Time'])
        et = str(gantt['Exit Time'])
        print(id + '\t' + st + '\t' + et)

    print()
    print('PID = Process ID')
    print('AT = Arrival Time')
    print('BT = Burst Time')
    print('CT = Completion Time')
    print('TAT = Turn Around Time')
    print('WT = Waiting Time')
    print('RT = Response Time')

    print()
    print('PID\tAT\tBT\tCT\tTAT\tWT\tRT')
    for process in output['Processes']:
        pid = str(process['Process ID'])
        at = str(process['Arrival Time'])
        bt = str(process['Burst Time'])
        ct = str(process['Completion Time'])
        tat = str(process['Turn Around Time'])
        wt = str(process['Waiting Time'])
        rt = str(process['Response Time'])
        print(pid + '\t' + at + '\t' + bt + '\t' +
              ct + '\t' + tat + '\t' + wt + '\t' + rt)

    print()
    print('Average Waiting Time = ' + str(output['Average Waiting Time']))


if __name__ == '__main__':

    cred = credentials.Certificate(
        'algorithms/jaynakum-experiments-88cc723f2db9.json')
    default_app = firebase_admin.initialize_app(
        cred, {'storageBucket': 'jaynakum-experiments.appspot.com'})

    db = firestore.client()
    doc_ref = db.collection(u'CPU Scheduling').document(
        u'First Come First Serve')
    result_doc_ref = db.collection(u'CPU Scheduling').document(u'Results')

    try:
        doc = doc_ref.get()
        while(True):
            print('check?')
            if(doc != doc_ref.get()):
                print('New Document')
                doc = doc_ref.get()
                input = doc.to_dict()
                processes = input['Processes']
                processes.sort(key=lambda process: process['Arrival Time'])

                print(processes)

                output = {
                    'Processes': processes,
                    'Gantt Chart': [],
                    'Average Waiting Time': 0,
                    'Average Turn Around Time': 0
                }

                fcfs = FCFS(output['Processes'])
                fcfs.simulate()
                fcfs.calculateTimes()
                printFormattedOutput()
            print('No Changes')
            doc = doc_ref.get()
    except Exception:
        print('Something went wrong :(')
