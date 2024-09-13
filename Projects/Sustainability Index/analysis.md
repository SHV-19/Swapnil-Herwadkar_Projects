Sustainability Report: Fashion Industry Trends and Insights

Introduction

This report is based on an analysis of the Sustainable Fashion Trends 2024 dataset and accompanying Sustainability Index Dashboard and Correlation Analysis. It provides an overview of sustainability trends in the fashion industry, focusing on key factors such as carbon emissions, water usage, waste production, material types, and sustainability ratings. The data was collected, transformed, and analyzed to understand the industry's progress toward more eco-friendly practices.

Data Collection and Transformation

Data Sources

The data was sourced from Kaggle and represents key metrics from fashion brands, such as:
•	Sustainability Rating (A to D, with A being the highest).
•	Material Types (e.g., Recycled Polyester, Hemp, Organic Cotton).
•	Environmental Impact Metrics:
o	Carbon Footprint (MT): Measured in metric tons of CO₂.
o	Water Usage (Liters): The amount of water consumed during production.
o	Waste Production (KG): The amount of waste generated during production.
o	Average Price (USD): The average cost of products offered by each brand.
•	Certification Types: GOTS, OEKO-TEX, Fair Trade, B Corp, etc.

Data Preparation

The dataset contained information for 5,000 fashion brands from 2010 to 2024. The data transformation process involved the following steps:

Data Cleaning:
   
o	Missing and erroneous values were handled appropriately (e.g., filling missing entries with averages or using forward-fill methods for time-series data).
o	Standardized values across brands to ensure consistency in measurements.

Encoding Categorical Data:

o	The Sustainability Rating (A, B, C, D) was converted into numerical values for analysis, where A=4, B=3, C=2, and D=1.
o	Material types and countries were encoded using the LabelEncoder for easier modeling and analysis.

Feature Engineering:

o	Derived features such as Average Carbon Footprint by Country and Yearly Waste Production Trends were created to enable more granular analysis.

Data Visualization:

o	A custom dashboard was created to visualize the Yearly Trends in Sustainability, Waste Production, and Water Usage.
o	The dashboard also highlighted Carbon Footprint by Country and Top Certification Counts.
Exploratory Data Analysis

Sustainability Ratings

•	Distribution: Sustainability ratings were skewed toward the middle (B and C), suggesting that most fashion brands are operating at a moderate level of sustainability. The few brands achieving an 'A' rating are likely making exceptional efforts in reducing their environmental impact.
Material Type Usage

•	Top Materials:

o	Recycled Polyester was the most frequently used material, with 867 occurrences.
o	Hemp and Vegan Leather were also widely adopted, suggesting that brands are exploring eco-friendly alternatives to traditional materials.
o	Organic Cotton had lower usage (817 occurrences), possibly due to higher costs or limited availability.



Correlation Analysis

Mean Squared Error for Sustainability Ratings Prediction: 1.3677109
Root Mean Squared Error for Sustainability Ratings Prediction: 1.1694917272046006

This RMSE shows that there is room to improve the model.

The correlation matrix (visualized in the heatmap) provided the following insights:

•	Weak Correlations: There was no significant correlation between sustainability ratings and key environmental metrics like carbon footprint, water usage, and waste production. This suggests that sustainability ratings are influenced by other factors not captured in this dataset, such as social impact or manufacturing processes.
•	Material Type and Environmental Impact: Material types, while important, did not show strong correlations with water usage, waste production, or carbon footprint. However, Recycled Polyester and Hemp showed slightly better performance in reducing waste.
•	Carbon Footprint: The data showed a weak negative correlation between carbon footprint and sustainability ratings, but the trend was not strong enough to draw firm conclusions.

Water Usage

•	Peak Water Usage: Water usage peaked in 2015, reaching approximately 2.7 billion liters. This could be attributed to increased production demands or water-intensive materials. However, the trend has declined slightly in recent years, with an average water usage of 2.2 billion liters in 2024.

Waste Production

•	Waste Management Improvements: Waste production peaked at 53,695 kg in 2016 but has been steadily declining, reaching an average of 45,518 kg in 2024. This suggests that fashion brands are becoming more efficient in managing waste, possibly through better recycling programs or reduced material waste during production.
Carbon Footprint by Country
•	High Emission Countries:
o	China and the USA consistently had the highest carbon emissions, with peaks at 11,986 MT and 4,303 MT, respectively. This highlights the need for more aggressive carbon reduction strategies in these countries, which are significant contributors to global emissions.
•	Lower Emission Countries:
o	European countries like France, Germany, and Italy showed lower carbon footprints, aligning with their stricter environmental regulations and greater emphasis on sustainability.

Top Certifications

•	GOTS and OEKO-TEX were the most widely adopted certifications, with over 1,000 instances each. These certifications ensure that brands are adhering to organic textile production standards and safe, eco-friendly practices in textile production.
•	B Corp and Fair Trade certifications, while less common, indicate a growing trend toward ensuring ethical labor practices and corporate social responsibility.
Certification Impact on Sustainability Ratings
•	Brands with multiple certifications tended to have slightly higher sustainability ratings, indicating that acquiring certifications like GOTS and Fair Trade can boost a brand's sustainability profile. 

Key Takeaways and Recommendations

Sustainability Rating Drivers

•	The analysis shows no strong correlation between environmental metrics (carbon footprint, water usage, waste production) and sustainability ratings. This suggests that sustainability ratings may be influenced by broader factors, such as labor practices, corporate policies, and the use of renewable energy sources.
•	Brands aiming for higher sustainability ratings should not only focus on reducing environmental impact but also consider improving labor practices and acquiring certifications to boost their scores.

Areas for Improvement

•	Water and Waste Management: While the fashion industry has made some progress in reducing waste and water usage, more aggressive measures are needed to bring down consumption to sustainable levels.
•	Carbon Emissions: High carbon-emitting countries like China and the USA must prioritize strategies to decarbonize their production processes. Adopting renewable energy, energy-efficient technologies, and carbon offset programs will be crucial for meeting global climate goals.

Material Innovation

•	The use of eco-friendly materials like Recycled Polyester, Hemp, and Vegan Leather is on the rise, but the adoption of more sustainable materials like Organic Cotton and Tencel should be encouraged.
•	Innovation in material sourcing and production processes can significantly reduce the overall environmental footprint of the fashion industry.

Conclusion

The fashion industry is making strides in sustainability, particularly in terms of waste and water management. However, the weak correlation between sustainability ratings and environmental metrics suggests that a holistic approach, including social responsibility and labor practices, is key to achieving higher sustainability standards. Brands must continue to innovate in material usage, improve transparency in sustainability reporting, and adopt stricter environmental practices to ensure long-term sustainability.
By focusing on these areas, the fashion industry can contribute to a more sustainable future while meeting growing consumer demand for eco-friendly and ethically produced goods.

Data Sources: Kaggle, Sustainable Fashion Trends 2024 Dataset, Custom Sustainability Index Dashboard
Prepared by: Swapnil Herwadkar



