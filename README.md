# Salesforce Data Import To MySQL

This script just reading Salesforce csv files import to MySQL database.

## Salesforce IDs

Salesforce using base62 encoding for Id column. I used Sumin Byeon's base62 library for id convertions.

[https://github.com/suminb/base62](https://github.com/suminb/base62)

Also original Salesforce ids added to SfId column

## Missing Tables

While you exporting your Salesforce data some tables does not seen on the list. I just detect and get data with Salesforce API.

It could be much more table but these are solved my problem.

~~~
BusinessHours
CaseMilestone
EntitlementMilestone
MilestoneType
SlaProcess
~~~

## Column Types

Script detecting column types with column names also the values in it.

## Users Table

In the User.csv file there is no password data. I just needed in my custom project and added Password column and set default password as "P@ssW0rD".

## Before Running

Be sure you created MySQL database!

## Running Application

You can import directly one file or whole directory. 

for one file
~~~
$ ./sfcsvimport.py --file ./csv_directory/Account.csv 
~~~

for all data in directory
~~~
$ ./sfcsvimport.py --directory ./csv_directory
~~~

## Parameters

You can test your data with "--test-data" parameter.

Below example will use only first 100 rows of each file.

~~~
$ ./sfcsvimport.py --directory ./csv_directory --test-data 100
~~~

Also with "--debug" parameter you can see detailed output and with "--log-file" parameter you can write it to the file.

~~~
$ ./sfcsvimport.py --directory ./csv_directory --test-data 100 --debug --log-file debug.log
~~~

You can see all available paramters with running -h for help.

~~~
$ ./sfcsvimport.py -h
usage: sfcsvimport.py [-h] [--directory DIRECTORY] [--file FILE] [--debug]
                      [--test-data TEST_DATA] [--log-file LOG_FILE]
                      [--mysql-host MYSQL_HOST] [--mysql-port MYSQL_PORT]
                      [--mysql-user MYSQL_USER]
                      [--mysql-password MYSQL_PASSWORD]
                      [--mysql-database MYSQL_DATABASE] [--reset-id-pool]
                      [--use-base62]

optional arguments:
  -h, --help            show this help message and exit
  --directory DIRECTORY
                        path of csv directory
  --file FILE           path of csv file
  --debug               debug
  --test-data TEST_DATA
                        test data fize per file
  --log-file LOG_FILE   path of log file
  --mysql-host MYSQL_HOST
                        mysql server address
  --mysql-port MYSQL_PORT
                        mysql server port
  --mysql-user MYSQL_USER
                        mysql username
  --mysql-password MYSQL_PASSWORD
                        mysql pasword
  --mysql-database MYSQL_DATABASE
                        mysql database anem
  --reset-id-pool       debug
  --use-base62          debug
~~~