-- Movies
INSERT INTO Movies (title, release_year, duration, description)
VALUES ('3 Idiots', 2009, 170, 'A story of friendship and following your passion.'),
       ('Dangal', 2016, 161, 'A father trains his daughters to become world-class wrestlers.');

-- Media
INSERT INTO Media (movie_id, media_type, url)
VALUES (1, 'Video', 'http://trailers.com/3idiots.mp4'),
       (1, 'Image', 'http://images.com/3idiots.jpg'),
       (2, 'Video', 'http://trailers.com/dangal.mp4');

-- Genres
INSERT INTO Genres (name) VALUES ('Comedy'), ('Drama'), ('Sports'), ('Biography');

-- Movie-Genre mapping
INSERT INTO MovieGenres (movie_id, genre_id)
VALUES (1, 1), (1, 2),   -- 3 Idiots -> Comedy, Drama
       (2, 2), (2, 3), (2, 4); -- Dangal -> Drama, Sports, Biography

-- Users
INSERT INTO Users (username, email)
VALUES ('rahul_k', 'rahul@example.com'),
       ('priya_s', 'priya@example.com');

-- Reviews
INSERT INTO Reviews (movie_id, user_id, rating, comment)
VALUES (1, 1, 9.0, 'Fun and inspiring movie!'),
       (2, 2, 9.5, 'Aamir Khan was outstanding, very motivating!');

-- Artists
INSERT INTO Artists (name, dob)
VALUES ('Aamir Khan', '1965-03-14'),
       ('Rajkumar Hirani', '1962-11-20'),
       ('Nitesh Tiwari', '1973-05-22'),
       ('Fatima Sana Shaikh', '1992-01-11'),
       ('Sanya Malhotra', '1992-02-25');

-- Skills
INSERT INTO Skills (skill_name) VALUES ('Acting'), ('Directing'), ('Writing'), ('Producing');

-- Artist Skills
INSERT INTO ArtistSkills (artist_id, skill_id)
VALUES (1, 1), (1, 4),        -- Aamir Khan -> Acting, Producing
       (2, 2), (2, 3),        -- Rajkumar Hirani -> Directing, Writing
       (3, 2), (3, 3),        -- Nitesh Tiwari -> Directing, Writing
       (4, 1), (5, 1);        -- Fatima & Sanya -> Acting

-- Roles
INSERT INTO Roles (role_name) VALUES ('Actor'), ('Director'), ('Writer'), ('Producer');

-- Artist-Movie-Roles
INSERT INTO MovieRoles (movie_id, artist_id, role_id)
VALUES (1, 1, 1),  -- Aamir acted in 3 Idiots
       (1, 2, 2),  -- Rajkumar Hirani directed 3 Idiots
       (1, 2, 3),  -- Rajkumar Hirani wrote 3 Idiots
       (2, 1, 1),  -- Aamir acted in Dangal
       (2, 3, 2),  -- Nitesh Tiwari directed Dangal
       (2, 4, 1),  -- Fatima acted in Dangal
       (2, 5, 1);  -- Sanya acted in Dangal
