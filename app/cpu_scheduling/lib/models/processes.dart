import 'package:cloud_firestore/cloud_firestore.dart';

class Processes {
  int _timeQuantum = 0;
  final List<Map<String, int>> _processes = [];

  List<Map<String, int>> getProcesses() {
    return _processes;
  }

  void setProcesses(List<Map<String, int>> processes) {
    _processes.clear();
    _processes.addAll(processes);
  }

  void setQuantum(int quantum) {
    _timeQuantum = quantum;
  }

  Future<void> uploadToFirebase(String algorithmName) async {
    var collection = FirebaseFirestore.instance.collection('CPU Scheduling');
    var snapshots = await collection.get();
    for (var doc in snapshots.docs) {
      await doc.reference.delete();
    }
    await collection
        .doc(algorithmName)
        .set({'Processes': _processes, 'Time Quantum': _timeQuantum});
  }
}
