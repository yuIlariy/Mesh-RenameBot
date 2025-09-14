from dataclasses import dataclass
import random

@dataclass
class FrenchTranslations:
    LANGUAGE_NAME = "🇫🇷 Français"
    LANGUAGE_CODE = "fr"

    WRONG_VALUE_ERROR = "❌ Oups ! Valeur invalide pour {{ variable_name }}. Réessaye ! 🤷‍♀️"

    START_MSG = (
    "✨ **Salut magicien des fichiers !** ✨\n\n"
    "Je suis **Auto Rename Bot** 🪄, ton assistant magique de renommage de fichiers !\n\n"
    "🔥 **Pourquoi tu vas m'adorer :**\n"
    "- Renomme les fichiers avec ✨ éclat et précision\n"
    "- Super rapide ⚡ et sécurisé 🔒\n"
    "- Supporte TOUS les types de fichiers ! 📂🎵🎬\n\n"
    "Envoie-moi juste un fichier et faisons de la magie ! 🎩\n\n"
    "🚀 **Astuce Pro :** Utilise /mode pour le mode ninja de renommage auto (doit ajouter /filters) !\n"
    "Besoin d'aide ? /help est là pour toi !\n\n"
    "🛸 **Propulsé par** [NAm](https://t.me/xspes)"
    )

    CANCEL_MESSAGE = "❗ Renommage annulé ! Pouf ! ✨ (Mises à jour bientôt !)"

    RENAME_NO_FILTER_MATCH = (
        "🔮 **Oups ! Aucune correspondance de filtre !**\n\n"
        "J'ai essayé d'utiliser des filtres mais je n'ai rien trouvé 🎩🐇\n"
        "Gère tes filtres avec /filters ✏️"
    )

    RENAME_FILTER_MATCH_USED = (
        "🎯 **Puissance des filtres activée !**\n"
        "J'utilise des filtres puisque tu n'as pas spécifié de nom\n"
        "Ajuste-les avec /filters ⚙️"
    )

    RENAME_NOFLTR_NONAME = (
        "📝 **AUCUN filtre trouvé !**\n\n"
        "Ajoute /filters 🎨 pour les filtres de renommage auto."
    )

    RENAME_CANCEL = "❌ Non, annulons ça ✌️"

    RENAMING_FILE = "🌀 **Transformation du fichier en cours...**"

    DL_RENAMING_FILE = "📥 **Téléchargement de ton trésor numérique...**"

    RENAME_ERRORED_REPORT = "💥 **Oups ! Quelque chose a cassé !** Signale ça s'il te plaît 🚨"

    RENAME_CANCEL_BY_USER = "🙅‍♂️ **Tu as agité la baguette d'annulation !** ✨"

    FLTR_ADD_LEFT_STR = "➕ Filtre ajouté : `<code>{{ text_1 }}</code>` **à GAUCHE**."
    FLTR_ADD_RIGHT_STR = (
        "➕ Filtre ajouté : `<code>{{ text_1 }}</code>` **à DROITE**."
    )
    FLTR_RM_STR = "❌ Filtre supprimé : `<code>{{ text_1 }}</code>`."
    FLTR_REPLACE_STR = (
        "🔄 Filtre remplacé : `<code>{{ text_1 }}</code>` → `<code>{{ text_2 }}</code>`."
    )

    CURRENT_FLTRS = "🎛️ **Ton Tableau de Bord des Filtres :**"
    ADD_FLTR = "➕ Ajouter Filtre"
    RM_FLTR = "❌ Supprimer Filtre"

    FILTERS_INTRO = (
        "🛠 **Guide des Filtres :**\n"
        "Il y a 3 types de filtres :\n\n"
        "🔄 **Filtre de Remplacement :** Remplace un mot par un autre.\n"
        "➕ **Filtre d'Addition :** Ajoute un mot au début ou à la fin.\n"
        "❌ **Filtre de Suppression :** Supprime un mot du nom de fichier."
    )

    ADD_REPLACE_FLTR = "➕ Ajouter Filtre de Remplacement"
    ADD_ADDITION_FLTR = "➕ Ajouter Filtre d'Addition"
    ADD_REMOVE_FLTR = "➕ Ajouter Filtre de Suppression"
    BACK = "🔙 Retour"

    REPALCE_FILTER_INIT_MSG = "✍️ Envoie le format : `<code>quoi_remplacer | remplacement</code>` ou /ignore pour revenir."

    NO_INPUT_FROM_USER = "🤷‍♂️ **Criquets...** Aucune entrée détectée !"
    INPUT_IGNORE = "👍 **Ignoré !**"
    WRONG_INPUT_FORMAT = "🤦‍♂️ **Oups !** Mauvais format ! Vérifie le format fourni et réessaye !"
    REPLACE_FILTER_SUCCESS = (
        "✅ **Filtre de remplacement ajouté :**\n" "`'{{ text_1 }}'` → `'{{ text_2 }}'`"
    )

    ADDITION_FILTER_INIT_MSG = (
        "✍️ Entre le texte à ajouter entre `<code>|</code>`\n"
        "Exemple : `<code>| texte à ajouter |</code>`\n"
        "ou /ignore pour revenir."
    )

    ADDITION_FILTER_SUCCESS_LEFT = (
        "✅ Filtre ajouté : `<code>{{ text_1 }}</code>` **à GAUCHE**."
    )
    ADDITION_FILTER_SUCCESS_RIGHT = (
        "✅ Filtre ajouté : `<code>{{ text_1 }}</code>` **à DROITE**."
    )

    ADDITION_LEFT = "🔄 Addition à GAUCHE"
    ADDITION_RIGHT = "🔄 Addition à DROITE"

    ADDITION_POSITION_PROMPT = "🧙‍♂️ **Où veux-tu ajouter le texte ?**"

    REMOVE_FILTER_INIT_MSG = (
        "✍️ Entre le texte que tu veux supprimer ou /ignore pour revenir."
    )

    REMOVE_FILTER_SUCCESS = (
        "✅ **Filtre de suppression ajouté :** `<code>{{ text_1 }}</code>` sera supprimé."
    )

    RENAME_THEMES_DOWNLOADING = [
        "🎩 Téléchargement complet ! Préparation de la magie...",
        "📦 Fichier acquis ! Prêt pour la sorcellerie de nommage...",
        "✨ Téléchargement réussi ! Les incantations commencent...",
        "⚡ Données sécurisées ! Moteurs de renommage en marche...",
        "💾 Fichier capturé ! Prêt pour une renaissance glorieuse..."
    ]

    RENAME_THEMES_UPLOADING = [
        "🚀 **Décollage !** Fichier renommé lancé !",
        "🎉 **Ta-da !** Ton fichier renommé est prêt !",
        "📤 Upload complet ! Profite de ton chef-d'œuvre !",
        "🌟 Métamorphose du fichier terminée !",
        "🏁 Course terminée ! Ton fichier a franchi la ligne d'arrivée !"
    ]

    RENAME_THEMES_DOWNLOAD_CANCELLED = [
        "🛑 **Abort !** Sortilège de téléchargement interrompu !",
        "🚧 Oups ! Tu as arrêté le train du téléchargement !",
        "🎭 Le spectacle est terminé avant d'avoir commencé !",
        "📵 Connexion de téléchargement terminée !",
        "👋 Tu as abandonné le téléchargement ! Au revoir !"
    ]

    RENAME_THEMES_UPLOAD_CANCELLED = [
        "✋ **Attends !** Upload arrêté en plein vol !",
        "🚫 Pas de livraison aujourd'hui ! Upload annulé !",
        "🌪️ Tornade d'upload dissipée !",
        "📴 Connexion perdue dans le vide !",
        "🤷‍♂️ Tu as changé d'avis ! Upload avorté !"
    ]

    REPLY_TO_MEDIA = "📎 **Psst !** Réponds `/rename` à un fichier !"

    RENAME_DOWNLOADING_DONE = random.choice(RENAME_THEMES_DOWNLOADING)
    RENAME_UPLOADING_DONE = random.choice(RENAME_THEMES_UPLOADING)
    RENAME_CANCEL_BY_USER = random.choice(RENAME_THEMES_DOWNLOAD_CANCELLED)
    RENAME_UPLOAD_CANCELLED_BY_USER = random.choice(RENAME_THEMES_UPLOAD_CANCELLED)
    RENAME_ERRORED = "💥 **Kaboom !** Sortilège de renommage échoué !"

    DOWNLOADING_THE_FILE = "📥 **Récupération de ton fichier...**"
    UPLOADING_THE_FILE = "📤 **Lancement :** `{{ new_file_name }}` 🚀"

    TRACK_MESSAGE_EXECUTION_START = (
        "🚀 **Mission de Renommage Lancée**\n"
        "🆔 ID Mission : `{{ uid }}`\n\n"
        "👤 **Agent :** @{{ username }}\n"
        "📛 **Nom de Code :** {{ name }}\n"
        "🪪 **ID :** `{{ user_id }}`\n"
        "📜 **Fichier :** `{{ file_name }}`\n\n"
        "`⚡ Hyperdrive engagé !`"
    )
    
    TRACK_MESSAGE_ADDED_RENAME = (
        "📥 **Mission de Renommage en File d'Attente**\n\n"
        "👤 **Agent :** @{{ username }}\n"
        "📛 **Nom de Code :** {{ name }}\n"
        "🪪 **ID :** `{{ user_id }}`\n\n"
        "`⏳ En attente de déploiement...`"
    )

    CAPTION_FOOT_NOTE = (
        "💡 **Astuce Pro :** Utilise /setcaption pour ajouter du style !\n"
        "✨ Utilise `/setcaption {file_name}` pour auto-remplir le nom de fichier dans la légende !"
    )

    DELETE_CAPTION = "🗑️ Supprimer Légende"
    CLOSE = "🚪 Quitter"

    CAPTION_CURRENT = "📝 **Légende Actuelle :** {{ caption }}"
    CAPTION_NOT_SET = "🫗 **Légende vide !** Si solitaire..."
    CAPTION_SET = "✅ **Nouvelle Légende :** {{ caption }}"
    CAPTION_DELETED = "🗑️ **Légende supprimée avec succès.**"

    RENAME_ADDED_TO_QUEUE = (
        "📊 **Renommage en File d'Attente**\n"
        "🆔 **ID DC :** {{ dc_id }}\n"
        "📦 **ID Media :** {{ media_id }}\n\n"
        "`⏳ Patience, jeune padawan...`"
    )

    RENAME_QUEUE_STATUS = (
        "📈 **Statistiques de File :**\n"
        "📊 **Total des Tâches :** {{ total_tasks }}\n"
        "⚡ **Capacité :** {{ queue_capacity }}\n"
        "⏳ **En Traitement :** {{ current_task }}"
    )

    RENAME_QUEUE_USER_STATUS = (
        "{% if is_executing %}\n"
        "⚡ **Ton fichier est en cours de magie !**\n"
        "🆔 **ID Tâche :** {{ task_id }}\n"
        "{% endif %}"
        "{% if is_pending %}\n"
        "⏳ **Ta place dans la file :** {{ task_number }}\n"
        "🆔 **ID Tâche :** {{ task_id }}\n"
        "{% endif %}"
    )

    USER_KICKED = "👢 **Tu as été viré !** Pas de bot pour toi !"
    USER_NOT_PARTICIPANT = (
        "🔒 **Alerte Club Secret !**\n\n"
        "Rejoins notre canal pour débloquer la magie !\n\n"
        "`🦄 Seules les licornes au-delà de ce point`"
    )
    
    JOIN_CHANNEL = "🔗 Rejoindre le Club Secret"

    MODE_INITIAL_MSG = (
        "🎛️ **Sélecteur de Mode de Sortie :**\n\n"
        "1️⃣ **Conserver le format original**"
        "{% if mode == udb.MODE_SAME_AS_SENT %} ✅{% endif %}\n"
        "2️⃣ **Forcer le mode document**"
        "{% if mode == udb.MODE_AS_DOCUMENT %} ✅{% endif %}\n"
        "3️⃣ **Mode média général**"
        "{% if mode == udb.MODE_AS_GMEDIA %} ✅{% endif %}\n\n"
        "✨ **Style de Renommage :**\n"
        "🅰️ **Renommage par commande**"
        "{% if command_mode == udb.MODE_RENAME_WITH_COMMAND %} ✅{% endif %}\n"
        "🅱️ **Renommage automatique**"
        "{% if command_mode == udb.MODE_RENAME_WITHOUT_COMMAND %} ✅{% endif %}"
    )

    MODE_SET_0 = "1️⃣ Mode OG"
    MODE_SET_1 = "2️⃣ Mode Document"
    MODE_SET_2 = "3️⃣ Mode Média"
    COMMAND_MODE_SET_3 = "🅰️ Commande"
    COMMAND_MODE_SET_4 = "🅱️ Auto"

    THUMB_REPLY_TO_MEDIA = "🖼️ **Réponds à une image** pour la définir comme miniature"
    THUMB_SET_SUCCESS = "✅ **Miniature verrouillée !**"
    THUMB_NOT_FOUND = "🕵️‍♂️ **Aucune miniature détectée !**"
    THUMB_CLEARED = "🧹 **Miniature balayée !**"

    HELP_STR = (
        "📚 **Livre de Sortilèges Magiques :**\n"
        "`{{ startcmd }}` - Vérifie si je suis en vie ! 💓\n"
        "`{{ renamecmd }}` - Renomme les fichiers comme un boss ! 🎩\n"
        "`{{ filterscmd }}` - Personnalise tes filtres de renommage ! ✨\n"
        "`{{ setthumbcmd }}` - Définir une miniature permanente ! 🖼️\n"
        "`{{ getthumbcmd }}` - Regarde la miniature actuelle ! 👀\n"
        "`{{ clrthumbcmd }}` - Supprime la miniature ! 🗑️\n"
        "`{{ modecmd }}` - Changer les modes de sortie :\n"
        "   - 📝 Format original\n"
        "   - 📂 Forcer document\n"
        "   - 🎥 Mode média\n\n"
        "   Changer les styles de renommage :\n"
        "   - 🏷️ Basé sur commande\n"
        "   - 🤖 Renommage auto (doit ajouter /filters)\n\n"
        "`{{ queuecmd }}` - Vérifie la file de renommage 📊\n"
        "`{{ setcaptioncmd }}` - Définir des légendes fancy 🎨\n"
        "`{{ helpcmd }}` - Ce livre magique ! 📖\n"
        "`{{ pingcmd }}` - Ping-pong ! 🏓\n"
        "`{{ infocmd }}` - Spécifications du bot ! 🤖\n"
        "`{{ profilecmd }}` - Tes stats ! 📈\n"
        "`{{ statuscmd }}` - Signes vitaux du bot ! 💓\n"
        "`{{ statscmd }}` - Chiffres globaux ! 🌍\n"
        "`{{ broadcastcmd }}` - Méga-annonce ! 📢\n"
        "`{{ leaderboardcmd }}` - Top utilisateurs ! 🏆\n"
        "`{{ setlanguagecmd }}` - Changer de langue ! 🌐"
    )

    CURRENT_LOCALE = "🌍 **Ta langue :** {{ user_locale }}"
