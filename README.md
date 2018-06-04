# Denoizing_with_fc_nets

ARTICLE 1 :

AVANTAGES :
- évite de flouter les petits détails en forçant le réseau à garder un faible niveau d'abstraction
- facile à entraîner car peu profond
- extraction de caractéristiques multi-échelles
- court-circuit des étapes de denoising pour la reconstruction d'image => trois parties distinctes dans la réseau avec chacune son rôle particulier
- entraînement intéressant en trois étapes, clean-to-clean, noisy-to-clean et adversarial noisy-to-clean

INCONVENIENTS :
- très peu profond, donc peut-être sensible à une plus grand diversité de bruits ou d'images

DB :

TRAINING :

MIT Indoor dataset et Places dataset

 => 64*64 crop de 5000 images de chaque base, pixels normalisés entre 0 et 1
 
Bruitage : "random level of Gaussian noise"

TEST :

100 images de BSDS300 et 200 images de PascalVOC

VALIDATION :

7 images de références (utilisées dans "J. Portilla, V. Strela, M. J. Wainwright, and E. P. Simoncelli. Image denoising using scale mixtures of gaussians in the wavelet domain.")


Méthode de test : PSNR seul

ARTICLE 2

AVANTAGES :
- profondeur du modèle choisi pour obtenir un certain champ de vision
- les auteurs attribuent majoritairement la qualité de leurs résultats à l'utilisation des couches de batch normalisation et du "residual learning", c'est-à-dire la reconstitution du bruit plutôt que de l'image débruitée
- bonne capacité de généralisation à d'autres types de bruit, tout en gardant des résultats compétitifs dans le cas de bruit de niveau connu

INCONVENIENTS :
---

Tests : PSNR pour la plupart, SSIM un petit peu

DB :

TRAINING : 

NOIR ET BLANC

400 images (180*180) du Berkeley Segmentation Dataset (https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/bsds/)

Niveaux de bruits connus : sigma = 15, 25, 50  (We set the patch size as 40 * 40, and crop 128 * 1 600 patches to train the model.) ?

Blind Gaussian denoising : sigma in [0,55] (the patch size as 50 * 50. 128 * 3 000 patches are cropped to train the model) ?


COULEUR

432 color images from Berkeley segmentation dataset (and 128 * 3 000 patches of size 50 * 50 are cropped to train the model) ?

Noise levels :  [0; 55] 


TEST :

68 natural images from Berkeley segmentation dataset (BSD68)

color version of the BSD68
