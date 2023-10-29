# Utilisation de l'image officielle Nginx
FROM nginx:latest

# Supprimer le fichier de configuration par défaut de Nginx
RUN rm /etc/nginx/conf.d/default.conf

# Copier le fichier de configuration Nginx personnalisé dans le conteneur
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Exposer le port 80 (HTTP)
EXPOSE 80

# Exposer le port 443 (HTTPS)
EXPOSE 443

# Commande pour lancer Nginx en mode détaché
CMD ["nginx", "-g", "daemon off;"]

