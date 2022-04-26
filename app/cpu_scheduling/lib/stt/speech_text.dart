import 'dart:async';
import 'dart:math';

import 'package:flutter/material.dart';
import 'package:speech_to_text/speech_recognition_error.dart';
import 'package:speech_to_text/speech_recognition_result.dart';
import 'package:speech_to_text/speech_to_text.dart';

import '../screens/algorithm_screen.dart';
import '../screens/simulate_screen.dart';

class SpeechText extends StatefulWidget {
  const SpeechText({Key? key}) : super(key: key);

  @override
  _SpeechTextState createState() => _SpeechTextState();
}

class _SpeechTextState extends State<SpeechText> {
  bool _hasSpeech = false;
  double level = 0.0;
  double minSoundLevel = 50000;
  double maxSoundLevel = -50000;
  String lastWords = '';
  String lastError = '';
  String lastStatus = '';
  String _currentLocaleId = '';
  final SpeechToText speech = SpeechToText();

  @override
  void initState() {
    super.initState();
  }

  Future<void> initSpeechState() async {
    try {
      var hasSpeech = await speech.initialize(
        onError: errorListener,
        onStatus: statusListener,
        debugLogging: true,
      );
      if (hasSpeech) {
        var systemLocale = await speech.systemLocale();
        _currentLocaleId = systemLocale?.localeId ?? '';
      }
      if (!mounted) return;

      setState(() {
        _hasSpeech = hasSpeech;
      });
    } catch (e) {
      setState(() {
        lastError = 'Speech recognition failed: ${e.toString()}';
        _hasSpeech = false;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Speech to Text'),
      ),
      body: Column(
        children: <Widget>[
          Column(
            children: <Widget>[
              InitSpeechWidget(
                _hasSpeech,
                initSpeechState,
              ),
              SpeechControlWidget(
                _hasSpeech,
                speech.isListening,
                startListening,
                stopListening,
              ),
            ],
          ),
          Expanded(
            flex: 4,
            child: RecognitionResultsWidget(
              lastWords: lastWords,
              level: level,
            ),
          ),
          SpeechStatusWidget(
            speech: speech,
          ),
        ],
      ),
    );
  }

  void startListening() {
    lastWords = '';
    lastError = '';
    speech.listen(
        onResult: resultListener,
        listenFor: const Duration(seconds: 30),
        pauseFor: const Duration(seconds: 5),
        partialResults: true,
        localeId: _currentLocaleId,
        onSoundLevelChange: soundLevelListener,
        cancelOnError: true,
        listenMode: ListenMode.confirmation);
    setState(() {});
  }

  void stopListening() {
    speech.stop();
    setState(() {
      level = 0.0;
    });
  }

  void _goTo(String title) {
    Navigator.pushReplacement(
      context,
      MaterialPageRoute(
        builder: (context) => AlgorithmScreen(
          algorithmName: title,
        ),
      ),
    );
  }

  void _simulateTo(String title) {
    Navigator.pushReplacement(
      context,
      MaterialPageRoute(
        builder: (context) => SimulateScreen(
          algorithmName: title,
        ),
      ),
    );
  }

  void resultListener(SpeechRecognitionResult result) {
    if (result.recognizedWords.toLowerCase() == "go to fcfs" ||
        result.recognizedWords.toLowerCase() ==
            "go to first come first serve") {
      _goTo("First Come First Serve");
    } else if (result.recognizedWords.toLowerCase() == "simulate fcfs" ||
        result.recognizedWords.toLowerCase() ==
            "simulate first come first serve") {
      _simulateTo("First Come First Serve");
    } else if (result.recognizedWords.toLowerCase() == "go to sjf" ||
        result.recognizedWords.toLowerCase() == "go to shortest job first") {
      _goTo("Shortest Job First");
    } else if (result.recognizedWords.toLowerCase() == "simulate sjf" ||
        result.recognizedWords.toLowerCase() == "simulate shortest job first") {
      _simulateTo("Shortest Job First");
    } else if (result.recognizedWords.toLowerCase() == "go to srtn" ||
        result.recognizedWords.toLowerCase() ==
            "go to shortest remaining time next") {
      _goTo("Shortest Remaining Time Next");
    } else if (result.recognizedWords.toLowerCase() == "simulate srtn" ||
        result.recognizedWords.toLowerCase() ==
            "simulate shortest remaining time next") {
      _simulateTo("Shortest Remaining Time Next");
    } else if (result.recognizedWords.toLowerCase() == "go to rr" ||
        result.recognizedWords.toLowerCase() == "go to round robin") {
      _goTo("Round Robin");
    } else if (result.recognizedWords.toLowerCase() == "simulate rr" ||
        result.recognizedWords.toLowerCase() == "simulate round robin") {
      _simulateTo("Round Robin");
    } else {
      setState(() {
        lastWords = '${result.recognizedWords} - ${!result.finalResult}';
      });
    }
  }

  void soundLevelListener(double level) {
    minSoundLevel = min(minSoundLevel, level);
    maxSoundLevel = max(maxSoundLevel, level);
    setState(() {
      this.level = level;
    });
  }

  void errorListener(SpeechRecognitionError error) {
    setState(() {
      lastError = '${error.errorMsg} - ${error.permanent}';
    });
  }

  void statusListener(String status) {
    setState(() {
      lastStatus = status;
    });
  }
}

/// Displays the most recently recognized words and the sound level.
class RecognitionResultsWidget extends StatelessWidget {
  const RecognitionResultsWidget({
    Key? key,
    required this.lastWords,
    required this.level,
  }) : super(key: key);

  final String lastWords;
  final double level;

  @override
  Widget build(BuildContext context) {
    return Column(
      children: <Widget>[
        Expanded(
          child: ListTile(
            title: const Text('Recognized Words:'),
            subtitle: Center(
              child: Text(
                lastWords,
                textAlign: TextAlign.center,
              ),
            ),
          ),
        ),
        // Expanded(
        //   child: Center(
        //     child: Text(
        //       lastWords,
        //       textAlign: TextAlign.center,
        //     ),
        //   ),
        // ),
        const Text(
            "Speak one of the following commands:\n\t'Go to FCFS' or 'Simulate FCFS'\n\t'Go to SJF' or 'Simulate SJF'\n\t'Go to SRTN' or 'Simulate SRTN'\n\t'Go to RR' or 'Simulate RR'"),
      ],
    );
  }
}

class SpeechControlWidget extends StatelessWidget {
  const SpeechControlWidget(
      this.hasSpeech, this.isListening, this.startListening, this.stopListening,
      {Key? key})
      : super(key: key);

  final bool hasSpeech;
  final bool isListening;
  final void Function() startListening;
  final void Function() stopListening;

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.spaceAround,
      children: <Widget>[
        OutlinedButton.icon(
          onPressed: !hasSpeech || isListening ? null : startListening,
          icon: const Icon(Icons.mic_rounded),
          label: const Text('Start'),
        ),
        OutlinedButton.icon(
          onPressed: isListening ? stopListening : null,
          icon: const Icon(Icons.mic_off_rounded),
          label: const Text('Stop'),
        ),
      ],
    );
  }
}

class InitSpeechWidget extends StatelessWidget {
  const InitSpeechWidget(this.hasSpeech, this.initSpeechState, {Key? key})
      : super(key: key);

  final bool hasSpeech;
  final Future<void> Function() initSpeechState;

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.spaceAround,
      children: <Widget>[
        OutlinedButton.icon(
          onPressed: hasSpeech ? null : initSpeechState,
          icon: const Icon(Icons.start_rounded),
          label: const Text('Initialize'),
        ),
      ],
    );
  }
}

class SpeechStatusWidget extends StatelessWidget {
  const SpeechStatusWidget({
    Key? key,
    required this.speech,
  }) : super(key: key);

  final SpeechToText speech;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.symmetric(vertical: 20),
      color: Theme.of(context).backgroundColor,
      child: Center(
        child: speech.isListening
            ? const Text(
                "Listening...",
                style: TextStyle(fontWeight: FontWeight.bold),
              )
            : const Text(
                'Not listening',
                style: TextStyle(fontWeight: FontWeight.bold),
              ),
      ),
    );
  }
}
