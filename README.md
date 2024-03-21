# Vehicle Sales Exploratory Data Analysis

The [Vehicle Sales and Market Trends Dataset](https://www.kaggle.com/datasets/syedanwarafridi/vehicle-sales-data) dataset is a publicly available dataset from Kaggle, published by Syed Anwar in February 2024. It provides a comprehensive collection of information about the sales transactions of various vehicles from the years 2014 to 2015. This dataset encompasses details such as the manufacture year, make, model, trim, body type, transmission type, VIN (Vehicle Identification Number), state of registration, condition rating, odometer reading, exterior and interior colors, seller information, Manheim Market Report (MMR) values, selling prices, and sale dates.

This data science project aims to perform exploratory market analysis on the Automotive Market, gleaning insight into consumer preferences and demands, sales trends, and pricing fluctuations based on various factors. The resulting insights can help automotive dealers and industry professionals better understand consumer preferences and make informed decisions on catering to their needs.

## **Final Columns**

<details>
  <summary>These are the final columns comprising the ETL pipeline's resulting data set.</summary>

- **Year** - The manufacturing year of the vehicle.
- **Make** - The brand or manufacturer of the vehicle.
- **Model** - The specific model of the vehicle.
- **Trim** - Additional designation for the vehicle model.
- **Body** - The body type of the vehicle (e.g., SUV, Sedan).
- **Transmission** - The transmission type of the vehicle (e.g., automatic).
- **Vehicle Identification Number** - A unique code designated to each vehicle.
- **State Code** - The two-letter code of the state where the vehicle is registered.
- **Odometer** - The mileage or distance traveled by the vehicle.
- **Color** - Exterior color of the vehicle.
- **Interior** - Interior color of the vehicle.
- **Seller** - The entity selling the vehicle.
- **Market Price** - The estimated market value of the vehicle based on the Manheim Market Report.
- **Selling Price** - The price at which the vehicle was sold.
- **Sale Date** - The date when the vehicle was sold.
</details>

## **Grain Columns**

<details>
  <summary>These columns are implemented to introduce more granularity into the final data set.</summary>

- **State** - The state where the vehicle is registered.
- **Sale Year** - Year the vehicle was sold.
- **Sale Month** - Month number the vehicle was sold.
- **Sale Month Name** - Name of the month the vehicle was sold.
- **Sale Day of Week** - Day of week the vehicle was sold.
- **Sale Day Name** - Name of the day the vehicle was sold.
- **Sale Month Short Name** - Short name of the month the vehicle was sold.
</details>

## Business Questions

<details>
  <summary><strong>Sales Inquiries</strong></summary>
  <div>
    <p><i>What is the disparity between the annual average reported market prices and the selling prices of vehicles from 2014 to 2015, and what has been the overall trend?</i></p>
    <div align="center">
      <img src="https://raw.githubusercontent.com/heischichou/Vehicle-Sales-Analysis/main/assets/Market%20Vs%20Selling%20Price.png"></img>
    </div>
    <br>
    <p align="justify">&nbsp;&nbsp;The results indicate that between 2014 and 2015, both the annual average reported market and selling prices of vehicles rose in value. Moreover, analyzing the annual average reported market and selling prices during that time reveals a fascinating trend. In 2014, the average market price was $12,945.37, while the average selling price was slightly lower at $12,735.92, resulting in a disparity of $209.45. Meanwhile, in 2015, the average market price increased to $13,903.61, and the average selling price also increased to $13,768.14, resulting in a smaller disparity of $135.47. These findings suggest that vehicles are being sold at prices closer to their market price in 2015 compared to 2014; this implies that the disparity between the average reported market prices and the average selling prices of vehicles is narrowing over time.</p>
  </div>
  <br>
  <div>
    <p><i>What are the quarterly sales figures over the years?</i></p>
    <div align="center">
      <img src="https://raw.githubusercontent.com/heischichou/Vehicle-Sales-Analysis/main/assets/Quarterly%20Sales%202015.png"></img>
    </div>
  </div>
  <br>
  <div>
    <p><i>What are the highest-grossing vehicle types overall?</i></p>
    <div align="center">
      <img src="https://raw.githubusercontent.com/heischichou/Vehicle-Sales-Analysis/main/assets/Highest%20Sales%20by%20Vehicle%20Body%20Type.png"></img>
    </div>
    <br>
    <p align="justify">&nbsp;&nbsp;The results highlight the diverse preferences of consumers for different vehicle types in the U.S. automotive market; in terms of gross sales value, Sedans are the highest-grossing vehicle type overall, with a total sales value exceeding $2.4 billion. SUVs follow closely behind, with sales totaling $1.89 billion—indicating their popularity and strong market demand. Crew Cabs, Minivans, and Coupes trail behind with considerably less but still significant gross sales values of $296 million, $243 million, and $242 million, respectively. Hatchbacks and SuperCrews round out the list with sales values of $236 million and $164 million, respectively. These findings suggest that consumers prefer to purchase vehicles with comfortable and practical accommodations for four or more passengers.</p>
  </div>
</details>

<details>
  <summary><strong>Product Inquiries</strong></summary>
  <div>
    <p><i>What are the highest-grossing vehicle types by manufacture year?</i></p>
    <div align="center">
      <img src="https://raw.githubusercontent.com/heischichou/Vehicle-Sales-Analysis/main/assets/Highest%20Grossing%20Vehicle%20Types%20by%20Manufacturing%20Year.png"></img>
    </div>
  </div>
  <br>
  <div>
    <p><i>What are the highest-selling vehicle types by manufacture year?</i></p>
    <div align="center">
      <img src="https://raw.githubusercontent.com/heischichou/Vehicle-Sales-Analysis/main/assets/Highest%20Selling%20Vehicle%20Types%20by%20Manufacturing%20Year.png"></img>
    </div>
  </div>
  <br>
  <p align="justify">&nbsp;&nbsp;As seen above in the figures above, the results on the top 3 highest-grossing and highest-selling vehicle types (Sedan, SUV, and CrewCab) by manufacture year from 2011 to 2015 demonstrate the following insights:</p>
  <ul>
    <li align="justify">Across their manufacturing years, Sedans are consistently the highest-grossing and highest-selling vehicle type at 206,429 units sold for $2.4 billion in total revenue. SUVs follow behind at 117,229 units sold for $1.89 billion in revenue, and CrewCabs at 13,627 units sold for $296 million. These figures suggest that Sedans are the prime choice of vehicle in the automotive industry among consumers, manufacturers, and dealers alike, and continue to generate significant demand and revenue regardless of their manufacture year.</li>
    <li align="justify">There are considerable variances in sales among distinct manufacturing years, indicating fluctuations in market demand. Notably, as newer vehicle models enter the market and displace older models, cumulative sales experienced a downward trend in revenue and the number of units sold; this implies that consumers prefer to purchase older models, or possibly, there is a decline in the automotive market over time.</li>
  </ul>
  <p align="justify">These results overall show that the United States is a lucrative market for vehicle dealers and manufacturers.</p>
</details>

<details>
  <summary><strong>Brand Inquiries</strong></summary>
  <div>
    <p><i>What are the top 5 brands in terms of total sales?</i></p>
    <div align="center">
      <img src="https://raw.githubusercontent.com/heischichou/Vehicle-Sales-Analysis/main/assets/Top%20Brands%20by%20Total%20Sales.png"></img>
    </div>
    <br>
    <p align="justify">&nbsp;&nbsp;The results illustrate the strong performance of automotive brands in the U.S. market in sales volume and market share. At the top spot, Ford emerges as a clear leader in the U.S. automotive industry with a gross sales value of roughly $1.16 billion, showcasing its strong market presence and consumer appeal. Chevrolet follows at a considerably lower market share than Ford at $621 million. Nissan and Toyota trail behind with competitive gross sales values of $507 million and $427 million, respectively. Lastly, BMW is the 5th top brand with a gross sales value of $362 million, highlighting its success in capturing a large consumer base.</p>
  </div>
  <br>
  <div>
    <p><i>What are the top 5 brands in terms of how many vehicles they sold?</i></p>
    <div align="center">
      <img src="https://raw.githubusercontent.com/heischichou/Vehicle-Sales-Analysis/main/assets/Top%20Brands%20by%20Number%20of%20Vehicles%20Sold.png"></img>
    </div>
    <br>
    <p align="justify">&nbsp;&nbsp;These results illustrate the strong performance of automotive brands in the U.S. market in terms of sales volume and market share. Based on the number of vehicles sold, Ford leads the U.S. market with a total of 78,858 units, capturing a significant market share of 33.50%. Chevrolet follows with 52,580 sold, comprising 22.34% of the market. Nissan and Toyota trail behind with 43,128 and 34,463 units sold, respectively, showing their competitive positions in the automotive industry. Lastly, Dodge is the 5th top brand, with 26,634 vehicles sold, representing 11.20% of the market.</p>
  </div>
</details>

<details>
  <summary><strong>Consumer Preferences</strong></summary>
  <div>
    <p><i>What are the most common vehicle body types?</i></p>
    <div align="center">
      <img src="https://raw.githubusercontent.com/heischichou/Vehicle-Sales-Analysis/main/assets/Most%20Common%20Vehicle%20Body%20Type.png"></img>
    </div>
    <br>
    <p align="justify">&nbsp;&nbsp;The results illustrate the popularity of different vehicle types available in the U.S. automotive market. In terms of total units sold, the most common vehicle type is Sedans, with a total of 206,429 units sold (47.55%). The remaining most common vehicles are SUVs at 117,229 units (27.01%), Hatchbacks at 23,184 units (5.34%), Minivans at 21,429 units (4.94%), Coupes at 5,537 units (3.54%), Wagons at 13,816 units (3.18%), and Crew Cabs at 13,627 units (3.14%), Convertibles at 8,935 units (2.06%), SuperCrews at 7,278 units (1.68%), and lastly, G Sedans at 6,812 units (1.57%).</p>
  </div>
  <br>
  <div>
    <p><i>What are the most common vehicle colors?</i></p>
    <div align="center">
      <img src="https://raw.githubusercontent.com/heischichou/Vehicle-Sales-Analysis/main/assets/Most%20Common%20Vehicle%20Colors.png"></img>
    </div>
    <br>
    <p align="justify">&nbsp;&nbsp;The results illustrate the popularity of color choices in the U.S. automotive market. In the number of units sold under the specific color, the most common vehicle color is Black, with a total of 90,446 units (21.25%). The remaining most common vehicle colors are White at 86,860 units (20.41%), Silver at 69,167 units (16.25%), Gray at 68,734 units (16.15%) and Blue at 44,622 units (10.48%), Red at 40,372 units (9.49%), Gold at 14,795 units (3.48%), and lastly, Purple at 10,644 units (2.5%). These findings suggest that monotone or grayscale colors are the most popular among vehicle owners and manufacturers in the U.S.</p>
  </div>
  <br>
  <div>
    <p><i>What is the most common vehicle transmission type?</i></p>
    <div align="center">
      <img src="https://raw.githubusercontent.com/heischichou/Vehicle-Sales-Analysis/main/assets/Most%20Common%20Vehicle%20Transmission%20Type.png"></img>
    </div>
    <br>
    <p align="justify">&nbsp;&nbsp;These results indicate that out of a total of roughly 459,400 vehicles, a small proportion, 15.7K vehicles (3.42%) are Manual transmissions, while the vast majority, 443.6K vehicles (96.58%) are Automatic transmissions. Overall, the results suggest that automatic vehicles are the preferred choice of vehicle transmission among vehicle owners and manufacturers.</p>
  </div>
</details>

<details>
  <summary><strong>Geographical Inquiries</strong></summary>
  <div>
    <p><i>Which states have the highest number of vehicles registered?</i></p>
    <div align="center">
      <img src="https://raw.githubusercontent.com/heischichou/Vehicle-Sales-Analysis/main/assets/Top%20States%20with%20Most%20Vehicles%20Sold.png"></img>
    </div>
    <br>
    <p align="justify">&nbsp;&nbsp;These results illustrate the distribution of registered vehicles across the United States. Florida has the highest number of registered vehicles, totaling 73,405 units, highlighting its large population and high vehicle ownership rate. California follows closely behind with 63,579 units, reflecting its status as the most populous state. Texas—with 40,393 units, also features prominently on the list, owing to its significant presence in the automotive landscape as a manufacturing and transportation export base. The remaining states with the highest number of vehicles sold are Georgia at 29,761 units, Pennsylvania at 23,522 units, New Jersey at 22,578 units, Illinois at 21,144 units, Ohio at 19,771 units, Tennessee at 18,476 units, and lastly, North Carolina at 18,040 units. These results overall affirm the high demand for vehicles in states hosting large populations.</p>
  </div>
</details>

<details>
  <summary><strong>Other Inquiries</strong></summary>
  <div>
    <p><i>Which vehicle types have the highest median mileage?</i></p>
    <div align="center">
      <img src="https://raw.githubusercontent.com/heischichou/Vehicle-Sales-Analysis/main/assets/Median%20Mileage%20by%20Vehicle%20Body%20Type.png"></img>
    </div>
  </div>
</details>
