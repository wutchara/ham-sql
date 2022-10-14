INSERT INTO `db`.`Persons` VALUES (0, 'Last', 'First', '--', 'city');
INSERT INTO `db`.`Persons`(`LastName`,`FirstName`,`City`) VALUES ('Last-3', 'First-4', 'city-3');
SELECT * FROM `db`.`Persons`;


SELECT * FROM `Persons`;

DELETE FROM `db`.`Persons` WHERE `PersonID`=1 AND `Address`='--';