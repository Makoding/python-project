This app suggests to the user how many calories should eat today. The result is based on user's weight, height, age and the temprature of the user's location (country and city) .
Running the main.py file displays you a link which gets you to a webpage that explains the cause of this app. 
There, through an additional link, the users get access to the calories calculation form page where they can put their necessary data for calculating their calorie intake and then by clicking on the calculate button they get their results.
The web pages are written in HTML and the Calories Calculation Form page has also CSS graphics.

There is a bit of web scraping aslo happening because the temprature parameter is extracted from the timeanddate.com site. 
The user's country and city input are added to the site's url and by copying the xml path to a .yaml file i was able to do the extraction.

