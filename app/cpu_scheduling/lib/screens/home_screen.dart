import 'package:cpu_scheduling/stt/speech_text.dart';
import 'package:flutter/material.dart';

import '../widgets/app_drawer.dart';
import '../widgets/cards.dart';

class HomeScreen extends StatelessWidget {
  static const routeName = 'home-screen';
  const HomeScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      drawer: const AppDrawer(),
      appBar: AppBar(
        title: const Text('CPU Scheduling'),
        actions: [
          IconButton(
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => const SpeechText(),
                ),
              );
            },
            icon: const Icon(Icons.mic_rounded),
          ),
        ],
      ),
      body: const Cards(),
    );
  }
}
