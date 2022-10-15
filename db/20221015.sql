SELECT * FROM `Persons`;

SELECT `LastName` AS `X` FROM `Persons` WHERE LastName = 'HAM';

SELECT DISTINCT `LastName` FROM `Persons`;

SELECT COUNT(`LastName`) AS XZXXXXX FROM `Persons`;

SELECT * FROM `db`.`Persons` WHERE `LastName` LIKE 'Last%';

SELECT * FROM `db`.`Persons` WHERE `LastName` LIKE '%-1';

SELECT * FROM `db`.`Persons` WHERE `LastName` LIKE '%st%';

SELECT * FROM `db`.`Persons` WHERE `LastName` IN ('Last-1', 'Last-2');

UPDATE `db`.`Persons` SET `LastName` = 'Last-5' WHERE `PersonID`=5;

UPDATE `db`.`Persons` SET `Address` = '..';

SELECT * FROM `db`.`Persons` WHERE `LastName` IN (SELECT * FROM `db`.`VIP`);
