import 'package:cpu_scheduling/models/processes.dart';
import 'package:cpu_scheduling/screens/result_screen.dart';
import 'package:flutter/material.dart';

class SimulateScreen extends StatefulWidget {
  final String algorithmName;
  const SimulateScreen({
    required this.algorithmName,
    Key? key,
  }) : super(key: key);

  @override
  State<SimulateScreen> createState() => _GetProcessesState();
}

class _GetProcessesState extends State<SimulateScreen> {
  final _formKey = GlobalKey<FormState>();
  final Processes _processes = Processes();
  final List<Map<String, int>> _inputProcesses = [];
  int _timeQuantum = 0;

  void submitProcesses() {
    FocusScope.of(context).unfocus();
    if (_formKey.currentState!.validate()) {
      _processes.setProcesses(_inputProcesses);
      _processes.setQuantum(_timeQuantum);
      _processes.uploadToFirebase(widget.algorithmName).then(
            (_) => {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => ResultScreen(processes: _processes),
                ),
              ),
            },
          );
    }
    _inputProcesses.clear();
  }

  @override
  Widget build(BuildContext context) {
    AppBar appBar = AppBar(title: const Text('Simulation'));
    return Scaffold(
      appBar: appBar,
      body: Padding(
        padding: EdgeInsets.only(bottom: 1.5 * appBar.preferredSize.height),
        child: Form(
          key: _formKey,
          child: Column(
            children: <Widget>[
              if (widget.algorithmName == 'Round Robin')
                Padding(
                  padding: const EdgeInsets.all(8.0),
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: <Widget>[
                      const Text('Time Quantum: '),
                      SizedBox(
                        width: 125,
                        child: TextFormField(
                          validator: (value) {
                            if (int.tryParse(value!) != null) {
                              if (int.parse(value) > 0) {
                                return null;
                              }
                            }
                            return 'invalid input';
                          },
                          onChanged: (value) {
                            _timeQuantum = int.parse(value);
                          },
                          keyboardType: TextInputType.number,
                        ),
                      ),
                    ],
                  ),
                ),
              Expanded(
                child: _inputProcesses.isEmpty
                    ? const Center(child: Text('Click + to add processes.'))
                    : ListView.builder(
                        padding: const EdgeInsets.all(8.0),
                        itemCount: _inputProcesses.length,
                        itemBuilder: (ctx, i) {
                          _inputProcesses[i]['Process ID'] = i;
                          return Card(
                            child: Padding(
                              padding: const EdgeInsets.symmetric(vertical: 8),
                              child: Row(
                                mainAxisAlignment:
                                    MainAxisAlignment.spaceEvenly,
                                children: <Widget>[
                                  Text('PID $i'),
                                  SizedBox(
                                    width: 125,
                                    child: TextFormField(
                                      decoration: const InputDecoration(
                                        hintText: 'Arrival Time',
                                      ),
                                      validator: (value) {
                                        if (int.tryParse(value!) != null) {
                                          if (int.parse(value) >= 0) {
                                            return null;
                                          }
                                        }
                                        return 'Invalid';
                                      },
                                      onChanged: (value) {
                                        if (int.tryParse(value) != null) {
                                          _inputProcesses[i]['Arrival Time'] =
                                              int.parse(value);
                                        }
                                      },
                                      keyboardType: TextInputType.number,
                                    ),
                                  ),
                                  SizedBox(
                                    width: 125,
                                    child: TextFormField(
                                      decoration: const InputDecoration(
                                        hintText: 'Burst Time',
                                      ),
                                      validator: (value) {
                                        if (int.tryParse(value!) != null) {
                                          if (int.parse(value) > 0) {
                                            return null;
                                          }
                                        }
                                        return 'Invalid';
                                      },
                                      onChanged: (value) {
                                        _inputProcesses[i]['Burst Time'] =
                                            int.parse(value);
                                      },
                                      keyboardType: TextInputType.number,
                                    ),
                                  ),
                                ],
                              ),
                            ),
                          );
                        },
                      ),
              ),
            ],
          ),
        ),
      ),
      floatingActionButtonLocation: FloatingActionButtonLocation.centerFloat,
      floatingActionButton: Row(
        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        children: <Widget>[
          FloatingActionButton(
            heroTag: 'Remove',
            onPressed: () {
              if (_inputProcesses.isNotEmpty) {
                setState(() {
                  _inputProcesses.removeLast();
                });
              }
            },
            child: const Icon(Icons.remove_rounded),
          ),
          SizedBox(
            width: 150,
            child: FloatingActionButton(
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(5),
              ),
              onPressed: submitProcesses,
              child: const Text('Simulate'),
            ),
          ),
          FloatingActionButton(
            heroTag: 'Add',
            onPressed: () {
              setState(() {
                _inputProcesses.add({});
              });
            },
            child: const Icon(Icons.add_rounded),
          ),
        ],
      ),
    );
  }
}
