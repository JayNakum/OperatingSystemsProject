import GenerateCharts as gc


class FCFS:
    def __init__(self, processes: list) -> None:
        self.time = 0
        self.processes = processes
        self.numberOfProcesses = len(processes)

    def simulate(self) -> None:
        for process in self.processes:

            if(process['Arrival Time'] > self.time):

                self.time += (process['Arrival Time'] - self.time)

            if 'Response Time' in process.keys():
                pass
            else:
                process['Response Time'] = (
                    self.time - process['Arrival Time'])

            output['Gantt Chart'].append(
                {'Process ID': process['Process ID'], 'Start Time': self.time, 'Exit Time': self.time + process['Burst Time']})

            self.time += process['Burst Time']

            process['Completion Time'] = self.time

    def _calculateTimes(self) -> int:
        sumTAT = 0
        sumWT = 0

        for process in self.processes:

            process['Turn Around Time'] = process['Completion Time'] - \
                process['Arrival Time']

            process['Waiting Time'] = process['Turn Around Time'] - \
                process['Burst Time']

            sumTAT += process['Turn Around Time']

            sumWT += process['Waiting Time']

        output['Average Waiting Time'] = (sumWT / self.numberOfProcesses)

        output['Average Turn Around Time'] = (sumTAT / self.numberOfProcesses)


if __name__ == '__main__':

    import firebase_admin
    from firebase_admin import credentials, firestore
    from google.cloud import exceptions

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
            if(doc != doc_ref.get()):
                print('New Document')
                doc = doc_ref.get()
                input = doc.to_dict()
                processes = input['Processes']
                processes.sort(key=lambda process: process['Arrival Time'])

                output = {
                    'Processes': processes,
                    'Gantt Chart': [],
                    'Average Waiting Time': 0,
                    'Average Turn Around Time': 0
                }

                fcfs = FCFS(output['Processes'])
                fcfs.simulate()
                fcfs._calculateTimes()

                chartURL = gc.generateGanttChart(
                    ganttChart=output['Gantt Chart'])
                outputURL = gc.generateOutput(
                    outputProcesses=output['Processes'], avgWT=output['Average Waiting Time'], avgTAT=output['Average Turn Around Time'])
                
                result_doc_ref.set({'Gantt Chart': chartURL, 'Output Table': outputURL})
            print('No Changes')
            doc = doc_ref.get()
    except exceptions.NotFound:
        print('No processes found')
