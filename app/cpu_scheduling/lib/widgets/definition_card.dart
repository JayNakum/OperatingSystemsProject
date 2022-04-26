import 'package:flutter/material.dart';

class DefinitionCard extends StatefulWidget {
  final String algorithmName;
  const DefinitionCard({
    required this.algorithmName,
    Key? key,
  }) : super(key: key);

  @override
  State<DefinitionCard> createState() => _DefinitionCardState();
}

class _DefinitionCardState extends State<DefinitionCard> {
  bool _showDefinition = false;
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
                  _showDefinition = !_showDefinition;
                });
              },
              title: Text('What is ${widget.algorithmName}?'),
              trailing: const Icon(Icons.arrow_drop_down_rounded),
            ),
            if (widget.algorithmName == 'First Come First Serve' &&
                _showDefinition)
              const Text(
                '\nThe process with the minimal arrival time will get the CPU first.'
                'The lesser the arrival time, the sooner will the process gets the CPU.\n',
              ),
            if (widget.algorithmName == 'Shortest Job First' && _showDefinition)
              const Text(
                '\nProcess which have the shortest burst time are scheduled first.\n'
                'If two processes have the same bust time then FCFS is used to break the tie.\n',
              ),
            if (widget.algorithmName == 'Shortest Remaining Time Next' &&
                _showDefinition)
              const Text(
                '\nIt is the preemptive form of SJF. In this algorithm, '
                'the OS schedules the Job according to the remaining time of the execution.\n',
              ),
            if (widget.algorithmName == 'Round Robin' && _showDefinition)
              const Text(
                '\nIn the Round Robin scheduling algorithm, the OS defines a time quantum (slice).\n'
                'All the processes will get executed in the cyclic way. '
                'Each of the process will get the CPU for a small amount of time (called time quantum) '
                'and then get back to the ready queue to wait for its next turn.\n',
              ),
          ],
        ),
      ),
    );
  }
}
