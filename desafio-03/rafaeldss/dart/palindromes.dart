import 'dart:io';

void main() {
  var begin = int.parse(stdin.readLineSync());
  var end = int.parse(stdin.readLineSync());

  for (; begin <= end; begin++) {
    var value = begin.toString();
    String reversedValue = value.split('').reversed.join();

    if (value == reversedValue) {
      print("$value");
    }
  }
}
