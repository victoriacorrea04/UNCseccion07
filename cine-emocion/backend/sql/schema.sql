CREATE DATABASE IF NOT EXISTS cine_emocion CHARACTER SET utf8mb4;
USE cine_emocion;

DROP TABLE IF EXISTS user_genres;
DROP TABLE IF EXISTS searches;
DROP TABLE IF EXISTS emotion_genres;
DROP TABLE IF EXISTS movie_genres;
DROP TABLE IF EXISTS emotions;
DROP TABLE IF EXISTS genres;
DROP TABLE IF EXISTS movies;

CREATE TABLE genres (
  id INT PRIMARY KEY,              -- usamos el mismo id que TMDB
  name VARCHAR(50) NOT NULL
);

CREATE TABLE movies (
  id INT AUTO_INCREMENT PRIMARY KEY,
  tmdb_id INT UNIQUE NULL,
  title VARCHAR(200) NOT NULL,
  overview TEXT,
  rating DECIMAL(3,1) NOT NULL DEFAULT 0,
  release_year SMALLINT,
  poster_url VARCHAR(300)
);

-- Relacion N:M peliculas <-> generos
CREATE TABLE movie_genres (
  movie_id INT NOT NULL,
  genre_id INT NOT NULL,
  PRIMARY KEY (movie_id, genre_id),
  FOREIGN KEY (movie_id) REFERENCES movies(id) ON DELETE CASCADE,
  FOREIGN KEY (genre_id) REFERENCES genres(id) ON DELETE CASCADE
);

CREATE TABLE emotions (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(30) NOT NULL UNIQUE,
  label VARCHAR(50) NOT NULL,
  emoji VARCHAR(10)
);

-- Relacion N:M emociones <-> generos (que generos recomendar para cada emocion)
CREATE TABLE emotion_genres (
  emotion_id INT NOT NULL,
  genre_id INT NOT NULL,
  PRIMARY KEY (emotion_id, genre_id),
  FOREIGN KEY (emotion_id) REFERENCES emotions(id) ON DELETE CASCADE,
  FOREIGN KEY (genre_id) REFERENCES genres(id) ON DELETE CASCADE
);

-- Usuarios del login (la contrasena se guarda siempre con hash).
-- No se hace DROP de users para no perder las cuentas al recrear el esquema.
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(50) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Preferencias del cuestionario: generos que le gustan o que prefiere evitar
CREATE TABLE user_genres (
  user_id INT NOT NULL,
  genre_id INT NOT NULL,
  tipo ENUM('gusta', 'evita') NOT NULL,
  PRIMARY KEY (user_id, genre_id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (genre_id) REFERENCES genres(id) ON DELETE CASCADE
);

-- Historial de lo que escriben los usuarios (user_id: quien lo registro, si habia iniciado sesion)
CREATE TABLE searches (
  id INT AUTO_INCREMENT PRIMARY KEY,
  text VARCHAR(500) NOT NULL,
  emotion_id INT NOT NULL,
  user_id INT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (emotion_id) REFERENCES emotions(id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL
);
