import 'package:cpu_scheduling/screens/simulate_screen.dart';
import 'package:cpu_scheduling/widgets/algorithm_card.dart';
import 'package:cpu_scheduling/widgets/definition_card.dart';
import 'package:flutter/material.dart';

class AlgorithmScreen extends StatelessWidget {
  final String algorithmName;
  const AlgorithmScreen({
    required this.algorithmName,
    Key? key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(algorithmName),
      ),
      body: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.all(10),
          child: Column(
            children: <Widget>[
              DefinitionCard(algorithmName: algorithmName),
              AlgorithmCard(algorithmName: algorithmName),
              Padding(
                padding: const EdgeInsets.all(10),
                child: ElevatedButton.icon(
                  onPressed: () {
                    Navigator.pushReplacement(
                      context,
                      MaterialPageRoute(
                        builder: (context) => SimulateScreen(
                          algorithmName: algorithmName,
                        ),
                      ),
                    );
                  },
                  icon: const Icon(Icons.timer_rounded),
                  label: const Text('Simulate'),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
