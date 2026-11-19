USE cine_emocion;

-- Usuario de prueba: demo / demo1234
INSERT IGNORE INTO users (username, password_hash) VALUES ('demo', 'scrypt:32768:8:1$F9O5P268dhMPvQvW$1d8c9451f1019f09f318d765b096f24bf29d53865544d5d5dab9d0fca383ce2a88b36897e840511eaf36542b0d8f3b8da01a4f721c873713643465a38d0ae558');

-- Preferencias de ejemplo del usuario demo: le gustan Drama, Comedia y Romance; evita Terror
INSERT IGNORE INTO user_genres (user_id, genre_id, tipo)
SELECT id, g.genre_id, g.tipo FROM users
JOIN (SELECT 18 AS genre_id, 'gusta' AS tipo UNION ALL SELECT 35, 'gusta'
      UNION ALL SELECT 10749, 'gusta' UNION ALL SELECT 27, 'evita') g
WHERE username = 'demo';
