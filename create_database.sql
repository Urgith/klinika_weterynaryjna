CREATE DATABASE klinika_weterynaryjna;

CREATE TABLE `asortyment` (
  `id_asortymentu` int(11) NOT NULL AUTO_INCREMENT,
  `data_zakupu` date DEFAULT NULL,
  `cena` float DEFAULT NULL,
  `ilosc` int(11) DEFAULT NULL,
  `produkt` varchar(127) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id_asortymentu`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `czynnosci` (
  `id_czynnosci` int(11) NOT NULL AUTO_INCREMENT,
  `czynnosc` varchar(63) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `cena` float DEFAULT NULL,
  PRIMARY KEY (`id_czynnosci`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `pracownicy` (
  `id_pracownika` int(11) NOT NULL AUTO_INCREMENT,
  `imie` varchar(31) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `nazwisko` varchar(63) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `plec` SET('mężczyzna', 'kobieta') COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `data_urodzenia` date DEFAULT NULL,
  `adres_zamieszkania` varchar(63) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `numer_telefonu` varchar(15) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `stanowisko_pracy` varchar(31) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `data_zatrudnienia` date DEFAULT NULL,
  PRIMARY KEY (`id_pracownika`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `zarobki` (
  `id_pracownika` int(11) DEFAULT NULL,
  `etat` SET('pełen', 'pół') COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `wyplata` float DEFAULT NULL,
  `od` date DEFAULT NULL,
  `do` date DEFAULT NULL,
  `premia` float DEFAULT NULL,
  KEY `FK_zarobki_pracownicy` (`id_pracownika`),
  CONSTRAINT `FK_zarobki_pracownicy` FOREIGN KEY (`id_pracownika`) REFERENCES `pracownicy` (`id_pracownika`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `zmiany` (
  `id_zmiany` int(11) NOT NULL AUTO_INCREMENT,
  `id_lekarza` int(11) DEFAULT NULL,
  `id_asystenta` int(11) DEFAULT NULL,
  `id_rejestratora` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_zmiany`),
  KEY `FK_zmiany_pracownicy` (`id_lekarza`),
  KEY `FK_zmiany_pracownicy_2` (`id_asystenta`),
  KEY `FK_zmiany_pracownicy_3` (`id_rejestratora`),
  CONSTRAINT `FK_zmiany_pracownicy` FOREIGN KEY (`id_lekarza`) REFERENCES `pracownicy` (`id_pracownika`),
  CONSTRAINT `FK_zmiany_pracownicy_2` FOREIGN KEY (`id_asystenta`) REFERENCES `pracownicy` (`id_pracownika`),
  CONSTRAINT `FK_zmiany_pracownicy_3` FOREIGN KEY (`id_rejestratora`) REFERENCES `pracownicy` (`id_pracownika`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `wlasciciele` (
  `id_wlasciciela` int(11) NOT NULL AUTO_INCREMENT,
  `imie` varchar(31) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `nazwisko` varchar(63) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `telefon` varchar(15) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `adres` varchar(63) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `data_rejestracji` datetime DEFAULT NULL,
  PRIMARY KEY (`id_wlasciciela`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `zwierzeta` (
  `id_zwierzecia` int(11) NOT NULL AUTO_INCREMENT,
  `id_wlasciciela` int(11) DEFAULT NULL,
  `zwierze` varchar(31) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `rasa` varchar(31) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `plec` SET('samiec', 'samica') COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `imie` varchar(31) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `data_urodzenia` date DEFAULT NULL,
  `wiek` float DEFAULT NULL,
  `waga` float DEFAULT NULL,
  `wzrost` float DEFAULT NULL,
  PRIMARY KEY (`id_zwierzecia`),
  KEY `FK_zwierzeta_wlasciciele` (`id_wlasciciela`),
  CONSTRAINT `FK_zwierzeta_wlasciciele` FOREIGN KEY (`id_wlasciciela`) REFERENCES `wlasciciele` (`id_wlasciciela`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `wizyty` (
  `id_wizyty` int(11) NOT NULL AUTO_INCREMENT,
  `id_zwierzecia` int(11) DEFAULT NULL,
  `id_czynnosci` int(11) DEFAULT NULL,
  `id_zmiany` int(11) DEFAULT NULL,
  `data_rejestracji` datetime DEFAULT NULL,
  `data_wizyty` datetime DEFAULT NULL,
  PRIMARY KEY (`id_wizyty`),
  KEY `FK_wizyty_czynnosci` (`id_czynnosci`),
  KEY `FK_wizyty_zwierzeta` (`id_zwierzecia`),
  KEY `FK_wizyty_zmiany` (`id_zmiany`),
  CONSTRAINT `FK_wizyty_czynnosci` FOREIGN KEY (`id_czynnosci`) REFERENCES `czynnosci` (`id_czynnosci`),
  CONSTRAINT `FK_wizyty_zmiany` FOREIGN KEY (`id_zmiany`) REFERENCES `zmiany` (`id_zmiany`),
  CONSTRAINT `FK_wizyty_zwierzeta` FOREIGN KEY (`id_zwierzecia`) REFERENCES `zwierzeta` (`id_zwierzecia`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
