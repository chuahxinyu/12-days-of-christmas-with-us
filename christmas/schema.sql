DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS songs;
DROP TABLE IF EXISTS movies;
DROP TABLE IF EXISTS recipes;
DROP TABLE IF EXISTS user_days;


CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    notes TEXT
);

CREATE TABLE songs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    artist TEXT,
    img TEXT NOT NULL,
    link TEXT NOT NULL
);

CREATE TABLE movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    img TEXT,
    external_link TEXT
);

CREATE TABLE recipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    img TEXT,
    external_link TEXT
);

CREATE TABLE user_days (
    user_id INTEGER,
    day_num INTEGER,
    movie_id INTEGER,
    song_id INTEGER,
    recipe_id INTEGER,
    img TEXT,
    PRIMARY KEY (user_id, day_num),
    FOREIGN KEY (user_id) REFERENCES user(id),
    FOREIGN KEY (movie_id) REFERENCES movies(id),
    FOREIGN KEY (song_id) REFERENCES songs(id),
    FOREIGN KEY (recipe_id) REFERENCES recipes(id)
);

INSERT INTO TABLE movies (title, description, img, external_link)
VALUES ('Santa Claus: The Movie',
'The legend of Santa Claus is put in jeopardy when an unscrupulous toy manufacturer attempts to take over Christmas.',
'/static/movies/1-santa-claus-the-movie.jpg',
'https://www.imdb.com/title/tt0089961/');

INSERT INTO TABLE movies (title, description, img, external_link)
VALUES (
'Dr. Seuss How the Grinch Stole Christmas (2000)', 
'On the outskirts of Whoville lives a green, revenge-seeking Grinch who plans to ruin Christmas for all of the citizens of the town.',
'/static/movies/2_How_the_Grinch_Stole_Christmas.jpg',
'https://www.imdb.com/title/tt0170016/');

INSERT INTO TABLE movies (title, description, img, external_link)
VALUES (
'Home Alone (1990)', 
'An eight-year-old troublemaker must protect his house from a pair of burglars when he is accidentally left home alone by his family during Christmas vacation.'
'/static/movies/3_HomeAlone.jpg',
'https://www.imdb.com/title/tt0099785/');

INSERT INTO TABLE movies (title, description, img, external_link)
VALUES (
'Elf (2003)', 
'Raised as an over-sized elf, a human travels from the North Pole to NYC to meet his biological father who doesnt know he exists and is in desperate need of some Christmas spirit.',
'/static/movies/4_Elf.jpg',
'https://www.imdb.com/title/tt0319343/');

INSERT INTO TABLE movies (title, description, img, external_link)
VALUES (
'The Polar Express', 
'On Christmas Eve, a young boy embarks on a magical adventure to the North Pole on the Polar Express, while learning about friendship, bravery, and the spirit of Christmas.',
'/static/movies/5_The_Polar_Express.jpg',
'https://www.imdb.com/title/tt0338348/');

INSERT INTO TABLE movies (title, description, img, external_link)
VALUES (
'The Nightmare Before Christmas', 
'Jack Skellington, king of Halloween Town, discovers Christmas Town, but his attempts to bring Christmas to his home causes confusion.',
'/static/movies/6_The_Nightmare_Before_Christmas.jpg',
'https://www.imdb.com/title/tt0107688/');

INSERT INTO TABLE movies (title, description, img, external_link)
VALUES (
'The Santa Clause', 
'When a man inadvertently makes Santa fall off of his roof on Christmas Eve, he finds himself magically recruited to take his place.',
'/static/movies/7_The_Santa_Clause.jpg',
'https://www.imdb.com/title/tt0111070/');

INSERT INTO TABLE movies (title, description, img, external_link)
VALUES (
'The Santa Clause 2', 
'Scott Calvin has been a humble Santa Claus for nearly ten years, but it might come to an end if he doesnt find a Mrs. Claus.',
'/static/movies/8_The Santa_Clause_2.jpg',
'https://www.imdb.com/title/tt0304669/');

INSERT INTO TABLE movies (title, description, img, external_link)
VALUES (
'The Santa Clause 3: The Escape Clause', 
'Santa, a.k.a. Scott Calvin, is faced with double-duty: how to keep his new family happy and how to stop Jack Frost from taking over Christmas.', 
'/static/movies/9_The_Santa_Clause_3.jpg',
'https://www.imdb.com/title/tt0107688/');

INSERT INTO TABLE movies (title, description, img, external_link)
VALUES (
'The Holiday', 
'Two women troubled with guy-problems swap homes in each others countries, where they each meet a local guy and fall in love.',
'/static/movies/10_The_Holiday.jpg',
'https://www.imdb.com/title/tt0457939/');

INSERT INTO TABLE movies (title, description, img, external_link)
VALUES (
'Arthur Christmas', 
'Santas clumsy son Arthur sets out on a mission with Grandsanta to give out a present they misplaced to a young girl in less than two hours.',
'/static/movies/11_Arthur_Christmas.jpg',
'https://www.imdb.com/title/tt1430607/');

INSERT INTO TABLE movies (title, description, img, external_link)
VALUES (
'Scrooged', 
'A selfish, cynical television executive is haunted by three spirits bearing lessons on Christmas Eve.',
'/static/movies/12_Scrooged.jpg',
'https://www.imdb.com/title/tt0096061/');

INSERT INTO TABLE movies (title, description, img, external_link)
VALUES (
'A Christmas Carol (2009)', 
'An animated retelling of Charles Dickens classic novel about a Victorian-era miser taken on a journey of self-redemption, courtesy of several mysterious Christmas apparitions.',
'/static/movies/13_A_Christmas_Carol.jpg',
'https://www.imdb.com/title/tt1067106/');

INSERT INTO TABLE songs (title, artist, img, link)
VALUES (
