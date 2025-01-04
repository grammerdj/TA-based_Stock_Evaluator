# TA-based_Stock_Evaluator
This project was completed during June and July, 2024. This was an attempt to apply newly-learned technical analysis skills by building a swing-trading algorithm. THIS PROJECT IS NOT GUARANTEED TO GENERATE RETURNS.

V1 Results: Long-only, non-leveraged, non-derivative positions; Ran July 8th - August 2nd; 7.3% Gross Return

Description:

    The algorithm takes in a list of all of the companies in the SP500, SP600, and SP400. It also asks you for a comma-separated list of the stocks your portfolio currently holds.
    It will then obtain the price information from Yahoo Finance for all of the companies above, and it will calculate various technical indicators since 2019. Some of these include EMA, 1st and 2nd Derivatives of EMA, trends, bollinger bands, ect.
    Then, it will identify the state of these technical indicators that contributed to the highest risk/reward subset of returns of each given stock. If these pass a threshold and are currently being traced, they will be added to the final document that suggests stocks to buy. 
    The returns are calculated on a 5-day basis, using the starting price and then the highest price of the stock in a given 5-day period.

Inputs: Current Stock Holdings
Output: The SP500, SP600, and SP400 will each have an output document containing the following columns:
1. "Index" - stock index the stock belongs to
2. "Ticker" - stock ticker
3. "Price" - last price (close)
4. "Number" - number of instances that the technical pattern resulting in the distributional metrics below has been traced by the stock
5. "Mean Return" - mean return for the subset of times the technical pattern was traced.
6. "Median Return" - median return for the subset of times the technical pattern was traced.
7. "SD Return" - standard deviation of returns for the subset of times the technical pattern was traced.
8. "Percent < 1.5%" - the percentage of times the stock returned below 1.5% return for the subset of times the technical pattern was traced.
9. "Percent < 1%" - the percentage of times teh stock returned below 1% return for the subset of times the technical pattern was traced.
10. "Risk Less 0" - the percentage of times the stock returned below 0% return for the subset of times the technical pattern was traced.
11. "Mean Low" - mean low as a percentage of starting price for the subset of times the technical pattern was traced.
12. "Median Lowest Value" - median low as a percentage of starting price for the subset of times the technical pattern was traced.
13. "10th Percentile Low" - 10th percentile low as a percentage of starting price for the subset of times the technical pattern was traced.
14. "1.5 ATR as % of Price" - 1.5X the recent average trading range of the stock as a percentage of price.
15. "Correlation with Portfolio" - the correlation coefficient of the stock will all of the stocks in your portfolio
