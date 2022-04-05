# LITREVIEW

Il s'agit d'une application web permettant à une communauté d'utilisateurs de consulter ou de solliciter une critique de livres à la demande.

## Faire un git clone du projet

Dans l'invite de commandes tapez `git clone https://github.com/Chreno972/oc_P9_Litreview.git`
Puis dans le terminal, taper `cd oc_P9_Litreview`, afin d'entrer dans le dossier du projet
## Installer un environnement virtuel avec venv

`python3 -m venv env`

## Activer son environnement virtuel

`env\Scripts\activate`

## Installer les packages nécessaires  requirements.txt

`pip install -r requirements.txt`

## Créer une sqlite3 database

`py manage.py migrate`
## Lancer le serveur django

`py manage.py runserver`

## Dans le terminal 
combinez 'ctrl - click' sur le lien http://127.0.0.1:8000/ qui vous dirige vers la page de connexion.

## Cliquez sur "s'inscrire" 
pour créer un nouveau compte utilisateur. Renseignez toutes les informations requises. puis clickez sur s'inscrire.

## Vous arrivez sur la page home 
qui correspond au flux. Ce flux affichera les posts des abonnés que vous suivez. 
Ici, vous pouvez créer un ticket à propos d'un livre en cliquant sur demander 'une critique', ce ticket apparaitra alors dans votre espace onglet 'posts' et dans le flux des personnes qui vous suivent.
Vous pouvez aussi créer une critique autonome afin de pouvoir noter un livre et lui donner une appréciation, cette critique autonome comme un ticket ou demande de critique apparaîtra dans votre espace, ainsi que dans le flux de ceux qui vous suivent.

## Cliquez sur 'Posts' 
pour accédez à tous vos tickets et critiques crées.

## Cliquez sur 'Abonnements'
ici vous pouvez suivre des abonnés et voir lesquels vous suivent. La section "Abonnés" affichera tous les abonnés que vous suivez, puis la section "Abonnements" affichera ceux qui vous suivent. 
Pour suivre un abonné, il vous suffit juste de taper son nom dans le formulaire et de valider.

## Cliquez sur 'Profil'
Ici, vous aurez la possibilité d'éditer votre profil, changer vos nom et adresse mail, et photo de profil. Vous pourrez aussi voir combien de Tickets et Critiques vous avez crées ainsi que le nombre de personne qui vous suit et que vous suivez.
Par défaut, un superutilisateur a été crée pour se connecter à la base de données et faire des modifications. pour l'utiliser, lancez le serveur
`py manage.py runserver`, dans la barre d'addresse de votre navigateur, tapez `http://127.0.0.1:8000/admin/`, les noms et mot de passe sont `Administrateur` et `admin2022`. Sinon, vous pouvez directement créer un nouvel utilisateur à l'adresse `http://127.0.0.1:8000/`.

## Cliquez sur 'Se déconnecter'
Pour vous déconnecter.






