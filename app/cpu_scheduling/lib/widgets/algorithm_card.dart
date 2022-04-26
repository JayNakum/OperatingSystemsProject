import 'package:flutter/material.dart';

class AlgorithmCard extends StatefulWidget {
  final String algorithmName;
  const AlgorithmCard({
    required this.algorithmName,
    Key? key,
  }) : super(key: key);

  @override
  _AlgorithmCardState createState() => _AlgorithmCardState();
}

class _AlgorithmCardState extends State<AlgorithmCard> {
  bool _showImplementation = false;
  @override
  Widget build(BuildContext context) {
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(8.0),
        child: Column(
          children: <Widget>[
            ListTile(
              onTap: () {
                setState(() {
                  _showImplementation = !_showImplementation;
                });
              },
              title: const Text('Algorithm'),
              trailing: const Icon(Icons.arrow_drop_down_rounded),
            ),
            if (widget.algorithmName == 'First Come First Serve' &&
                _showImplementation)
              const Text(
                  '\nStep 1 : Input the number of processes required to be scheduled using FCFS, burst time for each process and its arrival time.\n'
                  '\nStep 2 : Using enhanced bubble sort technique, sort the all given processes in ascending order according to arrival time in a ready queue.\n'
                  '\nStep 3 : Calculate the Finish Time, Turn Around Time and Waiting Time for each process which in turn help to calculate Average Waiting Time and Average Turn Around Time required by CPU to schedule given set of process using FCFS.\n'
                  '\nStep 4 : Process with less arrival time comes first and gets scheduled first by the CPU.\n'
                  '\nStep 5 : Calculate the Average Waiting Time and Average Turn Around Time.\n'),
            if (widget.algorithmName == 'Shortest Job First' &&
                _showImplementation)
              const Text(
                '\nStep 1: Sort all the processes according to their arrival time.\n'
                '\nStep 2: Select the process with minimum arrival time as well as minimum burst time.\n'
                '\nStep 3: After completion of the process, select from the ready queue the process which has the minimum burst time.\n'
                '\nStep 4: Repeat above processes untill all processes have finished their execution.\n',
              ),
            if (widget.algorithmName == 'Shortest Remaining Time Next' &&
                _showImplementation)
              const Text(
                '\nStep 1: Traverse until all process gets completely executed.\n'
                '\nStep 1.1: Find process with minimum remaining time at every single time lap.\n'
                '\nStep 1.2: Reduce its time by 1.\n'
                '\nStep 1.3: Check if its remaining time becomes 0 \n'
                '\nStep 1.4: Increment the counter of process completion.\n'
                '\nStep 1.5: Completion time of current process = current_time +1;\n'
                '\nStep 1.6: Calculate waiting time for each completed process.\n'
                '\twt[i]= Completion time - arrival_time-burst_time\n'
                '\nStep 1.7: Increment time lap by one.\n'
                '\nStep 2: Find turnaround time (waiting_time+burst_time).\n',
              ),
            if (widget.algorithmName == 'Round Robin' && _showImplementation)
              const Text(
                '\nStep 1: Create an array rem_bt[] to keep track of remaining burst time of processes. This array is initially a copy of bt[] (burst times array)\n'
                '\nStep 2: Create another array wt[] to store waiting times of processes. Initialize this array as 0.\n'
                '\nStep 3: Initialize time : t = 0\n'
                '\nStep 4: Keep traversing the all processes while all processes are not done. Do following for i\'th process if it is not done yet.\n'
                '\nStep 4.1: If rem_bt[i] > quantum\n'
                '\nStep 4.1.1:  t = t + quantum\n'
                '\nStep 4.1.2: rem_bt[i] -= quantum;\n'
                '\nStep 4.2: Else // Last cycle for this process\n'
                '\nStep 4.2.1: t = t + rem_bt[i];\n'
                '\nStep 4.2.2: wt[i] = t - bt[i]\n'
                '\nStep 4.2.3: rem_bt[i] = 0; // This process is over\n',
              ),
          ],
        ),
      ),
    );
  }
}
