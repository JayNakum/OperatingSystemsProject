import 'package:cpu_scheduling/models/processes.dart';
import 'package:firebase_storage/firebase_storage.dart';
import 'package:flutter/material.dart';
import 'package:photo_view/photo_view.dart';

class ResultScreen extends StatefulWidget {
  final Processes processes;
  const ResultScreen({
    required this.processes,
    Key? key,
  }) : super(key: key);

  @override
  State<ResultScreen> createState() => _ResultScreenState();
}

class _ResultScreenState extends State<ResultScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        title: const Text('Result'),
        actions: <Widget>[
          IconButton(
            onPressed: () {
              setState(() {});
            },
            icon: const Icon(Icons.refresh_rounded),
          ),
        ],
      ),
      body: Padding(
        padding: const EdgeInsets.all(10.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.start,
          children: [
            const ListTile(
              title: Text('Gantt Chart'),
              trailing: Icon(Icons.bar_chart_rounded),
            ),
            StreamBuilder<String>(
              stream: FirebaseStorage.instance
                  .ref('output/ganttChart.png')
                  .getDownloadURL()
                  .asStream(),
              builder: (context, snapshot) {
                if (snapshot.hasData) {
                  return Image(url: snapshot.data!);
                }
                return const CircularProgressIndicator();
              },
            ),
            const Divider(),
            const ListTile(
              title: Text('Output Table'),
              trailing: Icon(Icons.table_chart_rounded),
            ),
            StreamBuilder<String>(
              stream: FirebaseStorage.instance
                  .ref('output/outputTable.png')
                  .getDownloadURL()
                  .asStream(),
              builder: (context, snapshot) {
                if (snapshot.hasData) {
                  return Image(url: snapshot.data!);
                }
                return const CircularProgressIndicator();
              },
            ),
          ],
        ),
      ),
    );
  }
}

class Image extends StatelessWidget {
  final String url;
  const Image({
    required this.url,
    Key? key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return AspectRatio(
      aspectRatio: 16 / 9,
      child: ClipRect(
        child: PhotoView(
          backgroundDecoration: const BoxDecoration(color: Colors.white),
          imageProvider: NetworkImage(url),
          minScale: PhotoViewComputedScale.contained * 0.8,
          maxScale: PhotoViewComputedScale.covered * 2,
        ),
      ),
    );
  }
}
