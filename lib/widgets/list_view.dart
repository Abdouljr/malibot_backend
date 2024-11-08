import 'package:flutter/material.dart';

class ListItem extends StatelessWidget {
  ListItem({super.key, required this.titre});
  String titre;

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
        child: ListTile(
      leading: Container(
        decoration:
            BoxDecoration(shape: BoxShape.circle, color: Colors.grey.shade100),
        padding: const EdgeInsets.all(8.0),
        child: Icon(
          Icons.list_alt,
          color: Colors.deepPurple.withOpacity(0.8),
          size: 22.0,
        ),
      ),
      title: Text(
        "Titre de la liste de tâches",
        style: Theme.of(context).textTheme.bodyMedium!.copyWith(
              fontWeight: FontWeight.bold,
              color: Colors.black87,
            ),
      ),
      subtitle: Text(
        "Description de la liste de tâches",
        overflow: TextOverflow.ellipsis,
        style: Theme.of(context).textTheme.bodySmall!.copyWith(
              fontWeight: FontWeight.w400,
              color: Colors.black87,
            ),
      ),
      trailing: Container(
        decoration:
            BoxDecoration(shape: BoxShape.circle, color: Colors.grey.shade100),
        padding: const EdgeInsets.all(8.0),
        child: Text(
          titre,
          style: Theme.of(context).textTheme.bodyMedium!.copyWith(
                color: Colors.deepPurple.withOpacity(0.8),
              ),
        ),
      ),
    ));
  }
}
