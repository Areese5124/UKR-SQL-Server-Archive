## About 
The UKR Server Sql Archive was a project for created for [Doctor Amelia Glaser's](https://literature.ucsd.edu/people/faculty/aglaser.html) [Contemporary Ukrainian Poetry Archive](https://ukrpoetry.org/) under the supervision of [Doctor Margaret E. Roberts](https://polisci.ucsd.edu/people/faculty/faculty-directory/currently-active-faculty/roberts-profile.html) during the Fall Quarter of 2024. 

## Goal of the Project
The goal of this project was to create a scaleable SQL database structure and to transfer the data of the [Contemporary Ukrainian Poetry Archive](https://ukrpoetry.org/) into the SQL server. 

## Results of the Project
All of the data for public use was transferred from the spreadsheets it was on into a MYSQL server. The server operates independently of the UCSD server structures instead using a third party service as the host for the database. This allows users to not need a UCSD account to access the database. If you would like to access the database for any reason please email Doctor Glaser at **amglaser@ucsd.edu**.

Their are details of the structure of the archive in the [src folder](https://github.com/Areese5124/UKR-SQL-Server-Archive/blob/main/res/UKR%20Poem%20Archive%20Structure.png) with a Entity Relationship diagram. For further details you can examine the [UKR-Database-Construction-Script](https://github.com/Areese5124/UKR-SQL-Server-Archive/blob/main/.config/UKR-Database-Construction-Script.sql) which was the SQL script used to create the database.

