URL Link: http://people.ischool.berkeley.edu/~haroon/Vega.html

I have created a visualization using vega.js.
I have plotted the variation of average stars for restaurant category in the year 2012. I have selected the categories 'French', 'Chinese', 'Italian', 'Mexican', 'Mediterranean', 'American (New)', 'Indian', 'Thai', 'Japanese'. The plot shows the change in average star rating for these nine categories over the year 2012. X-axis is the Month and Y-axis is the average star rating. Hover ever each line to highlight a particular category.



DATA EXTRACTION (vega.js.py):
I have used the yelp business and review datasets.

CALCUALTING AVG STARS FOR CATEGORIES
1) First from the business dataset I find the categories of each of the businesses.

2) Then using the review dataset, I read each review, get the business ID and star rating. For the business ID I get the categories (from step 1) and calculate the average stars for each category

3) I store the output as a CSV (data.csv) with data in the format "category, month, avgStars"



VISUALIZATION (Vega.html)
1) I visualize the data in data.csv file using vega.js

2) For each category I plot a graph with Month in X-axis and avg stars in Y-axis

3) Each category is represented by different colored graphs

4) Hover over each line to highlight a particular category