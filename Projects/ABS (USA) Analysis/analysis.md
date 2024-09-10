INTRODUCTION

Alcohol consumption in the United States has been steadily growing for years. Per capita, Americans now consume 2.51 gallons of alcohol, a growth of over 15 percent compared to 20 years ago. (Statista.com)
Alcohol Beverage Services (ABS) is essential for managing inventory and reducing breakage of alcoholic beverages. This report examines data from two primary datasets: breakage logs and store inventory. Our analysis focuses on:
•	Identifying the products most prone to breakage.
•	Discovering potential correlations between breakage and factors such as sales volume.
•	Understanding current inventory levels across various categories.
•	Gaining insights into pricing and discount strategies.
By exploring these aspects, we aim to offer valuable recommendations for optimizing inventory management, minimizing breakage costs, and maximizing profitability for ABS.

METHODS

Data Acquisition

Data was sourced from two files 'Alcohol_Beverage_Services_Breakage_Inventory: a log of breakages or wasted inventory.xlsx' file and ‘ABS_Store_Inventory_and_Sale_Item: ABS’s listing of inventory items, including store quantities and sale prices.xlsx’ , covering the period from 2001 to 2023.
These datasets were instrumental in creating visualizations that offered insights into inventory levels and breakage trends, aiding the organization's leaders in making strategic decisions to enhance operational efficiency and reduce losses.
Data Preparation
The acquired data underwent a thorough review to identify and address any inconsistencies or missing values. In the dataset titled "Alcohol Beverage Services Breakage Inventory: A Log of Breakages or Wasted Inventory.xlsx," a few missing values were detected. These incomplete records were filtered out after determining that they contributed to inaccurate and unreliable inputs.
Several adjustments were made to ensure data consistency. Specifically, the date format in the dataset was inconsistent, necessitating formatting to standardize it. The data was then sorted in chronological order, starting from the oldest date. Additionally, column names were modified for better coherence and visual appeal:
•	"Date" was renamed to "Date Logged"
•	"Code" was changed to "Item Code"
•	"Item description" was capitalized to "Item Description"
These changes enhanced the dataset's readability and usability for subsequent analysis.
For the second dataset, ‘ABS_Store_Inventory_and_Sale_Item: ABS’s listing of inventory items, including store quantities and sale prices.xlsx,’ data cleaning was performed. The column ‘Sale Data’ was removed as they did not contribute to the report's objectives. The ‘Inventory’ column was left untouched to maintain data integrity, with zero values indicating out-of-stock products and negative values representing breakages and faulty products. Additionally, column names were modified for improved clarity and consistency. Size column was formatted to maitain data integrity, oz is the standard measure. All values having garbage value were formatted with correct unit of measure. 
•	"Code" was changed to "Item Code"
•	"Description" was changed to "Item Description"
•	“Price’ column was formatted to currency with 2 decimals”

Tools and Softwares 

Microsoft Excel (Cleaning&Preparation)
Tableau (Visualization)

Visualization Techniques

Bar Chart: Top 5 Products with Highest Breakage
Rows: Item Description (Filtered by Top 5 Products)
Columns: Breakage Quanity (SUM(Quanity)
Sorting: By Breakage Count (highest to lowest)
Additional Visualition Efforts: Quantity in Color Mode. Data Labels were added.

Line Chart: Breakage Trends Over Time

Rows: Quantity
Columns: Date Logged (Years/Timeline)
Sorting: By Breakage Count (highest to lowest)
Additional Visualition Efforts: Quantity in Color Mode. Data Labels were added.

Bar Chart: Comprehensive Inventory Status Overview
Rows: Category (Filtered by Top 3 Categories)
Columns: Inventory Quanity (SUM(Total Inventory)
Sorting: Category (highest to lowest)
Additional Visualition Efforts: Total Inventory in Color Mode. Data Labels were added.

Pie Chart: Product Category Percentage Breakdown 
Rows: Total Inventory (Qucik Calculation, %Total)
Columns: Category (Filtered for Top 15 Category)
Sorting: Category (highest to lowest)
Additional Visualition Efforts: Category in Color Mode. Legend was sorted with highest to lowest percentage. Total Inventory added to Angle, Size mode. Data labels were added.

Bar Chart:  Inventory Status for Item Code: 92452
Rows: Inventory Status, Item Code (Item Code filtered for Item Code: 92452)
Additional Visualition Efforts: Total Inventory in Color Mode. Data Labels were added.
Caluclated Field: Inventory Status: 
IF [Total Inventory] = 0 THEN "Out of Stock"
ELSEIF [Total Inventory] < 0 THEN "Faulty"
ELSE "In Stock"
END

Bar Chart:  Inventory Pricing
Rows: Item Description
Column: Price, SUM)Total Price
Additional Visualition Efforts: Price, Total Price in Color Mode. Data Labels were added.
Caluclated Field: Total Price: 
[Price] * [Total Inventory]

Highlight Tables:  Best Discounts
Rows: Discount Percentage
Column: Item description (Filtered on Top 10)
Additional Visualition Efforts: Discount Percentage in Color Mode. Data Labels were added.
Caluclated Field: Discount Percentage: 
([Price] - [Sale Price]) / [Price] * 100

REPORT

What are the top 5 products with breakages?

Covering a period from 2001 to 2022, these were the Top 5 Products with breakages.
1.	Coors Lite
2.	Miller Lite
3.	Corona Extra
4.	Heineken
5.	Modelo Especial

Is there any seasonality or time relationship to the breakages?
 
Before the outbreak of the pandemic, alcohol sales in the United States had been rising for years. 2020 was a sharp reversal of this trend. In 2022, sales of alcoholic beverages finally reached and surpassed pre-pandemic levels at 259.8 billion U.S. dollars. (Statista.com)
In 2022, total alcoholic beverage sales numbers in the United States reached nearly 260 billion U.S. dollars. U.S. sales numbers had been increasing for years prior to the COVID-19 pandemic. Supplier gross revenue was highest revenue was highest in the spirits segment at 37.58 billion U.S. dollars. (Statista.com)
According to a report from Statista (https://www.statista.com/), total alcoholic beverage sales in the US have increased steadily over the years, potentially peaking in 2019 (pre-pandemic). United States alcohol sales were a little over $252 billion in 2019.(Overproof).  It was observed that there was a decrease in alcohol consumption in 2021, likely due to the pandemic. The stockpiling behavior observed in 2020 due to pandemic uncertainty might be an outlier.
This analysis suggests that breakage might be more correlated with sales volume than seasonality. Higher-selling products experience more handling, distribution, and shipment, potentially leading to greater breakage. Breakage trends may show consistency over time, with disruptions only during unforeseen events like a pandemic.

What product “category” does ABS have the highest amount of inventory of?
 
Among spirits, U.S. consumers prefer vodka by a wide margin. Seventy-seven million 9-liter bottles of vodka are consumed every year. (Alcohol.org)
This visualization/analysis indicates that vodka was the most sought-after category in the US, with the highest inventory levels across all categories. This observation is supported by a report from Alcohol.org, which highlights that vodka is the most consumed category of alcohol. Consequently, high inventory levels are maintained to meet the substantial demand.
 
Show the product “category” percentage breakdowns using a pie chart or donut chart.
 
As analyzed earlier, Vodka comprises 15.71% of the total inventory among the top 15 categories.
What is the inventory level for the specific product “code” 92452? Why might that value be negative from a supply chain perspective?
The inventory system tracks stock levels, and a negative value indicates we have fewer items available than what's listed (potentially due to breakage or faulty products). For instance, analysis showed Item Code 92452 with a negative inventory, suggesting there might be damaged items in stock.
 
What product has the highest price?

From the analysis, it was concluded that 'Remy Martin Louis XIII Cognac' was the highest priced product in the inventory, priced at $4,800. Additionally, Tito’s Handmade Vodka had the highest total inventory value at $230,107, followed by J.D. Whiskey and other products.

Of the products with sale prices, which one(s) have the best discount vs. their typical price?
 
From the analysis, Coppola Diamond Prosecco and Coppola Diamond Rosé Prosecco offered the highest discount at 31.5%, followed by D’usse VSOP Cognac at 28.8%.

What is the range of sizes for the beverages ABS sells?

The sizes were divided into two major units of measure: milliliters to liters, and ounces. The size range for ounces is from 0.51 oz to 96 oz, while the range for milliliters to liters is from 100 ml to 19 liters.

Does ABS sell anything other than beverages? If so, what do they sell and what is the corresponding price of the product?
Yes, ABS sell Whiskey Rocks T-SHIRT apart from beverages. It is priced at 14.99$

Do you think it is possible to combine the breakage and inventory datasets? If so, how would you combine the datasets / what information would you need to merge the information?

Merging Breakage and Inventory Data
While merging the breakage and inventory datasets using "Item Code" as the primary key is technically possible with functions like UNION or LEFT JOIN, data quality issues pose a significant challenge.
Obstacles:
•	Inconsistent Data: Different item descriptions for the same code indicate a lack of data integrity.
•	Missing Data: Missing item codes in one or both data sets can hinder the merger.
Recommended Approach:
Data Cleaning:
•	Standardize item descriptions across both datasets.
•	Identify and address missing values (if possible).
•	Check for duplicate entries.
Merge Strategy:
•	LEFT JOIN: Includes all items from the inventory, even if there's no breakage data.
•	INNER JOIN: Only includes items with matching codes in both datasets.
By cleaning and preparing the data, you can achieve a more accurate and informative merged dataset that reflects the actual breakage and inventory situation.
While combining these datasets based on "Item Code" is feasible, it hinges on resolving the current data quality issues. This would involve data discovery efforts to identify and rectify inconsistencies and missing values.

RESULT & CONCLUSION

This analysis of alcohol beverage data from ABS yielded valuable insights into breakage trends, inventory levels, and product categories. Here's a summary of the key findings:
Breakage:
The top 5 products experiencing the most breakage were all popular beer brands. This potentially relates to high sales volume and handling during distribution.
Breakage trends may not be seasonal, but rather correlate with sales volume. Higher-selling products see more handling and potentially more breakage.
Inventory:
Vodka had the highest inventory levels, aligning with its popularity among U.S. consumers.
Negative inventory values for specific items indicate damaged or faulty products in stock.
Pricing and Discounts:
Remy Martin Louis XIII Cognac was the most expensive item.
Coppola Diamond Prosecco and D’usse VSOP Cognac offered the highest discounts.
Data Integration:
While merging breakage and inventory data by "Item Code" is possible, data quality issues pose challenges.
Resolving inconsistencies in descriptions and missing values is crucial before merging.

Conclusion:

This data analysis provides valuable insights into ABS's inventory management and breakage patterns. Addressing data quality issues will allow for a more comprehensive analysis by merging the breakage and inventory datasets. This would offer a clearer picture of breakage costs and potential areas for improvement in handling high-volume products.
Additional Notes:
The analysis identified ABS selling a non-beverage item - Whiskey Rocks T-Shirt.
The size range for beverages was identified in ounces (0.51 oz to 96 oz) and milliliters/liters (100 ml to 19 liters).

REFERENCES

Alcohol.org (2023, June). The Alcohol Industry in Data. Retracted on 6/15/2024
Footnote: https://alcohol.org/guides/the-alcohol-industry-in-data/ 
McCarty, S. (2020, November 18). Alcohol sales data and trends. Overproof [Online]. Retractred from https://overproof.com/2020/11/18/alcohol-sales-data-and-trends/ on 6/14/2024
Statista. (2023, June 07). Alcoholic beverages industry in the United States [Topic overview]. Retracted from https://www.statista.com/topics/8803/alcoholic-beverages-industry-in-the-united-states/#topicOverview on 6/15/2024
Statista. (2023, June 07). U.S. total alcoholic beverages sales since 1990. Retracted from https://www.statista.com/statistics/207936/us-total-alcoholic-beverages-sales-since-1990/ on 6/14/2024
Yahoo! Finance. (2022). Top 10 best-selling beers in the US. Retracted from https://finance.yahoo.com/news/25-top-selling-beers-america-040529506.html on 6/14/2024
