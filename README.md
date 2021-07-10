# Car Dealership Management System
## FSDI 111 Assignment
The owner of a successful used car dealership would like you to build a web application that allows them to see what they have in stock. Sometimes, some cars need to be moved to a different location so that higher profile vehicles can be displayed out front. The secondary location is a couple of blocks away and it is where lower-end vehicle are kept, but often these are excellent choices for people with a lower budget.

At any given time, this car dealership has over 100 cars in stock distributed across two car lots and they are all used cars meaning no two are exactly alike (in terms of conditions, make, model, etc). The goal is for us to give our sales personnel a tool for them to be able to view the full inventory so that they can offer or suggest other vehicles we have in stock whenever a buyer's first choice is unavailable to them for whatever reason; Sort of like a second option. These second options end up amounting to a large bulk of the dealerships sales as buyers will often settle for a cheaper car than the one they originally walked in for if it is within their budget and satisfies their needs.

To build this system, the owner has asked that you created a system that allows employees to:

1. Register new vehicles by specifying their: make, model, mileage, color, VIN (vehicle identification number), condition (a range of: excellent, good, fair, bad, very bad), cost (to us), retail price, an optional text description and between 1 and 3 pictures of the vehicle.

2. View the full inventory list containing the car's make, model and color per each record we actively have in stock.

3. Update records to fix mistakes.

4. Delete cars we no longer hold in stock (soft delete in case we ever want to analyze what cars sell the most in the future).

5. View single car entries by clicking on them from the inventory list thus allowing us to see all of its registered attributes (all the features specified in item #1).