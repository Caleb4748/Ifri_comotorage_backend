from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    ROLE_CHOICES = (
        ('PASSAGER', _('Passager')),
        ('CONDUCTEUR', _('Conducteur')),
    )

    # Redéfinir email pour qu'il soit unique et requis
    email = models.EmailField(_('email address'), unique=True)
    
    # Remplacer username par email comme champ d'identification principal
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name'] # username est toujours requis par AbstractUser, mais email est le login

    telephone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message=_("Le numéro de téléphone doit être entré au format: '+999999999'. Jusqu'à 15 chiffres autorisés.")
    )
    telephone = models.CharField(validators=[telephone_regex], max_length=17, blank=True, null=True, unique=True, help_text=_("Numéro de téléphone au format international."))
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='PASSAGER')
    
    photo_profil = models.ImageField(upload_to='photos_profil/', null=True, blank=True, help_text=_("Photo de profil de l'utilisateur."))
    
    adresse_geographique = models.CharField(max_length=255, blank=True, null=True, help_text=_("Adresse géographique de l'utilisateur."))
    
    horaires_habituels = models.TextField(blank=True, null=True, help_text=_("Horaires habituels de trajet (ex: Lun-Ven 8h-18h)."))
    
    informations_vehicule = models.TextField(blank=True, null=True, help_text=_("Informations sur le véhicule (pour les conducteurs). Marque, modèle, couleur, etc."))

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if self.role == 'PASSAGER':
            self.informations_vehicule = None # Les passagers ne peuvent pas avoir d'infos véhicule
        super().save(*args, **kwargs)