import 'package:flutter/material.dart';

class AboutScreen extends StatelessWidget {
  const AboutScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('About Us'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(10.0),
        child: Column(
          children: <Widget>[
            Text(
              'Team Members:',
              style: Theme.of(context).textTheme.headlineMedium,
            ),
            Text(
              'Jay Nakum\n'
              'Vipul Chaudhary\n'
              'Chintan Udani\n'
              'Jenish Modh\n'
              'Shreya Panengadan\n'
              'Disha Dugad\n',
              style: Theme.of(context).textTheme.headlineSmall,
            )
          ],
        ),
      ),
    );
  }
}
