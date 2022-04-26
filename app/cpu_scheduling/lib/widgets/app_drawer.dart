import 'package:cpu_scheduling/screens/about_screen.dart';
import 'package:cpu_scheduling/screens/simulate_screen.dart';
import 'package:flutter/material.dart';

class AppDrawer extends StatelessWidget {
  const AppDrawer({Key? key}) : super(key: key);

  void _navigateTo(BuildContext context, String name) {
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => SimulateScreen(
          algorithmName: name,
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Drawer(
      child: ListView(
        children: <Widget>[
          DrawerHeader(
            decoration: BoxDecoration(
              color: Theme.of(context).colorScheme.primary,
            ),
            child: const Center(
              child: Text(
                'OS Project',
                style: TextStyle(
                  color: Colors.white,
                  fontSize: 21,
                ),
              ),
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(10),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: <Widget>[
                const Text('Jump to simulation\n'),
                ListTile(
                  leading: const Icon(Icons.queue_rounded),
                  title: const Text('FCFS'),
                  subtitle: const Text('First Come First Serve'),
                  onTap: () {
                    _navigateTo(context, 'First Come First Serve');
                  },
                ),
                ListTile(
                  leading: const Icon(Icons.short_text_rounded),
                  title: const Text('SJF'),
                  subtitle: const Text('Shortest Job First'),
                  onTap: () {
                    _navigateTo(context, 'Shortest Job First');
                  },
                ),
                const Divider(),
                ListTile(
                  leading: const Icon(Icons.timelapse_rounded),
                  title: const Text('SRTN'),
                  subtitle: const Text('Shortest Rremaining Time Next'),
                  onTap: () {
                    _navigateTo(context, 'Shortest Remaining Time Next');
                  },
                ),
                ListTile(
                  leading: const Icon(Icons.replay_rounded),
                  title: const Text('RR'),
                  subtitle: const Text('Round Robin'),
                  onTap: () {
                    _navigateTo(context, 'Round Robin');
                  },
                ),
                const Divider(),
                ListTile(
                  leading: const Icon(Icons.info_rounded),
                  title: const Text('About'),
                  onTap: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => const AboutScreen(),
                      ),
                    );
                  },
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
