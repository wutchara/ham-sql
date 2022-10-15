`db`CREATE TABLE `db`.Persons (
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


SELECT `db`.`Persons`.`LastName`, `db`.`Persons`.`FirstName`, `db`.`VIP`.`Status` 
FROM `db`.`Persons` 
FULL OUTER JOIN `db`.`VIP` ON `db`.`Persons`.`LastName` = `db`.`VIP`.`LastName`;


SELECT A.LastName, B.LastName FROM Persons A, VIP B;



CREATE TABLE `db`.ccb_ci_rmr
(
 
   trialgroup                      VARCHAR(255)     NOT NULL,
   site                            VARCHAR(255)     NOT NULL,
   processts                       VARCHAR(255)     NOT NULL,
   insertts                        VARCHAR(255)     NOT NULL,
   hddsnenddate                    VARCHAR(255)     NOT NULL,
   hddsn                           VARCHAR(255)     NOT NULL,
   enddate                         VARCHAR(255)     NOT NULL,
   drivemodel                      VARCHAR(255)     NOT NULL,
   pfcode                          VARCHAR(255)     NOT NULL,
   testcode                        VARCHAR(255)     NOT NULL,
   testcodec                       VARCHAR(255)     NOT NULL,
   testcodesuff                    VARCHAR(255)     NOT NULL,
   mfgid                           VARCHAR(255)     NOT NULL,
   mfgid_1                         VARCHAR(255)     NOT NULL,
   mfgid_2                         VARCHAR(255)     NOT NULL,
   mfgid_3                         VARCHAR(255)     NOT NULL,
   mfgid_4                         VARCHAR(255)     NOT NULL,
   mfgid_5                         VARCHAR(255)     NOT NULL,
   hddtrial                        VARCHAR(255)     NOT NULL,
   aetype                          VARCHAR(255)     NOT NULL,
   hdctype                         VARCHAR(255)     NOT NULL,
   cmdname                         VARCHAR(255)     NOT NULL,
   qualifier                       VARCHAR(255)     NOT NULL,
   lhd                             INTEGER                 NOT NULL,
   mcsbver                         INTEGER                 NOT NULL,
   phd                             INTEGER                 NOT NULL,
   subqualifier                    VARCHAR(255)     NOT NULL,
   readerselection                 INTEGER                 NOT NULL,
   cmdexecutiontimeinmilliseconds  BIGINT                  NOT NULL,
   deltarmr                        INTEGER                 NOT NULL,
   dletarmr_0                      INTEGER                 NOT NULL,
   deltarmr_1                      INTEGER                 NOT NULL,
   mrr                             INTEGER                 NOT NULL,
   avermrval_0                     INTEGER                 NOT NULL,
   avermrval_1                     INTEGER                 NOT NULL,
   minrmr                          INTEGER                 NOT NULL,
   minrmrval_0                     INTEGER                 NOT NULL,
   minrmrval_1                     INTEGER                 NOT NULL,
   maxrmr                          INTEGER                 NOT NULL,
   maxrmrval_0                     INTEGER                 NOT NULL,
   maxrmrval_1                     INTEGER                 NOT NULL,
   deltatfc                        INTEGER                 NOT NULL,
   tfr                             INTEGER                 NOT NULL,
   mintfc                          INTEGER                 NOT NULL,
   maxtfc                          INTEGER                 NOT NULL,
   aveecsval                       INTEGER                 NOT NULL,
   minecsval                       INTEGER                 NOT NULL,
   maxecsval                       INTEGER                 NOT NULL,
   aveldrval                       INTEGER                 NOT NULL,
   minldrval                       INTEGER                 NOT NULL,
   maxldrval                       INTEGER                 NOT NULL,
   ecsroughresistance              INTEGER                 NOT NULL,
   ecsfineresistance_0             INTEGER                 NOT NULL,
   ecsfineresistance_1             INTEGER                 NOT NULL,
   ecsresistanceslope              BIGINT                  NOT NULL,
   drivetemp                       INTEGER                 NOT NULL,
   heliumconc                      INTEGER                 NOT NULL,
   aveheliumconc                   INTEGER                 NOT NULL,
   avepmrplusval                   DOUBLE                  NOT NULL,
   minpmrplusval                   DOUBLE                  NOT NULL,
   maxpmrplusval                   DOUBLE                  NOT NULL,
   pmrplusadcgain                  INTEGER                 NOT NULL,
   pmrplusbiasdacp1                INTEGER                 NOT NULL,
   pmrplusbiasdacp2                INTEGER                 NOT NULL,
   pmrplusvoltdacp1                INTEGER                 NOT NULL,
   pmrplusvoltdacp2                INTEGER                 NOT NULL,
   spaidentifier                   INTEGER                 NOT NULL,
   startdate                       VARCHAR(255)     NOT NULL,
   deltatfc2val                    INTEGER                 NOT NULL,
   avetfc2val                      INTEGER                 NOT NULL,
   mintfc2val                      INTEGER                 NOT NULL,
   maxtfc2val                      INTEGER                 NOT NULL,
   aventsval                       INTEGER                 NOT NULL,
   minntsval                       INTEGER                 NOT NULL,
   maxntsval                       INTEGER                 NOT NULL,
   product                         VARCHAR(255)     NOT NULL,
   procid                          VARCHAR(255)     NOT NULL,
   enddt                           VARCHAR(255)     NOT NULL
);