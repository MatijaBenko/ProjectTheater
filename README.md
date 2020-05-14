## Problem Overview
In this project, I wrote a python program that can be used by small theaters to sell tickets for performances. The program allows a theater to enter the number of rows and columns of seating that they have and the price for each row of seats. It will then allow the theater staff to sell individual seats or groups of seats, give the total for each order, and keep track of which seats are still available.

![Theater Seating](http://www.preferred-seating.com/images/Phoenix-Elite-36-Front.jpg)

What the Program Must Do: 

* The first time your program is run, it should prompt the user for the number of rows and columns in the theater and for the price for seats row of seating (up to a pre-defined maximum number).  Store that information in a configuration file that you can then read the next time the program is run.

* Display a main menu to the user with the following options:

    * Display a seating chart
    * Sell one or more tickets
    * Display statistics such as the number of tickets sold, the number of seats still available, the total revenue from ticket sales, etc.
    * Reset the program and re-enter the theater seating and pricing information

* The seating chart should be displayed in a fashion similar to the one below (which is for a theater with 10 rows and 30 columns of seating) where taken seats are represented by a * symbol and available seats are represented by a # symbol.

```text
                       Seats
           0        1         2         3
           123456789012345678901234567890
    Row  1 ***###***###*########*****####
    Row  2 ####*************####*******##
    Row  3 **###**********########****###
    Row  4 **######**************##******
    Row  5 ********#####*********########
    Row  6 ##############************####
    Row  7 #######************###########
    Row  8 ************##****############
    Row  9 #########*****############****
    Row 10 #####*************############
```

*  When selling tickets, the program should allow the user to enter individual seats (by row and seat number) and/or ranges of seats.  You must validate user input so that you do not accept a row or seat
  number that does not exist and you do not sell a seat that is already taken. When the group of seats has been reserved, display the total price for the transaction.

*  Extra Feature: Although not required, you may wish to have your program save the seating chart to a configuration file so that it can be read back in when the program is restarted.

## Solution Specification
Your solution should strive to meet the standards specified below as they form the basis on which it will be graded.

1. You must use a two-dimensional array to keep track of your seating chart.  You may wish to use other vectors or arrays to keep track of additional information.

2. Your program must be divided into functions which perform well-defined and logical sub-tasks for the problem.  Before you go too far on your development, check with your professor, TA, or a tutor about your choice of functions and the parameters and/or return types that they will require.

3. The file `theater.txt` must be used to save the theater configuration so that when the program starts again, the information can be read from the file instead of being re-entered by the user. When your program starts, check to see if this file exists and if it does not, create it.

3. You must validate all user input and handle errors gracefully.

5. Since this is your final project in the class, show off as much of what you've learned as possible.  In particular, you are expected to make use of the following concepts somewhere in your program.

   * Appropriate branching and looping statements
   * Console input/output and file output using streams
   * Functions with various return and parameter types (pass-by-reference, default values, etc)
   * Global constants (likely for your maximum array dimensions)
   * Vectors and arrays passed as function arguments
