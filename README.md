# Party-Ranking
Ici, tous les scripts Python et layouts que j'utilise pour monter des PRs

(Merci par ailleurs à Baguette, Sardine, Nono à qui j'ai pu emprunter différents scripts pour les modifier à ma sauce)

# Installation
Cliquer sur le bouton vert "Code", puis Download ZIP.

Après il faut modifier le fichier config.txt et ajouter le chemin vers votre dossier PR, et la clé discord comètebot (demandez sur discord).

Enfin, mettre les PP des gens dans le dossier `pr-avatars`.

# Prérequis
Un dossier comprenant le dossier 'Images' (Images.zip contient tout ce qu'il y a dans le dossier Images), le dossier 'Vidéos' et le dossier 'PR Avatar' 
Le dossier PR Avatar contient les avatars des personnes (à vous même de le faire)

**Pour pouvoir télécharger des sons (utiliser ffmpeg)**: 
- Télécharger `ffmpeg-5.0.1-full_build.7z`(dispo sur https://www.ffmpeg.org/)
- Aller dans "Modifier les variables d'environnement système"
- Variables d'environnement > Path > Modifier > Nouveau puis coller C:\ffmpeg\bin 
- Enregistrer

Les différents scripts sont par ailleurs 
- `results.py` : crée le layout et la sheet des résultats avec les samples à remplir
- `video.py` : crée la vidéo finale
- `ScriptPR.py` : sert à la création de la vidéo (crée les layout intermédiaires avec les ranks)
- `process_PR_stats_ranking.py` : **à ne pas toucher**, crée les affinités
- 
Je vous laisse vous débrouiller pour modifier les données à chaque fois pour les différents scripts

# Méthode
- Lancer le script `results.py`
Le script va faire les affinités/stats et la sheet de résultats dans un nouveau dossier mais aussi la sheet de samples qui va nous intéresser 

- Ouvrir la sheet "(PR) samples"
 
- Remplir les vides dans Rank (correspond à des Tiebreaks)
  
![oui](https://cdn.discordapp.com/attachments/1209289359157891182/1209290298551836702/image.png?ex=660b4c5a&is=65f8d75a&hm=690a4d82d3ec2affbeec60c28884167711d84480357590ad1e1bab887616b475&)

- Remplir les colonnes Sample (seconds) et Sample length (seconds)
Sample (seconds) : correspond à la seconde où le sample commence
Sample length (seconds) : correspond à la durée du sample

![oui](https://cdn.discordapp.com/attachments/1209289359157891182/1209290697795182632/image.png?ex=660b4cb9&is=65f8d7b9&hm=93850edc926a8cd8161824887ac31dd7f6e82dff0ad53a5474c1daa55b689588&)

- Lancer le script `video.py`

À savoir: vous pouvez modifier song_per_part = ... dans votre script video.py. 
Ça correspond au nombre de sons montés avant de diviser la vidéo. (C'est-à-dire que si le nombre de sons dans votre PR est plus grand que le nombre de song_per_part, votre vidéo va se faire en plusieurs fois et vous allez devoir relancer le script entre chaque "bout de vidéo")

Conseil pour video.py: ne pas lancer sur idle
