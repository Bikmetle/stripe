django + stripe api project for Rishat's company


We have 3 items with the following fields: name, description, price

By making GET request to /buy/{id} you'll get Stripe Session Id for the chosen item.
By making GET request to /item/{id} you'll get html page for buying the chosen item.
