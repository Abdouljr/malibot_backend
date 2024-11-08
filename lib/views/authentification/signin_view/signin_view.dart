import 'package:flutter/material.dart';
import 'package:malibot_cheallenge/views/authentification/login_view/login_view.dart';
import 'package:malibot_cheallenge/widgets/defaut_button.dart';

class SiginInView extends StatefulWidget {
  const SiginInView({super.key});

  @override
  State<SiginInView> createState() => _SiginInViewState();
}

class _SiginInViewState extends State<SiginInView> {
  bool obscurePassword = true;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: const Color.fromRGBO(255, 255, 255, 1),
        body: SingleChildScrollView(
          child: Container(
            height: MediaQuery.of(context).size.height - 50,
            width: double.infinity,
            padding: const EdgeInsets.symmetric(horizontal: 20),
            child: Column(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                _hearder,
                _inputField,
                DefautButton(onPressed: () {}, btnText: "S'inscrire"),
                _login
              ],
            ),
          ),
        ));
  }

  Column get _hearder {
    return Column(children: <Widget>[
      const SizedBox(height: 60.0),
      const Text(
        "S'inscrire",
        style: TextStyle(
          fontSize: 30,
          fontWeight: FontWeight.bold,
        ),
      ),
      const SizedBox(
        height: 20,
      ),
      Text(
        "Creer un compte pour commencer",
        style: TextStyle(fontSize: 15, color: Colors.grey[700]),
      )
    ]);
  }

  Column get _inputField {
    return Column(
      children: <Widget>[
        TextFormField(
          decoration: InputDecoration(
              hintText: "Nom d'utilisateur",
              border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(18),
                  borderSide: BorderSide.none),
              fillColor: Colors.deepPurple.withOpacity(0.1),
              filled: true,
              prefixIcon: const Icon(Icons.person)),
        ),
        const SizedBox(height: 12),
        TextFormField(
          decoration: InputDecoration(
              hintText: "Email",
              border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(18),
                  borderSide: BorderSide.none),
              fillColor: Colors.deepPurple.withOpacity(0.1),
              filled: true,
              prefixIcon: const Icon(Icons.email)),
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
        const SizedBox(height: 12),
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
        const SizedBox(height: 12),
        TextFormField(
          decoration: InputDecoration(
              hintText: "Confirmer Mot de passe",
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
        ),
      ],
    );
  }

  Row get _login {
    return Row(mainAxisAlignment: MainAxisAlignment.center, children: <Widget>[
      const Text("J'ai un déjà un compte ! "),
      TextButton(
          onPressed: () {
            Navigator.push<void>(
              context,
              MaterialPageRoute<void>(
                builder: (BuildContext context) => const LoginView(),
              ),
            );
          },
          child: const Text(
            "Se Connecter",
            style: TextStyle(color: Colors.deepPurple),
          ))
    ]);
  }
}
