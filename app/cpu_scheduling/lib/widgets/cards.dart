import 'package:flutter/material.dart';

import '../screens/algorithm_screen.dart';

class Cards extends StatelessWidget {
  const Cards({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return PageView(
      children: const <Widget>[
        MyCard(
          title: 'What is CPU Scheduling?',
          desctiption:
              'CPU Scheduling is a process of determining which process will own CPU for execution while another process is on hold. The main task is to make sure that the CPU never remains idle, the OS selects one of the processes available in the ready queue for execution.\nIn Multiprogramming systems, the Operating system schedules the processes on the CPU to have the maximum utilization of it and this procedure is called CPU scheduling. The Operating System uses various scheduling algorithms to schedule the processes.',
          imagePath: 'assets/images/CPU-Scheduling.png',
        ),
        MyCard(
          title: 'Non-Preemptive',
          desctiption:
              'Non-preemptive Scheduling is a CPU scheduling technique the process takes the resource (CPU time) and holds it till the process gets terminated or is pushed to the waiting state. No process is interrupted until it is completed, and after that processor switches to another process.',
          imagePath: 'assets/images/Non-Preemptive.png',
        ),
        MyCard(
          title: 'Preemptive',
          desctiption:
              'Preemptive Scheduling works by dividing time slots of CPU to a given process. The time slot given might be able to complete the whole process or might not be able to it. When the burst time of the process is greater than CPU cycle, it is placed back into the ready queue and will execute in the next chance.',
          imagePath: 'assets/images/Preemptive.png',
        ),
      ],
    );
  }
}

class MyCard extends StatelessWidget {
  final String title, desctiption, imagePath;
  const MyCard({
    Key? key,
    required this.title,
    required this.desctiption,
    required this.imagePath,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(20),
      child: Card(
        elevation: 5,
        child: Padding(
          padding: const EdgeInsets.all(10.0),
          child: Column(
            children: <Widget>[
              Text(
                title,
                style: Theme.of(context).textTheme.titleLarge,
              ),
              const Divider(),
              Expanded(
                flex: 1,
                child: SingleChildScrollView(
                  child: Text(
                    desctiption,
                    style: const TextStyle(
                      height: 1.5,
                    ),
                  ),
                ),
              ),
              if (title != 'What is CPU Scheduling?')
                Padding(
                  padding: const EdgeInsets.all(25),
                  child: title == 'Non-Preemptive'
                      ? Column(
                          children: <Widget>[
                            const Text('Examples: '),
                            OutlinedButton(
                              child: const Text('First Come First Serve'),
                              onPressed: () {
                                Navigator.push(
                                  context,
                                  MaterialPageRoute(
                                    builder: (context) => const AlgorithmScreen(
                                      algorithmName: 'First Come First Serve',
                                    ),
                                  ),
                                );
                              },
                            ),
                            OutlinedButton(
                              child: const Text('Shortest Job First'),
                              onPressed: () {
                                Navigator.push(
                                  context,
                                  MaterialPageRoute(
                                    builder: (context) => const AlgorithmScreen(
                                      algorithmName: 'Shortest Job First',
                                    ),
                                  ),
                                );
                              },
                            ),
                          ],
                        )
                      : Column(
                          children: <Widget>[
                            const Text('Examples: '),
                            OutlinedButton(
                              child: const Text('Shortest Remaining Time Next'),
                              onPressed: () {
                                Navigator.push(
                                  context,
                                  MaterialPageRoute(
                                    builder: (context) => const AlgorithmScreen(
                                      algorithmName:
                                          'Shortest Remaining Time Next',
                                    ),
                                  ),
                                );
                              },
                            ),
                            OutlinedButton(
                              child: const Text('Round Robin'),
                              onPressed: () {
                                Navigator.push(
                                  context,
                                  MaterialPageRoute(
                                    builder: (context) => const AlgorithmScreen(
                                      algorithmName: 'Round Robin',
                                    ),
                                  ),
                                );
                              },
                            ),
                          ],
                        ),
                ),
              const Divider(),
              Image(
                image: AssetImage(imagePath),
                fit: BoxFit.fitHeight,
              ),
            ],
          ),
        ),
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(15),
        ),
      ),
    );
  }
}
