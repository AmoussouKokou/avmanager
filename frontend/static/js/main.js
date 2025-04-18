function toggleOptions(element) {
    const allOptions = document.querySelectorAll('.option-block');
    const targetId = element.getAttribute('data-target');
    const targetBlock = document.getElementById(targetId);

    // Fermer tous les autres
    allOptions.forEach(opt => {
        if (opt !== targetBlock) {
            opt.style.display = 'none';
        }
    });

    // Basculer l'affichage du bloc cliqué
    if (targetBlock.style.display === 'block') {
        targetBlock.style.display = 'none';
    } else {
        targetBlock.style.display = 'block';
    }
}


// function closeAllOptions() {
//     const allOptions = document.querySelectorAll('.option-block');
//     allOptions.forEach(opt => opt.style.display = 'none');
// }

// function toggleYoutubeOptions() {
//     const options = document.getElementById('youtube-options');
//     if (options.style.display === 'none') {
//         options.style.display = 'block';
//     } else {
//         options.style.display = 'none';
//     }
// }
// function toggleYoutubeOptions() {
//     const target = document.getElementById('youtube-options');
//     const isVisible = target.style.display === 'block';
//     closeAllOptions();
//     target.style.display = isVisible ? 'none' : 'block';
// }

function handleYoutubeDownload(event) {
    event.preventDefault();
    const link = document.getElementById('youtube-link').value;
    alert("Téléchargement demandé pour : " + link);

    // Tu peux ensuite remplacer cette alerte par un appel réel à ton backend Flask
}

// function toggleMp4ToMp3Options() {
//     const target = document.getElementById('mp4-to-mp3-options');
//     const isVisible = target.style.display === 'block';
//     closeAllOptions();
//     target.style.display = isVisible ? 'none' : 'block';
// }

// function toggleMp4ToMp3Options() {
//     const options = document.getElementById('mp4-to-mp3-options');
//     options.style.display = (options.style.display === 'none') ? 'block' : 'none';
// }



function handleMp4ToMp3(event) {
    event.preventDefault();
    const file = document.getElementById('mp4-file').files[0];

    if (file) {
        alert("Conversion demandée pour : " + file.name);
        // Tu pourras remplacer cette alerte par un envoi réel au backend
    } else {
        alert("Veuillez sélectionner un fichier MP4.");
    }
}

function handleMp3ToMp4(event) {
    event.preventDefault(); // Empêche le rechargement de la page

    const mp3File = document.getElementById("mp3File").files[0];
    const imageFile = document.getElementById("imageFile").files[0];

    if (!mp3File || !imageFile) {
        alert("Veuillez sélectionner un fichier MP3 et une image.");
        return;
    }

    // Simule le traitement (tu pourras remplacer par une vraie requête plus tard)
    console.log("Fichier MP3 :", mp3File.name);
    console.log("Image sélectionnée :", imageFile.name);
    alert("Conversion simulée : " + mp3File.name + " + " + imageFile.name);
}

function handleJoinMp3(event) {
    event.preventDefault(); // Empêche le rechargement de la page

    const input = event.target.querySelector('input[type="file"]');
    const files = input.files;

    if (files.length < 2) {
        alert("Veuillez sélectionner au moins deux fichiers MP3 à joindre.");
        return;
    }

    // Pour l'instant, juste une confirmation visuelle
    let fileNames = Array.from(files).map(file => file.name).join(", ");
    alert("Fichiers sélectionnés pour la jointure : " + fileNames);

    // Ici tu pourras ajouter ta logique pour envoyer les fichiers au serveur ou les traiter localement
}

function handleCutMp3(event) {
    event.preventDefault();

    const file = document.getElementById('cutMp3File').files[0];
    const start = document.getElementById('cutStart').value.trim();
    const end = document.getElementById('cutEnd').value.trim();

    if (!file || !start || !end) {
        alert('Veuillez remplir tous les champs.');
        return;
    }

    console.log("Fichier MP3 :", file.name);
    console.log("Début :", start);
    console.log("Fin :", end);

    // TODO : Ajouter la logique de traitement réel (backend ou WebAssembly par ex.)
    alert("La découpe de l'extrait entre " + start + " et " + end + " sera traitée.");
}


// Afficher le nom du fichier sélectionné
document.addEventListener('DOMContentLoaded', function() {
    const fileInput = document.getElementById('mp4-file');
    const fileName = document.getElementById('file-name');

    if (fileInput) {
        fileInput.addEventListener('change', function() {
            if (fileInput.files.length > 0) {
                fileName.value = fileInput.files[0].name;
            } else {
                fileName.value = '';
            }
        });
    }
});