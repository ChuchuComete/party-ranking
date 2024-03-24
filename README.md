# Party-Ranking
Ici, tous les scripts Python que j'utilise pour monter des PRs 

(Merci par ailleurs à Baguette, Sardine, Nono à qui j'ai pu emprunter différents scripts pour les modifier à ma sauce)

# Prérequis
Un dossier comprenant le dossier 'Images', le dossier 'Vidéos' et le dossier 'PR Avatar' 
Le dossier PR Avatar contient les avatars des personnes (à vous même de le faire)

Je vous laisse vous débrouiller pour modifier les données à chaque fois pour les différents scripts
# Méthode
- Lancer le script results.py
Le script va faire les affinités/stats et la sheet de résultats dans un nouveau dossier mais aussi la sheet de samples qui va nous intéresser 

- Ouvrir la sheet "(PR) samples"
 
- Remplir les vides dans Rank (correspond à des Tiebreaks)
  
![oui](https://cdn.discordapp.com/attachments/1209289359157891182/1209290298551836702/image.png?ex=660b4c5a&is=65f8d75a&hm=690a4d82d3ec2affbeec60c28884167711d84480357590ad1e1bab887616b475&)

- Remplir les colonnes Sample (seconds) et Sample length (seconds)
Sample (seconds) : correspond à la seconde où le sample commence
Sample length (seconds) : correspond à la durée du sample

![oui](https://cdn.discordapp.com/attachments/1209289359157891182/1209290697795182632/image.png?ex=660b4cb9&is=65f8d7b9&hm=93850edc926a8cd8161824887ac31dd7f6e82dff0ad53a5474c1daa55b689588&)

- Lancer le script video.py

À savoir: vous pouvez modifier song_per_part = ... dans votre script video.py. 
Ça correspond au nombre de sons montés avant de diviser la vidéo. (C'est-à-dire que si le nombre de sons dans votre PR est plus grand que le nombre de song_per_part, votre vidéo va se faire en plusieurs fois et vous allez devoir relancer le script entre chaque "bout de vidéo")

Conseil pour video.py: ne pas lancer sur idle
