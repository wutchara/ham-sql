CREATE TABLE `db`.Persons (
    PersonID INT,
    LastName VARCHAR(255),
    FirstName VARCHAR(255),
    Address VARCHAR(255),
    City VARCHAR(255)
);


INSERT INTO `db`.`Persons` VALUES (0, 'Last', 'First', '--', 'city');

INSERT INTO `db`.`Persons`(`LastName`,`FirstName`,`City`) VALUES ('Last-3', 'First-4', 'city-3');


ALTER TABLE `db`.`Persons`
ADD Email VARCHAR(255);

SELECT * FROM `db`.`Persons` WHERE `PersonID`=1 AND `Address`='--';
SELECT * FROM `Persons`;

DELETE FROM `db`.`Persons` WHERE `PersonID`=1 AND `Address`='--';