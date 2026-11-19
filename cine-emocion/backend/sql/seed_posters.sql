USE cine_emocion;

-- Asigna a cada pelicula su poster (backend/static/posters/<id>.jpg)
UPDATE movies SET poster_url = CONCAT('/static/posters/', id, '.jpg') WHERE poster_url IS NULL;
