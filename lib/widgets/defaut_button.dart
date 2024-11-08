import 'package:flutter/material.dart';

class DefautButton extends StatelessWidget {
  DefautButton({
    super.key,
    required this.onPressed,
    required this.btnText,
    this.btnColor = Colors.deepPurple,
    this.textColor = Colors.white,
  });

  Function()? onPressed;
  String btnText;
  Color btnColor;
  Color textColor;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.only(top: 3, left: 3),
      child: ElevatedButton(
        onPressed: onPressed as void Function()?,
        style: ElevatedButton.styleFrom(
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(15),
          ),
          padding: const EdgeInsets.symmetric(vertical: 15),
          backgroundColor: btnColor,
        ),
        child: Text(
          btnText,
          style: TextStyle(fontSize: 20, color: textColor),
        ),
      ),
    );
  }
}
