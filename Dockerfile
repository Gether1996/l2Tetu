# Utilisation d'une image de base Python
FROM python:3.11

# Répertoire de travail
WORKDIR /app

# Copier les fichiers requis dans le conteneur
COPY ./L2Tetu /app

# Installer les dépendances
RUN pip install -r /app/requirements.txt

# Exposer le port sur lequel votre application écoute
EXPOSE 8000

# Commande pour lancer votre application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
