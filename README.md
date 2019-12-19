# Finding-the-standard-deviation-of-stores-sales-in-each-city.
- To write Mapper and Reducer programs that read “purchases.txt” (taken from Udacity’s Hadoop course) file from HDFS cluster and finds the standard deviation of stores’ sales in each city.<br>
- To calculate the standard deviation refer Welford’s online algorithm. You may find Python code snippet in the link. The required parts of the algorithm are as follows:<br>
𝑥𝑛= 𝑥𝑛−1+𝑥𝑛−𝑥𝑛−1𝑛 𝑀2,𝑛= 𝑀2,𝑛−1+(𝑥𝑛−𝑥𝑛−1 )(𝑥𝑛−𝑥𝑛 ) 𝜎2𝑛=𝑀2,𝑛𝑛<br>
Here, xn denotes the sample mean of the first n samples and σ2n their population variance. <br>
Once you calculate the popular variance for each city and then you can take the square root of it, which will give you the standard deviation.
