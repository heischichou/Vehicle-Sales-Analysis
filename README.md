# Vehicle Sales Exploratory Data Analysis
The [Vehicle Sales and Market Trends Dataset](https://www.kaggle.com/datasets/syedanwarafridi/vehicle-sales-data) dataset is a publicly available dataset from Kaggle, published by Syed Anwar in February 2024. It provides a comprehensive collection of information about the sales transactions of various vehicles from the years 2014 to 2015. This dataset encompasses details such as the manufacture year, make, model, trim, body type, transmission type, VIN (Vehicle Identification Number), state of registration, condition rating, odometer reading, exterior and interior colors, seller information, Manheim Market Report (MMR) values, selling prices, and sale dates.

This data science project aims to perform exploratory market analysis on the Automotive Market, gleaning insight into consumer preferences and demands, sales trends, and pricing fluctuations based on various factors. The resulting insights can help automotive dealers and industry professionals better understand consumer preferences and make informed decisions on catering to their needs.

## **Final Columns**
<details>
  <summary>These are the final columns comprising the ETL pipeline's resulting data set.</summary>

  + **Year** - The manufacturing year of the vehicle.
  + **Make** - The brand or manufacturer of the vehicle.
  + **Model** - The specific model of the vehicle.
  + **Trim** - Additional designation for the vehicle model.
  + **Body** - The body type of the vehicle (e.g., SUV, Sedan).
  + **Transmission** - The transmission type of the vehicle (e.g., automatic).
  + **Vehicle Identification Number** - A unique code designated to each vehicle.
  + **State Code** - The two-letter code of the state where the vehicle is registered.
  + **Odometer** - The mileage or distance traveled by the vehicle.
  + **Color** - Exterior color of the vehicle.
  + **Interior** - Interior color of the vehicle.
  + **Seller** - The entity selling the vehicle.
  + **Market Price** - The estimated market value of the vehicle based on the Manheim Market Report.
  + **Selling Price** - The price at which the vehicle was sold.
  + **Sale Date** - The date when the vehicle was sold.
</details>

## **Grain Columns**
<details>
  <summary>These columns are implemented to introduce more granularity into the final data set.</summary>

  
  + **State** - The state where the vehicle is registered.
  + **Sale Year** - Year the vehicle was sold.
  + **Sale Month** - Month number the vehicle was sold.
  + **Sale Month Name** - Name of the month the vehicle was sold.
  + **Sale Day of Week** - Day of week the vehicle was sold.
  + **Sale Day Name** - Name of the day the vehicle was sold.
  + **Sale Month Short Name** - Short name of the month the vehicle was sold.
</details>

## Business Questions
<details>
  <summary><strong>Sales Inquiries</strong></summary>
  <div>
    <p><i><i>What is the trend of market price versus selling price over the years?</i></i></p>
    <div align="center">
      <img src="https://raw.githubusercontent.com/heischichou/Vehicle-Sales-Analysis/main/assets/Market%20Vs%20Selling%20Price.png"></img>
    </div>
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
</details>

<details>
  <summary><strong>Brand Inquiries</strong></summary>
  <div>
    <p><i>What are the top 5 brands in terms of total sales?</i></p>
    <div align="center">
      <img src="https://raw.githubusercontent.com/heischichou/Vehicle-Sales-Analysis/main/assets/Top%20Brands%20by%20Total%20Sales.png"></img>
    </div>
  </div>
  <br>
  <div>
    <p><i>What are the top 5 brands in terms of how many vehicles they sold?</i></p>
    <div align="center">
      <img src="https://raw.githubusercontent.com/heischichou/Vehicle-Sales-Analysis/main/assets/Top%20Brands%20by%20Number%20of%20Vehicles%20Sold.png"></img>
    </div>
  </div>
</details>

<details>
  <summary><strong>Consumer Preferences</strong></summary>
  <div>
    <p><i>What are the most common vehicle body types?</i></p>
    <div align="center">
      <img src="https://raw.githubusercontent.com/heischichou/Vehicle-Sales-Analysis/main/assets/Most%20Common%20Vehicle%20Body%20Type.png"></img>
    </div>
  </div>
  <br>
  <div>
    <p fontWeight="bold">What are the most common vehicle colors?</i></p>
    <div align="center">
      <img src="https://raw.githubusercontent.com/heischichou/Vehicle-Sales-Analysis/main/assets/Most%20Common%20Vehicle%20Colors.png"></img>
    </div>
  </div>
  <br>
  <div>
    <p><i>What is the most common vehicle transmission type?</i></p>
    <div align="center">
      <img src="https://raw.githubusercontent.com/heischichou/Vehicle-Sales-Analysis/main/assets/Most%20Common%20Vehicle%20Transmission%20Type.png"></img>
    </div>
</details>

<details>
  <summary><strong>Geographical Inquiries</strong></summary>
  <div>
    <p><i>Which states have the highest number of vehicles registered?</i></p>
    <div align="center">
      <img src="https://raw.githubusercontent.com/heischichou/Vehicle-Sales-Analysis/main/assets/Top%20States%20with%20Most%20Vehicles%20Sold.png"></img>
    </div>
  </div>
  <br>
  <div>
    <p><i>What are the most common vehicle types across all states?</i></p>
    <div align="center">
      <img src="https://raw.githubusercontent.com/heischichou/Vehicle-Sales-Analysis/main/assets/Most%20Common%20Vehicle%20Body%20Type.png"></img>
    </div>
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