CREATE TABLE User (
  email VARCHAR(30) NOT NULL,
  name VARCHAR(40) NOT NULL,
  password TEXT NOT NULL,
  CONSTRAINT PK_User PRIMARY KEY (email)
);

CREATE TABLE Admin (
  email VARCHAR(40) NOT NULL,
  CONSTRAINT PK_Admin PRIMARY KEY (email),
  CONSTRAINT FK_Admin_User FOREIGN KEY (email)
  REFERENCES User (email)
  ON DELETE CASCADE
  ON UPDATE CASCADE
);

CREATE TABLE Chef (
  email VARCHAR(40) NOT NULL,
  description TEXT NOT NULL,
  CONSTRAINT PK_Chef PRIMARY KEY (email),
  CONSTRAINT FK_Chef_User FOREIGN KEY (email)
  REFERENCES User (email)
  ON DELETE CASCADE
  ON UPDATE CASCADE
);

CREATE TABLE Follow (
  chef_follower VARCHAR(40) NOT NULL,
  chef_follow VARCHAR(40) NOT NULL,
  CONSTRAINT PK_Follow PRIMARY KEY (chef_follower, chef_follow),
  CONSTRAINT FK_Follow_Left FOREIGN KEY (chef_follower)
  REFERENCES Chef (email)
  ON DELETE CASCADE
  ON UPDATE CASCADE,
  CONSTRAINT FK_Follow_Right FOREIGN KEY (chef_follow)
  REFERENCES Chef (email)
  ON DELETE CASCADE
  ON UPDATE CASCADE
);


CREATE TABLE Category (
  name VARCHAR(30) NOT NULL,
  CONSTRAINT PK_Category PRIMARY KEY (name)
);

CREATE TABLE Recipe (
  id_recipe SERIAL NOT NULL,
  name VARCHAR(30) NOT NULL,
  image BYTEA NOT NULL,
  description TEXT NOT NULL,
  likes INTEGER,
  category VARCHAR(15),
  owner VARCHAR(40) NOT NULL,
  CONSTRAINT PK_Recipe PRIMARY KEY id_recipe,
  CONSTRAINT FK_Recipe_Category FOREIGN KEY (category)
  REFERENCES Category (name)
  ON UPDATE CASCADE
  ON DELETE SET NULL,
  CONSTRAINT FK_Recipe_Chef FOREIGN KEY (owner)
  REFERENCES Chef (email)
  ON UPDATE CASCADE
  ON DELETE CASCADE
);

CREATE TABLE Coment (
  id_coment SERIAL,
  id_recipe INTEGER,
  email VARCHAR(40),
  message VARCHAR(50) NOT NULL,
  CONSTRAINT PK_Coment PRIMARY KEY (id_coment),
  CONSTRAINT FK_Coment_Recipe FOREIGN KEY (id_recipe)
  REFERENCES Recipe (id_recipe),
  ON DELETE CASCADE
  ON UPDATE CASCADE,
  CONSTRAINT FK_Coment_Chef FOREIGN KEY (email)
  REFERENCES Chef (email)
  ON DELETE CASCADE
  ON UPDATE CASCADE,
);

CREATE TABLE Post (
  id_post SERIAL NOT NULL,
  description TEXT NOT NULL,
  publisher VARCHAR(40) NOT NULL,
  recipe_published INTEGER,
  CONSTRAINT PK_Post PRIMARY KEY (id_post),
  CONSTRAINT FK_Post_Chef FOREIGN KEY (publisher)
  REFERENCES Chef (email)
  ON DELETE CASCADE
  ON UPDATE CASCADE,
  CONSTRAINT FK_Post_Recipe FOREIGN KEY (recipe_published)
  REFERENCES Recipe (id_recipe)
  ON DELETE CASCADE
  ON UPDATE CASCADE
);

CREATE TABLE Share (
  chef VARCHAR(40) NOT NULL,
  id_post INTEGER NOT NULL,
  CONSTRAINT PK_Share PRIMARY KEY (chef, id_post),
  CONSTRAINT FK_Share_Chef FOREIGN KEY (chef)
  REFERENCES Chef (email)
  ON DELETE CASCADE
  ON UPDATE CASCADE,
  CONSTRAINT FK_Share_Post FOREIGN KEY (id_post)
  REFERENCES Post (id_post)
  ON DELETE CASCADE
  ON UPDATE CASCADE
);

CREATE TABLE Recipe_Ingredients (
  id_recipe INTEGER,
  ingredient VARCHAR(20) NOT NULL,
  CONSTRAINT PK_Ingredients PRIMARY KEY (id_recipe, ingredient),
  CONSTRAINT FK_Recipe_Ingredients_Recipe FOREIGN KEY (id_recipe)
  REFERENCES Recipe (id_recipe)
  ON DELETE CASCADE
  ON UPDATE CASCADE
);
