import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:malibot_cheallenge/widgets/list_view.dart';

class HomeView extends StatefulWidget {
  const HomeView({super.key});

  @override
  State<HomeView> createState() => _HomeViewState();
}

class _HomeViewState extends State<HomeView> {
  List<MenuItem> menuItems = [
    MenuItem(title: "Aujourd'hui", icon: Icons.calendar_today),
    MenuItem(title: "importants", icon: Icons.star_border),
    MenuItem(title: "Réglages", icon: Icons.settings),
    MenuItem(title: "Deconnexion", icon: Icons.power_settings_new),
  ];

  List<String> ages = ["22", "5", "44", "23", "22"];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.white,
        leadingWidth: 60,
        leading: Container(
          padding: const EdgeInsets.all(5.0),
          margin: const EdgeInsets.all(5.0),
          decoration: BoxDecoration(
              shape: BoxShape.circle, color: Colors.grey.shade100),
          child: const Icon(
            CupertinoIcons.person,
            color: Colors.deepPurple,
            size: 22.0,
          ),
        ),
        title: _titleContent(context),
        actions: [
          GestureDetector(
            onTap: () {},
            child: Container(
              decoration: BoxDecoration(
                  shape: BoxShape.circle, color: Colors.grey.shade100),
              padding: const EdgeInsets.all(8.0),
              margin: const EdgeInsets.all(8.0),
              child: const Icon(
                Icons.search,
                color: Colors.deepPurple,
                size: 24.0,
              ),
            ),
          ),
        ],
      ),
      body: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
        Card(
          elevation: 0.5,
          shadowColor: Colors.grey.shade100,
          surfaceTintColor: Colors.white,
          shape:
              RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
          margin: const EdgeInsets.symmetric(horizontal: 10, vertical: 15),
          child: SizedBox(
              height: 80,
              width: double.infinity,
              child: ListView.builder(
                scrollDirection: Axis.horizontal,
                padding: const EdgeInsets.all(5),
                shrinkWrap: true,
                physics: const BouncingScrollPhysics(),
                itemCount: menuItems.length,
                itemBuilder: (BuildContext context, int index) {
                  MenuItem item = menuItems[index];
                  return MenuItem_widget(item: item);
                },
              )),
        ),
        const Padding(
          padding: EdgeInsets.all(8.0),
          child: Text(
            'Listes de Taches',
            textAlign: TextAlign.left,
            style: TextStyle(
              fontSize: 15,
              fontWeight: FontWeight.bold,
              color: Colors.black,
            ),
          ),
        ),
        ListView.builder(
          physics: const NeverScrollableScrollPhysics(),
          shrinkWrap: true,
          itemCount: ages.length,
          itemBuilder: (BuildContext context, int index) {
            String age = ages[index];
            return ListItem(titre: age);
          },
        )
      ]),
      bottomNavigationBar: Container(
        height: 50,
        width: double.infinity,
        padding: const EdgeInsets.symmetric(horizontal: 10),
        child:
            Row(mainAxisAlignment: MainAxisAlignment.spaceBetween, children: [
          GestureDetector(
            child:
                Row(crossAxisAlignment: CrossAxisAlignment.center, children: [
              Container(
                decoration: BoxDecoration(
                    shape: BoxShape.circle, color: Colors.grey.shade100),
                padding: const EdgeInsets.all(5.0),
                margin: const EdgeInsets.all(8.0),
                child: const Icon(
                  CupertinoIcons.add,
                  color: Colors.deepPurple,
                  size: 20.0,
                ),
              ),
              const Text(
                'Nouvelle Liste',
                style: TextStyle(
                  fontSize: 14,
                  fontWeight: FontWeight.bold,
                  color: Colors.deepPurple,
                ),
              ),
            ]),
          ),
          GestureDetector(
            onTap: () {},
            child: Container(
              decoration: BoxDecoration(
                  shape: BoxShape.circle, color: Colors.grey.shade100),
              padding: const EdgeInsets.all(5.0),
              margin: const EdgeInsets.all(8.0),
              child: const Icon(
                Icons.post_add_outlined,
                color: Colors.deepPurple,
                size: 24.0,
              ),
            ),
          ),
        ]),
      ),
    );
  }

  Column _titleContent(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          'Abdouljr',
          style: Theme.of(context).textTheme.titleMedium!.copyWith(
                fontWeight: FontWeight.bold,
                color: Colors.black87,
              ),
        ),
        Text(
          'maigaabdoulaziz795@gmail.com',
          style: Theme.of(context).textTheme.titleSmall!.copyWith(
                color: Colors.grey.shade700,
                fontWeight: FontWeight.w400,
              ),
        ),
      ],
    );
  }
}

class MenuItem_widget extends StatelessWidget {
  const MenuItem_widget({
    super.key,
    required this.item,
  });

  final MenuItem item;

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
        onTap: () {},
        child: Container(
            padding: const EdgeInsets.symmetric(horizontal: 15, vertical: 5),
            child: Column(
              mainAxisAlignment: MainAxisAlignment.spaceAround,
              children: [
                Container(
                  decoration: BoxDecoration(
                      shape: BoxShape.circle, color: Colors.grey.shade100),
                  padding: const EdgeInsets.all(8.0),
                  child: Icon(
                    item.icon,
                    color: item.color!.withOpacity(0.8),
                    size: 22.0,
                  ),
                ),
                Text(
                  item.title,
                  style: Theme.of(context).textTheme.bodySmall!.copyWith(
                        fontWeight: FontWeight.w400,
                        color: Colors.black87,
                      ),
                ),
              ],
            )));
  }
}

class MenuItem {
  String title;
  IconData icon;
  Color? color;
  VoidCallback? onTap;
  MenuItem(
      {required this.title,
      required this.icon,
      this.color = Colors.deepPurple,
      this.onTap});
}
