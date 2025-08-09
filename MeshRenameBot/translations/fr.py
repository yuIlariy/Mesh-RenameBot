from dataclasses import dataclass
import random

@dataclass
class FrenchTranslations:
    LANGUAGE_NAME = "Français"
    LANGUAGE_CODE = "fr"

    WRONG_VALUE_ERROR = "❌ Valeur invalide entrée pour la variable {{ variable_name }}."

    START_MSG = (
    "Bonjour ! 👋\n"
    "Je suis **Bot de Renommage Auto**, votre assistant pour renommer facilement des fichiers sur Telegram.\n\n"
    "✨ **Fonctionnalités :**\n"
    "- Renommer des fichiers avec noms et extensions personnalisés\n"
    "- Rapide, sécurisé et facile à utiliser\n"
    "- Prend en charge de nombreux types de fichiers\n\n"
    "Envoyez-moi simplement un fichier et je vous guiderai !\n\n"
    "Commençons ! Utilisez /mode pour activer le renommage auto, **Renommer sans commande**🚀\n"
    "Envoyez /help pour en savoir plus.\n\n"
    "🚀 **Propulsé par** [NAm](https://t.me/xspes)"
    )

    CANCEL_MESSAGE = "⚠️ Le renommage a été **annulé**. Mise à jour prochainement."

    RENAME_NO_FILTER_MATCH = (
        "🚫 **AUCUN FILTRE CORRESPONDANT - ANNULATION DU RENOMMAGE**\n\n"
        "🔍 Utilisation des filtres car aucun nom n'a été spécifié.\n"
        "👻 Gérez vos filtres avec /filters."
    )

    RENAME_FILTER_MATCH_USED = (
        "✅ Utilisation des filtres car aucun nom n'a été spécifié.\n"
        "👻 Gérez vos filtres avec /filters."
    )

    RENAME_NOFLTR_NONAME = (
        "✍️ Entrez le nouveau nom de fichier au format :\n"
        "```/rename mon_nouveau_fichier.extension```\n"
        "ou utilisez `/filters` pour configurer les filtres."
    )

    RENAME_CANCEL = "❌ Annuler ce renommage."

    RENAMING_FILE = "🔄 Renommage du fichier... Veuillez patienter."

    DL_RENAMING_FILE = "📥 Téléchargement du fichier... Veuillez patienter."

    RENAME_ERRORED_REPORT = "❗ Erreur lors du téléchargement. Signalez ce problème."

    RENAME_CANCEL_BY_USER = "🚫 **Annulé par l'utilisateur.**"

    FLTR_ADD_LEFT_STR = "➕ Filtre ajouté : `<code>{{ text_1 }}</code>` **à GAUCHE**."
    FLTR_ADD_RIGHT_STR = (
        "➕ Filtre d'ajout : `<code>{{ text_1 }}</code>` **à DROITE**."
    )
    FLTR_RM_STR = "❌ Supprimer le filtre : `<code>{{ text_1 }}</code>`."
    FLTR_REPLACE_STR = (
        "🔄 Remplacer le filtre : `<code>{{ text_1 }}</code>` → `<code>{{ text_2 }}</code>`."
    )

    CURRENT_FLTRS = "⚙️ **Vos Filtres Actuels :**"
    ADD_FLTR = "➕ Ajouter un filtre"
    RM_FLTR = "❌ Supprimer un filtre"

    FILTERS_INTRO = (
        "🛠 **Guide des Filtres :**\n"
        "Il existe 3 types de filtres :\n\n"
        "🔄 **Filtre de Remplacement :** Remplacer un mot par un autre.\n"
        "➕ **Filtre d'Ajout :** Ajouter un mot au début ou à la fin.\n"
        "❌ **Filtre de Suppression :** Supprimer un mot du nom de fichier."
    )

    ADD_REPLACE_FLTR = "➕ Ajouter un filtre de remplacement"
    ADD_ADDITION_FLTR = "➕ Ajouter un filtre d'ajout"
    ADD_REMOVE_FLTR = "➕ Ajouter un filtre de suppression"
    BACK = "🔙 Retour"

    REPALCE_FILTER_INIT_MSG = "✍️ Envoyez le format : `<code>à_remplacer | remplacement</code>` ou `/ignore` pour revenir."

    NO_INPUT_FROM_USER = "⚠️ Aucune entrée reçue de votre part."
    INPUT_IGNORE = "✅ **Ignoré**."
    WRONG_INPUT_FORMAT = "❌ Format invalide. Vérifiez le format fourni."
    REPLACE_FILTER_SUCCESS = (
        "✅ **Filtre de remplacement ajouté :**\n" "`'{{ text_1 }}'` → `'{{ text_2 }}'`"
    )

    ADDITION_FILTER_INIT_MSG = (
        "✍️ Entrez le texte à ajouter entre `<code>|</code>`\n"
        "Exemple : `<code>| texte à ajouter |</code>`\n"
        "ou `/ignore` pour revenir."
    )

    ADDITION_FILTER_SUCCESS_LEFT = (
        "✅ Filtre ajouté : `<code>{{ text_1 }}</code>` **à GAUCHE**."
    )
    ADDITION_FILTER_SUCCESS_RIGHT = (
        "✅ Filtre ajouté : `<code>{{ text_1 }}</code>` **à DROITE**."
    )

    ADDITION_LEFT = "🔄 Ajout à gauche"
    ADDITION_RIGHT = "🔄 Ajout à droite"

    ADDITION_POSITION_PROMPT = "📍 **Où voulez-vous ajouter le texte ?**"

    REMOVE_FILTER_INIT_MSG = (
        "✍️ Entrez le texte que vous souhaitez supprimer ou `/ignore` pour revenir."
    )

    REMOVE_FILTER_SUCCESS = (
        "✅ **Filtre de suppression ajouté :** `<code>{{ text_1 }}</code>` sera supprimé."
    )

    RENAME_THEMES_DOWNLOADING = [
        "✅ Téléchargement terminé. Lancement du renommage...",
        "📦 Fichier récupéré ! Prêt pour un nouveau nom...",
        "🪄 Téléchargement terminé. ✨ Commençons le renommage...",
        "🔧 Données acquises. Moteur de renommage en marche...",
        "💾 Sauvegardé et scellé. Maintenant, renommons avec style...",
    ]

    RENAME_THEMES_UPLOADING = [
        "✅ Tout renommé et prêt ! Téléversement terminé.",
        "🚀 Fichier renommé avec succès et publié.",
        "📤 Téléversement terminé. Votre chef-d'œuvre renommé est en ligne !",
        "🌟 Renommage finalisé. Livré dans l'univers !",
        "📁 Tâche terminée. Le fichier est renommé.",
    ]

    RENAME_THEMES_DOWNLOAD_CANCELLED = [
        "🛑 Téléchargement interrompu. Le rêve de renommage s'évanouit...",
        "🚫 Vous avez débranché. Téléchargement annulé.",
        "❌ Opération annulée en cours. Fichier non récupéré.",
        "📴 Renommage annulé pendant le téléchargement. Mission avortée.",
        "👋 Utilisateur a annulé pendant le téléchargement. Adieu, fichier.",
    ]

    RENAME_THEMES_UPLOAD_CANCELLED = [
        "🛑 Téléversement annulé. Fichier reste local et ignoré.",
        "🚫 Renommage inversé. Téléversement terminé.",
        "❌ Étape finale interrompue. Renommage abandonné.",
        "📴 Téléversement refusé. Fichier renommé n'ira nulle part.",
        "👋 Utilisateur a dit 'non' pendant le téléversement. Fichier retiré.",
    ]

    REPLY_TO_MEDIA = "📂 Répondez `/rename` à un fichier média."

    RENAME_DOWNLOADING_DONE = random.choice(RENAME_THEMES_DOWNLOADING)
    RENAME_UPLOADING_DONE = random.choice(RENAME_THEMES_UPLOADING)
    RENAME_CANCEL_BY_USER = random.choice(RENAME_THEMES_DOWNLOAD_CANCELLED)
    RENAME_UPLOAD_CANCELLED_BY_USER = random.choice(RENAME_THEMES_UPLOAD_CANCELLED)
    RENAME_ERRORED = "❗ Erreur lors du processus de renommage."

    DOWNLOADING_THE_FILE = "📥 Téléchargement du fichier"
    UPLOADING_THE_FILE = "📤 Téléversement du fichier : **{{ new_file_name }}**"

    TRACK_MESSAGE_EXECUTION_START = (
        "🚀 **Exécution Commencée pour la Tâche de Renommage**\n"
        "🆔 ID Tâche : `{{ uid }}`\n\n"
        "👤 **Nom d'utilisateur :** @{{ username }}\n"
        "📛 **Nom :** {{ name }}\n"
        "🆔 **ID Utilisateur :** `<code>{{ user_id }}</code>`\n"
        "📂 **Nom du Fichier :** `<code>{{ file_name }}</code>`"
    )
    
    TRACK_MESSAGE_ADDED_RENAME = (
        "✅ **Tâche de Renommage Ajoutée**\n\n"
        "👤 **Nom d'utilisateur :** @{{ username }}\n"
        "📛 **Nom :** {{ name }}\n"
        "🆔 **ID Utilisateur :** `<code>{{ user_id }}</code>`"
    )

    CAPTION_FOOT_NOTE = (
        "☄️ **NOTE :** Vous pouvez définir la légende avec `/setcaption` suivi de votre texte.\n"
        "📂 Utilisez `<code>{file_name}</code>` pour insérer dynamiquement le nom du fichier renommé."
    )

    DELETE_CAPTION = "🗑 Supprimer la légende"
    CLOSE = "❌ Fermer"

    CAPTION_CURRENT = "📝 **Votre Légende Actuelle :** {{ caption }}"
    CAPTION_NOT_SET = "⚠️ **Aucune légende définie.**"
    CAPTION_SET = "✅ **Légende mise à jour :** {{ caption }}"
    CAPTION_DELETED = "🗑 **Légende supprimée avec succès.**"

    RENAME_ADDED_TO_QUEUE = (
        "📥 **Tâche de Renommage Ajoutée à la File**\n"
        "🆔 **ID DC :** {{ dc_id }}\n"
        "👻 **ID Média :** {{ media_id }}"
    )

    RENAME_QUEUE_STATUS = (
        "📊 **État de la File de Renommage :**\n"
        "☄️ **Total des Tâches en File :** {{ total_tasks }}\n"
        "⚡ **Capacité de la File :** {{ queue_capacity }}\n"
        "⏳ **En Cours de Traitement :** {{ current_task }}"
    )

    RENAME_QUEUE_USER_STATUS = (
        "{% if is_executing %}\n"
        "⚡ **Votre Tâche est en Cours d'Exécution**\n"
        "🆔 **ID Tâche :** {{ task_id }}\n"
        "{% endif %}"
        "{% if is_pending %}\n"
        "⏳ **Position de Votre Tâche dans la File :** {{ task_number }}\n"
        "🆔 **ID Tâche :** {{ task_id }}\n"
        "{% endif %}"
    )

    USER_KICKED = "👻 **Vous avez été retiré du chat. Vous ne pouvez pas utiliser ce bot.**"
    USER_NOT_PARTICIPANT = "👻 **Rejoignez le chat requis pour utiliser ce bot.**"
    JOIN_CHANNEL = "🔗 Rejoindre la Chaîne des Mises à Jour"

    MODE_INITIAL_MSG = (
        "📂 **Mode de Sortie des Fichiers :**\n\n"
        "1️⃣ **Même format qu'envoyé**"
        "{% if mode == udb.MODE_SAME_AS_SENT %} ✅{% endif %}\n"
        "2️⃣ **Forcer en Document**"
        "{% if mode == udb.MODE_AS_DOCUMENT %} ✅{% endif %}\n"
        "3️⃣ **Téléverser comme Média Général**"
        "{% if mode == udb.MODE_AS_GMEDIA %} ✅{% endif %}\n\n"
        "👻 **Sélectionnez le mode de renommage :**\n"
        "🅰️ **Renommer avec commande**"
        "{% if command_mode == udb.MODE_RENAME_WITH_COMMAND %} ✅{% endif %}\n"
        "🅱️ **Renommer sans commande**"
        "{% if command_mode == udb.MODE_RENAME_WITHOUT_COMMAND %} ✅{% endif %}"
    )

    MODE_SET_0 = "1️⃣"
    MODE_SET_1 = "2️⃣"
    MODE_SET_2 = "3️⃣"
    COMMAND_MODE_SET_3 = "🅰️"
    COMMAND_MODE_SET_4 = "🅱️"

    THUMB_REPLY_TO_MEDIA = "📸 Répondez à une image pour la définir comme miniature."
    THUMB_SET_SUCCESS = "✅ **Miniature définie avec succès.**"
    THUMB_NOT_FOUND = "⚠️ **Aucune miniature trouvée.**"
    THUMB_CLEARED = "🗑 **Miniature supprimée avec succès.**"

    HELP_STR = (
        "📖 **Commandes du Bot :**\n"
        "`{{ startcmd }}` - ✅ Vérifier si le bot fonctionne\n"
        "`{{ renamecmd }}` - ✍️ Répondez à un média avec `/rename nomfichier.extension` pour le renommer\n"
        "`{{ filterscmd }}` - ⚙️ Gérer vos filtres de renommage\n"
        "`{{ setthumbcmd }}` - 📷 Définir une miniature permanente (répondez à une image)\n"
        "`{{ getthumbcmd }}` - 📸 Obtenir la miniature actuelle\n"
        "`{{ clrthumbcmd }}` - ❌ Supprimer la miniature définie\n"
        "`{{ modecmd }}` - 🔄 Basculer entre 3 modes de sortie :\n"
        "    - 📝 Même format qu'envoyé\n"
        "    - 📂 Document forcé\n"
        "    - 🎥 Média Général (vidéo/audio streamable)\n\n"
        "    🔄 Basculer entre modes de renommage :\n"
        "    - 🏷 Renommer **avec commande**\n"
        "    - ✨ Renommer **sans commande/auto**\n\n"
        "`{{ queuecmd }}` - 📊 Voir l'état de la file de renommage\n"
        "`{{ setcaptioncmd }}` - 📝 Définir une légende pour les fichiers renommés\n"
        "`{{ helpcmd }}` - 📖 Afficher ce message d'aide\n"
        "`{{ pingcmd }}` - 🎈Ping le Bot\n"
        "`{{ infocmd }}` - 🧑‍💻 Voir les infos du bot\n"
        "`{{ profilecmd }}` - ☄️ Vos statistiques d'utilisation\n"
        "`{{ statuscmd }}` - 🗿 État du Bot\n"
        "`{{ statscmd }}` - 👻 Statistiques globales du bot\n"
        "`{{ broadcastcmd }}` - ☄️Faire un broadcast\n"
        "`{{ leaderboardcmd }}` - 👻 Classement des utilisateurs\n"
        "`{{ setlanguagecmd }}` - 🌐 Changer la langue du bot"
    )

    CURRENT_LOCALE = "🌐 **Votre langue actuelle :** {{ user_locale }}"



