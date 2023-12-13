USE `passwordVault`;

CREATE TABLE IF NOT EXISTS `userVault` (
    `password_id` INT AUTO_INCREMENT PRIMARY KEY,
    `websiteURL` VARCHAR(60),
    `username` VARCHAR(25) NOT NULL,
    `password_salt` VARCHAR(64) NOT NULL,
    `password_cipher` VARCHAR(256) NOT NULL
);