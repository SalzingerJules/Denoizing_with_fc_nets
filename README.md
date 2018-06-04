# Denoizing_with_fc_nets

ARTICLE 1 :

AVANTAGES :
évite de flouter les petits détails en forçant le réseau à garder un faible niveau d'abstraction
facile à entraîner car peu profond
extraction de caractéristiques multi-échelles
court-circuit des étapes de denoising pour la reconstruction d'image => trois parties distinctes dans la réseau avec chacune son rôle particulier
entraînement intéressant en trois étapes, clean-to-clean, noisy-to-clean et adversarial noisy-to-clean

INCONVENIENTS :
très peu profond, donc peut-être sensible à une plus grand diversité de bruits ou d'images

DB :
TRAINING :
MIT Indoor dataset
Places dataset
 => 64*64 crop de 5000 images de chaque base, pixels normalisés entre 0 et 1
Bruitage : "random level of Gaussian noise"

TEST :
100 images de BSDS300 et 200 images de PascalVOC

VALIDATION :
7 images de références (utilisées dans "J. Portilla, V. Strela, M. J. Wainwright, and E. P. Simoncelli. Image denoising using scale mixtures of gaussians in the wavelet domain.")

Méthode de test : PSNR seul
