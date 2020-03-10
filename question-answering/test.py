import question_answering

model, data = question_answering.load_data()

question_set =[('What is the URL of $MSFT?', 'http://www.microsoft.com', 'MSFT'), ('What is the Investor Relations URL of $MSFT?', 'https://www.microsoft.com/en-us/investor/', 'MSFT'), ('What is the Sector of $MSFT?', 'Technology', 'MSFT'), ('What is the Industry of $MSFT?', 'Software - Infrastructure', 'MSFT'), ('What is the Equity Style of $MSFT?', 'Large Cap/Growth', 'MSFT'), ('What is the Next Earnings Release of $MSFT?', 'Apr. 24, 2020', 'MSFT'), ('What is the Last Earnings Release of $MSFT?', 'Jan. 29, 2020', 'MSFT'), ('What is the Next Ex-Dividend Date of $MSFT?', '--', 'MSFT'), ('What is the Last Ex-Dividend Date of $MSFT?', 'Feb. 19, 2020', 'MSFT'), ('What is the Description of $MSFT?', 'Microsoft develops and licenses consumer and enterprise software. It is known for its Windows operating systems and Office productivity suite. The company is organized into three overarching segments: productivity and business processes (legacy Microsoft Office, cloud-based Office 365, Exchange, SharePoint, Skype, LinkedIn, Dynamics), intelligence cloud (infrastructure- and platform-as-a-service offerings Azure, Windows Server OS, SQL Server), and more personal computing (Windows Client, Xbox, Bing search, display advertising, and Surface laptops, tablets, and desktops). Through acquisitions, Microsoft owns Xamarin, LinkedIn, and GitHub. It reports revenue in product and service and other revenue on its income statement.', 'MSFT'), ('What is the Existing Metric Alerts of $MSFT?', 'Operator', 'MSFT'), ('What is the 1 Month Price Returns (Daily) of $MSFT?', '-2.09%', 'MSFT'), ('What is the 3 Month Price Returns (Daily) of $MSFT?', '6.36%', 'MSFT'), ('What is the 6 Month Price Returns (Daily) of $MSFT?', '19.51%', 'MSFT'), ('What is the Year to Date Price Returns (Daily) of $MSFT?', '2.73%', 'MSFT'), ('What is the 1 Year Price Returns (Daily) of $MSFT?', '44.61%', 'MSFT'), ('What is the 3 Year Price Returns (Daily) of $MSFT?', '153.2%', 'MSFT'), ('What is the 52 Week High (Daily) of $MSFT?', '190.70', 'MSFT'), ('What is the 52 Week Low (Daily) of $MSFT?', '108.80', 'MSFT'), ('What is the 52-Week High Date of $MSFT?', 'Feb. 11, 2020', 'MSFT'), ('What is the 52-Week Low Date of $MSFT?', 'Mar. 08, 2019', 'MSFT'), ('What is the Shares Outstanding of $MSFT?', '7.606B', 'MSFT'), ('What is the Dividend of $MSFT?', '0.51', 'MSFT'), ('What is the Dividend Yield (Forward) of $MSFT?', '1.26%', 'MSFT'), ('What is the Dividend Yield of $MSFT?', '1.20%', 'MSFT'), ('What is the Cash Dividend Payout Ratio of $MSFT?', '35.59%', 'MSFT'), ('What is the Payout Ratio of $MSFT?', '32.59%', 'MSFT'), ('What is the Latest Dividend Pay Date of $MSFT?', 'Mar. 12, 2020', 'MSFT'), ('What is the Last Split Factor of $MSFT?', '2.00', 'MSFT'), ('What is the Last Split Date of $MSFT?', 'Feb. 18, 2003', 'MSFT'), ('What is the Beta (5Y) of $MSFT?', '1.106', 'MSFT'), ('What is the Max Drawdown (All) of $MSFT?', '69.45%', 'MSFT'), ('What is the Daily Value at Risk (VaR) 1% (All) of $MSFT?', '5.43%', 'MSFT'), ('What is the Daily Value at Risk (VaR) 5% (All) of $MSFT?', '3.00%', 'MSFT'), ('What is the Monthly Value at Risk (VaR) 5% (All) of $MSFT?', '11.63%', 'MSFT'), ('What is the Monthly Value at Risk (VaR) 1% (All) of $MSFT?', '20.00%', 'MSFT'), ('What is the Revenue Estimates for Current Quarter of $MSFT?', '34.46B', 'MSFT'), ('What is the Revenue Estimates for Current Fiscal Year of $MSFT?', '142.48B', 'MSFT'), ('What is the EPS Estimates for Current Quarter of $MSFT?', '1.323', 'MSFT'), ('What is the EPS Estimates for Current Fiscal Year of $MSFT?', '5.686', 'MSFT'), ('What is the PE Ratio (Forward) of $MSFT?', '28.49', 'MSFT'), ('What is the PE Ratio (Forward 1y) of $MSFT?', '25.77', 'MSFT'), ('What is the PS Ratio (Forward) of $MSFT?', '8.649', 'MSFT'), ('What is the PS Ratio (Forward 1y) of $MSFT?', '7.746', 'MSFT'), ('What is the Price Target Upside (Daily) of $MSFT?', '21.86%', 'MSFT'), ('What is the Revenue (TTM) of $MSFT?', '134.25B', 'MSFT'), ('What is the Revenue (Per Share Quarterly) of $MSFT?', '4.799', 'MSFT'), ('What is the Revenue (Quarterly YoY Growth) of $MSFT?', '13.66%', 'MSFT'), ('What is the EPS Diluted (TTM) of $MSFT?', '5.74', 'MSFT'), ('What is the EPS Diluted (Quarterly YoY Growth) of $MSFT?', '39.81%', 'MSFT'), ('What is the Net Income (TTM) of $MSFT?', '44.32B', 'MSFT'), ('What is the EBITDA (TTM) of $MSFT?', '64.51B', 'MSFT'), ('What is the Total Assets (Quarterly) of $MSFT?', '282.79B', 'MSFT'), ('What is the Cash and Short Term Investments (Quarterly) of $MSFT?', '134.25B', 'MSFT'), ('What is the Book Value (Per Share) of $MSFT?', '14.47', 'MSFT'), ('What is the Tangible Book Value (Per Share) of $MSFT?', '7.980', 'MSFT'), ('What is the Total Liabilities (Quarterly) of $MSFT?', '172.68B', 'MSFT'), ('What is the Non-Current Portion of Long Term Debt (Quarterly) of $MSFT?', '63.36B', 'MSFT'), ('What is the Total Long Term Debt (Quarterly) of $MSFT?', '69.61B', 'MSFT'), ('What is the Shareholders Equity (Quarterly) of $MSFT?', '110.11B', 'MSFT'), ('What is the Cash from Financing (TTM) of $MSFT?', '-35.41B', 'MSFT'), ('What is the Cash from Investing (TTM) of $MSFT?', '-16.43B', 'MSFT'), ('What is the Cash from Operations (TTM) of $MSFT?', '54.13B', 'MSFT'), ('What is the Capital Expenditures (TTM) of $MSFT?', '13.55B', 'MSFT'), ('What is the Net Income (% of Quarterly Revenues) of $MSFT?', '31.56%', 'MSFT'), ('What is the Net Income (% of Annual Revenues) of $MSFT?', '31.18%', 'MSFT'), ('What is the Accruals (Quarterly) of $MSFT?', '969.00M', 'MSFT'), ('What is the Beneish M-Score (Annual) of $MSFT?', '-2.495', 'MSFT'), ('What is the Gross Profit Margin (Quarterly) of $MSFT?', '66.51%', 'MSFT'), ('What is the Profit Margin (Quarterly) of $MSFT?', '31.56%', 'MSFT'), ('What is the EBITDA Margin (TTM) of $MSFT?', '48.05%', 'MSFT'), ('What is the Operating Margin (TTM) of $MSFT?', '36.74%', 'MSFT'), ('What is the Asset Utilization (TTM) of $MSFT?', '0.4898', 'MSFT'), ('What is the Days Sales Outstanding (Quarterly) of $MSFT?', '52.68', 'MSFT'), ('What is the Days Inventory Outstanding (Quarterly) of $MSFT?', '16.41', 'MSFT'), ('What is the Days Payable Outstanding (Quarterly) of $MSFT?', '68.62', 'MSFT'), ('What is the Receivables Turnover (Quarterly) of $MSFT?', '1.732', 'MSFT'), ('What is the Return on Assets of $MSFT?', '16.17%', 'MSFT'), ('What is the Return on Equity of $MSFT?', '43.84%', 'MSFT'), ('What is the Return on Invested Capital of $MSFT?', '25.68%', 'MSFT'), ('What is the Market Cap of $MSFT?', '1.232T', 'MSFT'), ('What is the Enterprise Value of $MSFT?', '1.168T', 'MSFT'), ('What is the PE Ratio of $MSFT?', '28.22', 'MSFT'), ('What is the PE 10 of $MSFT?', '62.00', 'MSFT'), ('What is the PEG Ratio of $MSFT?', '0.8507', 'MSFT'), ('What is the Earnings Yield of $MSFT?', '3.54%', 'MSFT'), ('What is the PS Ratio of $MSFT?', '9.316', 'MSFT'), ('What is the Price to Book Value of $MSFT?', '11.19', 'MSFT'), ('What is the EV to Revenues of $MSFT?', '8.697', 'MSFT'), ('What is the EV to EBITDA of $MSFT?', '18.10', 'MSFT'), ('What is the EV to EBIT of $MSFT?', '22.25', 'MSFT'), ('What is the Operating PE Ratio of $MSFT?', '25.36', 'MSFT'), ('What is the Operating Earnings Yield of $MSFT?', '3.94%', 'MSFT'), ('What is the Altman Z-Score (TTM) of $MSFT?', '5.866', 'MSFT'), ('What is the Current Ratio of $MSFT?', '2.801', 'MSFT'), ('What is the Debt to Equity Ratio of $MSFT?', '0.6322', 'MSFT'), ('What is the Free Cash Flow (Quarterly) of $MSFT?', '7.135B', 'MSFT'), ('What is the KZ Index (Annual) of $MSFT?', '-17.20', 'MSFT'), ('What is the Tangible Common Equity Ratio (Quarterly) of $MSFT?', '26.02%', 'MSFT'), ('What is the Times Interest Earned (TTM) of $MSFT?', '19.95', 'MSFT'), ('What is the Total Employees (Annual) of $MSFT?', '144000', 'MSFT'), ('What is the Revenue Per Employee (Annual) of $MSFT?', '915221.8', 'MSFT'), ('What is the Net Income Per Employee (Annual) of $MSFT?', '285381.8', 'MSFT'), ('What is the CA Score (TTM) of $MSFT?', '-0.0121', 'MSFT'), ('What is the Piotroski F Score (TTM) of $MSFT?', '8.00', 'MSFT'), ('What is the Fulmer H Factor (TTM) of $MSFT?', '7.561', 'MSFT'), ("What is the Graham's Number (TTM) of $MSFT?", '43.23', 'MSFT'), ('What is the Net Current Asset Value Per Share (NCAVPS) (Quarterly) of $MSFT?', '-0.7372', 'MSFT'), ('What is the Ohlson Score (TTM) of $MSFT?', '-1.431', 'MSFT'), ('What is the Quality Ratio (TTM) of $MSFT?', '0.3317', 'MSFT'), ('What is the Springate Score (TTM) of $MSFT?', '1.799', 'MSFT'), ('What is the Sustainable Growth Rate (TTM) of $MSFT?', '29.56%', 'MSFT'), ("What is the Tobin's Q (Approximate) (Quarterly) of $MSFT?", '4.088', 'MSFT'), ('What is the Zmijewski Score (TTM) of $MSFT?', '-1.587', 'MSFT'), ('What is the Momentum Score of $MSFT?', '9.000', 'MSFT'), ('What is the Market Cap Score of $MSFT?', '1.000', 'MSFT'), ('What is the Quality Ratio Score of $MSFT?', '7.000', 'MSFT')]

correct = []
for question, answer, topic_entity in question_set:

    if question_answering.answer_question(model, data, question) == answer:

        correct.add(question)

print(question)