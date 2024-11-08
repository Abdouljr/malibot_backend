import 'package:flutter/material.dart';
import 'package:malibot_cheallenge/views/authentification/signin_view/signin_view.dart';
import 'package:malibot_cheallenge/widgets/defaut_button.dart';

class LoginView extends StatefulWidget {
  const LoginView({super.key});

  @override
  State<LoginView> createState() => _LoginViewState();
}

class _LoginViewState extends State<LoginView> {
  bool obscurePassword = true;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      body: Container(
        margin: const EdgeInsets.all(20),
        height: double.infinity,
        child: Column(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [_headear, _inputField, _forgotPassword, _signup],
        ),
      ),
    );
  }

  Column get _headear {
    return const Column(
      children: [
        Text(
          "Bienvenue à vous",
          style: TextStyle(fontSize: 40, fontWeight: FontWeight.bold),
        ),
        Text("Entrer vos identifiants pour vous connecter!")
      ],
    );
  }

  Column get _inputField {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        TextFormField(
          decoration: InputDecoration(
              hintText: "Email",
              border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(18),
                  borderSide: BorderSide.none),
              fillColor: Colors.deepPurple.withOpacity(0.1),
              filled: true,
              prefixIcon: const Icon(Icons.person)),
          validator: (value) {
            if (value!.isEmpty) {
              return "L'email est obligatoire";
            }
            if (!value.contains('@')) {
              return "L'email n'est pas correct";
            }
            return null;
          },
        ),
        const SizedBox(height: 10),
        TextFormField(
          decoration: InputDecoration(
              hintText: "Mot de passe",
              border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(18),
                  borderSide: BorderSide.none),
              fillColor: Colors.deepPurple.withOpacity(0.1),
              filled: true,
              prefixIcon: const Icon(Icons.password),
              suffixIcon: IconButton(
                icon: Icon(
                  obscurePassword ? Icons.visibility : Icons.visibility_off,
                  color: Colors.grey.shade600,
                ),
                onPressed: () {
                  setState(() {
                    obscurePassword = !obscurePassword;
                  });
                },
              )),
          obscureText: obscurePassword,
          validator: (value) {
            if (value!.isEmpty) {
              return "Le mot de passe est obligatoire";
            }
            if (value.length < 6) {
              return "Le mot de passe doit contenir au moins 6 caractères";
            }
            return null;
          },
        ),
        const SizedBox(height: 10),
        DefautButton(onPressed: () {}, btnText: "Se Connecter")
      ],
    );
  }

  TextButton get _forgotPassword {
    return TextButton(
      onPressed: () {},
      child: const Text(
        "Mot de passe Oublié ?",
        style: TextStyle(color: Colors.deepPurple),
      ),
    );
  }

  Row get _signup {
    return Row(mainAxisAlignment: MainAxisAlignment.center, children: [
      const Text("Je n'ai pas de compte ? "),
      TextButton(
          onPressed: () {
            Navigator.push<void>(
              context,
              MaterialPageRoute<void>(
                builder: (BuildContext context) => const SiginInView(),
              ),
            );
          },
          child: const Text(
            "S'inscrire",
            style: TextStyle(color: Colors.deepPurple),
          ))
    ]);
  }
}
