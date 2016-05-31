---
title: Numerische Simulationen
author: Philipp Geier
date: 1. Juni 2016 

toc: "yes"
#fontsize: '8pt'

---

# Einführung

## Inhalt der Lehrveranstaltung

* Konzepte relationaler Datenbanksysteme
* Design von Datenbanken
* Daten mit SQL^[Standard Query Language] abfragen und verändern
* Some math $\alpha \mathbb{R} \mathbbm{1} 1 2 3$

Basis für alle Beispiele: MySQL

## Inhalt im Detail

* Einführung, Hello-World!-Beispiel, MySQL
* Datenbankmodellierung (semantisch, logisch, physisch)
* Entity-Relationship-Modelle
* Datentypen
* Relationships (1:1, 1:n, n:m, identifying vs. non-identifying)
* Primary Keys, Foreign Keys, Foreign Key Constraints
* Normalformen (1NF, 2NF, 3NF), De-Normalisierung
* SQL-Einführung (SELECT, INSERT, UPDATE, DELETE, CREATE/ALTER/DROP TABLE)
* Transaktionen, ACID
* viele praktische Beispiel

## Datenbanken versus Datenbanksysteme

\colA{6cm}

Datenbanken

* Adressen für Serienbriefe
* Patientenkartei einer Artzpraxis
* Warenbestand eines Lebensmitteldiskonters
* Facebook
* Telekom-Abrechnungssystem
* ...

\colB{6cm}

Datenbanksysteme

* IBM DB/2
* Microsoft Access
* Microsoft SQL Server
* MySQL
* Oracle
* PostgreSQL
* SAP MaxDB
* SQLite

\colEnd

\vspace{3mm}

PS: Ein Datenbanksystem ist genaugenommen ein *Datenbankmanagagementsystem*.
**DBMS** = *Database Management System*.

# Test2

## Test

```` {.table type="multiline" aligns="C" caption="a table" header="yes"}
$\mathrm{Mathrm}$,$\mathit{Mathit}$,$\mathbf{MathBF}$,$\bm{BM}$
$\mathrm{A little text}$,$\mathit{A little text}$,$\mathbf{A little text}$,$\bm{A little text}$
$\mathrm{\nabla \cdot \nabla}$,$\mathit{\nabla \cdot \nabla}$,$\mathbf{\nabla \cdot \nabla}$,$\bm{\nabla \cdot \nabla}$
$\mathrm{\alpha \times 3}$,$\mathit{\alpha \times 3}$,$\mathbf{\alpha \times 3}$,$\bm{\alpha \times 3}$
```` 

## Wozu Datenbanksysteme?

* Sicherheit

    + Datenverluste vermeiden
    + steuern, wer welche Daten lesen/verändern darf
    + aufzeichnen, wer wann was verändert hat
    + Transaktionen
    + Backups
    + Hochverfügbarkeit

* Netzwerkzugriff
* Multi-User-Zugriff mit Zugriffskontrolle

## Client/Server-Modell

<!-- \includegraphics[width=0.8textwidth]{bilder/client-server.png}
-->

## Relationale Datenbanken

* Organisation aller Daten in Tabellen
* jede Tabelle für sich: ähnlich wie Excel-Tabellenblatt
* Tabellen sind miteinander verknüpft (Relationships)
* Verknüpfungen über ID-Spalten (Primary Key, Foreign Key)


# Test3

## Relationale Datenbanken

hbox{}hspace*{-9mm}includegraphics[width=1.17textwidth]{bilder/schema-mylibrary.png}

# Test4

## Standard Query Language = SQL

    SELECT * FROM personen

    SELECT * FROM personen ORDER BY nachname, vorname

    SELECT id, nachname, vorname FROM personen

    SELECT COUNT(*) FROM personen

    SELECT COUNT(*) FROM personen WHERE geschlecht='f'
    
    
## Col test


\row{c}

\col{0.3\textwidth}

![](images/Tux.pdf){#fig:fig1 width=50%}\

test

\col{0.3\textwidth}

test
![](images/Tux.pdf){#fig:fig1 width=50%}\

\rowend

\row{c}

\col{0.3\textwidth}

![](images/Tux.pdf){#fig:fig1 width=50%}\

test

\col{0.3\textwidth}

test
![](images/Tux.pdf){#fig:fig1 width=50%}\

\rowend
