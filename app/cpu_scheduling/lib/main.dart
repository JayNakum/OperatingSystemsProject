import 'package:flutter/material.dart';
import 'package:firebase_core/firebase_core.dart';

import './screens/home_screen.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'CPU Scheduling',
      theme: ThemeData(
        primarySwatch: Colors.indigo,
        fontFamily: 'Raleway',
      ),
      home: FutureBuilder(
        future: Firebase.initializeApp(),
        builder: (ctx, snapshot) {
          if (snapshot.hasError) {
            return const Center(child: Text('Something went Wrong :('));
          }
          if (snapshot.connectionState == ConnectionState.waiting) {
            return const Center(child: CircularProgressIndicator());
          }
          return const HomeScreen();
        },
      ),
    );
  }
}
