BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `wuyts_maxim` (
	`brand`	TEXT,
	`product_name`	TEXT,
	`old_price in €`	INTEGER,
	`current_price in €`	INTEGER,
	`total_ratings`	INTEGER
);
INSERT INTO `wuyts_maxim` VALUES ('Nubia','Nubia N1 Lite 4G LTE Dual SIM Unlocked Smartphone 5.5" 2GB RAM Black/Gold| US Warranty','131,99','70,99','9)');
INSERT INTO `wuyts_maxim` VALUES ('SAMSUNG','Samsung Galaxy S7 Edge Dual SIM Unlocked Smart Phone| Dual Edge 5.5" AMOLED Display| Gold Color| 32GB Storage 4GB RAM International Version - No Warranty','693,99','503,9',46);
INSERT INTO `wuyts_maxim` VALUES ('Apple','Apple iPhone 7 256GB Black Unlocked Smartphone','777,99','437,9','6)');
INSERT INTO `wuyts_maxim` VALUES ('SAMSUNG','Samsung Galaxy S8+ (Plus) G955FD Dual SIM GSM Unlocked Smart Phone| 6.2" AMOLED Display| Maple Gold Color| 64GB Storage International Version - No Warranty','789,99','412,9',10);
INSERT INTO `wuyts_maxim` VALUES ('Motorola','Moto G5 Plus XT1687 32GB Smartphone (Unlocked| Fine Gold) - US Warranty','202,99','176,9',66);
INSERT INTO `wuyts_maxim` VALUES ('SAMSUNG','Samsung Galaxy S8+ (Plus) G955FD Dual SIM GSM Unlocked Smart Phone| 6.2" AMOLED Display| Midnight Black Color| 64GB Storage International Version - No Warranty',NULL,'604,9',10);
INSERT INTO `wuyts_maxim` VALUES ('SAMSUNG','Samsung Galaxy Note 8 Dual SIM Unlocked Smartphone with LED Dual Camera (6.3" Black| 6GB RAM) International Version - No Warranty','751,99','503,9','1)');
INSERT INTO `wuyts_maxim` VALUES ('Motorola','Moto G5s Plus (Special Edition) Unlocked Smartphone Dual Camera (5.5" Lunar Gray| 32GB Storage 3GB RAM) US Warranty','243,99','174,9',40);
COMMIT;