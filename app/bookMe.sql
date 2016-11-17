--COMP 343
--BookMe
-- -----------------------------------------------------||||
-- Drop all tables before running scripts
DROP TABLE IF EXISTS reservation cascade;
DROP TABLE IF EXISTS waiting cascade;
DROP TABLE IF EXISTS user cascade;
DROP TABLE IF EXISTS room cascade;
DROP TABLE IF EXISTS timeslot cascade;
-- /////////////////////////////////////////////////////////
-- ---------------------------------
-- Table: user
-- Desc: represents users of the system
-- ---------------------------------
CREATE TABLE IF NOT EXISTS user (
	userId INT UNSIGNED NOT NULL AUTO_INCREMENT,
	password VARCHAR(30) NOT NULL,
	name VARCHAR(30)  NOT NULL DEFAULT ' ',
	email VARCHAR(30)  NOT NULL DEFAULT ' ',
	PRIMARY KEY (userId)
);
-- ---------------------------------
-- Table: room
-- Desc: represents rooms that can be reserved
-- Note: lock :: determine if room can be accessed
-- ---------------------------------
CREATE TABLE IF NOT EXISTS room (
	roomId INT UNSIGNED NOT NULL AUTO_INCREMENT,
	roomLock BOOLEAN NOT NULL DEFAULT 0,
	PRIMARY KEY (roomId)
);
-- ---------------------------------
-- Table: timeslot
-- Desc: represents a timeslot for a reservation
-- ---------------------------------
CREATE TABLE IF NOT EXISTS timeslot (
	timeId INT UNSIGNED NOT NULL AUTO_INCREMENT,
	startTime INT UNSIGNED NOT NULL,
	endTime INT UNSIGNED NOT NULL,
	date DATE NOT NULL,
	block INT UNSIGNED NOT NULL,
	PRIMARY KEY (timeId)
);
-- ---------------------------------
-- Table: waiting
-- Desc: captures a reservation that is on a waiting list
-- ---------------------------------
CREATE TABLE IF NOT EXISTS waiting (
	waitingId INT UNSIGNED NOT NULL AUTO_INCREMENT,
	room INT UNSIGNED,
	reservee INT UNSIGNED,
	description VARCHAR(100),
	timeslot INT UNSIGNED,
	PRIMARY KEY (waitingId),
	FOREIGN KEY (room) REFERENCES room (roomId),
	FOREIGN KEY (reservee) REFERENCES user (userId),
	FOREIGN KEY (timeslot) REFERENCES timeslot (timeId)
);
-- ---------------------------------
-- Table: reservation
-- Desc: represents reservations made by users
-- ---------------------------------
CREATE TABLE IF NOT EXISTS reservation (
	reservationId INT UNSIGNED NOT NULL AUTO_INCREMENT,
	room INT UNSIGNED,
	description VARCHAR(100),
	holder INT UNSIGNED,
	timeslot INT UNSIGNED,
	PRIMARY KEY (reservationId),
	FOREIGN KEY (room) REFERENCES room (roomId),
	FOREIGN KEY (holder) REFERENCES user (userId),
	FOREIGN KEY (timeslot) REFERENCES timeslot (timeId)
);
-- ///////////// INSERT STATMENTS //////////////////////
INSERT INTO user(password, name, email) VALUES
	('pass','John Smith', 'jsmith@hotmail.com'),
	('pass','Emily Haynes', 'e_haynes@gmail.com');
INSERT INTO room(roomId) VALUES
	(1),
	(2),
	(3),
	(4),
	(5);
