# Module 3 Project
# Northwind Traders Hypothesis Testing

Northwind Traders is a fictitious company that connects buyers and sellers around the world. I have investigated 4 questions using hypothesis testing and provided recommendations for furthing company growth.

<a href="0_Data_Exploration.ipynb">Data Exploration</a>

<a href="https://docs.google.com/presentation/d/13S-cCuHyVbKEIIxlDAow6rFU5phzE8Ck90G_k4r0l5E/edit?usp=sharing">Presentation</a>

<a href="https://medium.com/@savannahmcamis/hypothesis-testing-for-discounts-6fdd56a953f">Blog Post</a>

## Question 1
<a href="1_Discounts.ipynb">Discounts</a>

Does discount amount have a statistically significant effect on the quantity of a product in an order? If so, at what level(s) of discount?
𝐻𝑜:𝜇1=𝜇2
𝐻𝑎:𝜇1<𝜇2

### Methodology
First, I compare the means of the quantities purchased with and without discounts. Then I compare the means of the quantities purchased with the major levels of discount. I use resampling to create a sampling distribution to satisfy the normality assumption of the major hypothesis tests. I run a one-tailed Welch's T-Test to compare the means of the two groups. Finally, I use an ANOVA test and a Tukey Test to compare the levels of discount. I then explain my results and recommendations.

### Results
Based on the results to hypothesis testing, I conclude that adding a discount to a product has a statistically significant effect on the quantity purchased. The level of discount matters only slightly. Discounts of 10% are not statistically significant, but other levels are. There is no statistical significance in the quantity ordered at discount levels of 5%, 15%, 20%, or 25%.

### Recommendations
I recommend that Northwind offer discounts of 5% as an incentive to increase quantity ordered. Higher discounts do not lead to higher quantities. As a result, discounts higher than 5% would most likely decrease gross revenue. Discounts do have a statistically significant effect on quantity ordered as opposed to no discount. In particular, Northwind should target customers who are not currently receiving a lot of discounts, and begin offering them minor discounts on all products. They should also lower all discount amounts to 5%.


## Question 2
<a href="2_Product_Category.ipynb">Product Category</a>

Do some types of products bring in more gross revenue than others?
𝐻𝑜:𝜇1=𝜇2=...=𝜇𝑛
𝐻𝑎:𝜇1<𝜇𝑖

### Results
The two categories that bring in the highest average gross revenue are Meat/Poultry and Produce. Beverages have the lowest average gross revenue but also the most outliers. The largest effect size is between Produce vs Beverages.

### Recommendations
I recommend that Northwinds focus their sales efforts toward products in the categories of Produce and Meat/Poultry as these categories bring in the highest average gross revenue.

## Question 3
<a href="3_Customer_Region.ipynb">Customer Region</a>

Are there significant differences between demand for various customer regions?
𝐻𝑜:𝜇1=𝜇2=...=𝜇𝑛
𝐻𝑎:𝜇1≠𝜇𝑖

### Results
When comparing the regions, I determined that the largest and most profitable orders come from North America and Western Europe. I also found that orders in Southern Europe, Northern Europe, and the British Isles are typically smaller. These results held for both quantity ordered and gross revenue.

### Recommendations
More rapport with customers needs to be built within Southern and Northern Europe. Additionally, more time should be spent on these customers because typically their orders are smaller. I would recommend hiring a product manager who has experience in those regions to help boost sales there.

## Question 4
<a href="4_Employee_Performance.ipynb">Employee Performance</a>

Are there statistically significant differences in the average annual gross revenue between employees?
𝐻𝑜:𝜇1=𝜇2=...=𝜇𝑛
𝐻𝑎:𝜇1≠𝜇𝑖

### Results
I can conclude that there is a statistically significant difference in the level of gross revenue brought in by different employees. Employees 1, 2, and 5 are the highest performing employees in terms of gross revenue. Employees 3 and 6 are the worst performing employees.

### Recommendations
These results can be used to strategize ways to boost employee performance. Since employees 1, 2, and 5 bring in the most gross revenue, perhaps they could host a training session for the other employees to share their best practices. I have also identifed that employees 3 and 6 may require additional support and training to hone their sales skills. This analysis could also be used as a basis for employee bonuses and awards to boost employee satisfaction.


## Future Work
1. The biggest future work revolves around profitability. Since there was no way to determine the cost of goods sold, I could only make inferences about total revenue and not profit. Ideally, I'd be able to analyze the profitability of each order so that I could evaluate each order on its contribution to the company's overall financial health.
2. I'd like to make employee evaluation metrics annual or monthly. Instead of seeing their total orders place, seeing the number of sales each employee has per year since they started with the company. This would allow me to evaluate the growth progression of employees, and identify employees who need additional help. 
3. Determine if order size has an effect on processing and shipping time, and if certain shippers have better response times for different sized orders.
</detail>
