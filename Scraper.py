class Scraper:
    
    """ Class documentation:
    
            This class is meant to be called as a part of my TA analysis algorithm in order to scrape stock ticker symbols and their 
            historical prices. An instance of this class will have a couple attributes to it, including exchange list, save type, return_df, start date,
            and end date.
    
    """

    # This initializes all of the options for the scraper

    def __init__(self, exchange_list=["NYSE"], save_type="CSV", return_df=False, start_date=None, end_date=None):

        import datetime as dt
        
        assert (type(exchange_list) == list) & (len(exchange_list) > 0), "Please enter the exchanges you would like retrieved in a list format with " +\
        "at least one exchange."
        assert (save_type == "CSV") | (save_type == "JSON"), "Please enter your save type as either 'CSV' or 'JSON'."
        
        if start_date != None:
        
            assert bool(dt.datetime.strptime(start_date, '%Y-%m-%d')), "Make sure you enter your start date in the format YYYY-MM-DD."
        
        if end_date != None:
        
            assert bool(dt.datetime.strptime(end_date, '%Y-%m-%d')), "Make sure you enter your end date in the format YYYY-MM-DD."
            
        assert type(return_df) == bool, "Please enter your selection for whether or not you want your scrapes directly returned as a boolean."
        self.exchange_list = exchange_list
        self.save_type = save_type
        self.return_df = return_df
        self.start_date = start_date
        self.end_date = end_date

    
    # This function uses the pandas datareader and yfinance library to actually 
    # actually scrape the historical data, and then reformats the date to remove the time component. Currently, this is only capable of scraping 
    # daily data.

    def _scrape_stock_information(stock_symbol, start_date= None, end_date=None):

        import pandas_datareader.data as web
        import pandas as pd
        import datetime as dt
        import yfinance as yf
        yf.pdr_override()
        
        failed_scrapes = []
        if (start_date != None) & (end_date != None):
            website_df = web.get_data_yahoo(stock_symbol, start = start_date, end = end_date)
        elif start_date != None:
            website_df = web.get_data_yahoo(stock_symbol, start = start_date)
        elif end_date != None:
            website_df = web.get_data_yahoo(stock_symbol, end = end_date)
        else:
            website_df = web.get_data_yahoo(stock_symbol)
        if website_df.shape[0] == 0:
            print("This stock failed to scrape. Apologies")
            failed_scrapes.append(stock_symbol)
            return "Nope"
        else:
            date_list = []
            for index in website_df.index:
                string_index = str(index)[0:10]
                date_list.append(dt.datetime.strptime(string_index, '%Y-%m-%d').date())
            website_df['Date'] = date_list
            website_df = website_df.set_index('Date')
            return website_df

    
    # This function will compile a list of every publicly traded stock on the market as a dataframe with the columns [Symbol, Name]. 
    # If you have the function scrape multiple exchanges, it will create a file for each exchange.
    # If you have return_df = True, it will return a dictionary of your stock symbol dataframes with the format {Exchange: Dataframe}
    # This function uses the website EODDATA as a source.

    def scrape_tickers(self): 

        import requests
        from bs4 import BeautifulSoup
        import pandas as pd
        import os
        
        if self.return_df:
            output = {}
        else:
            print("You have specified that the stock symbol dataframes that you scrape not be returned from this function. If you would like " + \
                  "to return the dataframes that you scrape, please create a scraper with the return_df parameter True")
            
        #This will loop through all the exchanges in the exchange list provided.
        for i in range(0, len(self.exchange_list)):
    
            symbols = []
            names = []
            
            print(f"Now scraping stock symbols and names for {self.exchange_list[i]}")
            url = 'https://eoddata.com/stocklist/' + self.exchange_list[i] + '/{}.html'
            
            #This loop will loop through the pages of EOD Data to get all of a specific exchange's stock symbols
            for letter in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', \
                           'U', 'V', 'W', 'X', 'Y', 'Z']:
                print("Now scraping stock tickers starting with " + letter)
                page_url = url.format(letter)
                page = requests.get(page_url)
                assert page.status_code == 200, "The EOD Website failed to load (Status != 200)"
    
                #This portion of the code isolates the stock symbols from the table on the website.
                data = BeautifulSoup(page.text, 'html.parser')
                tbl = data.find('table', {'class': 'quotes'})
                assert len(tbl) > 0
                hdr = tbl.find_all('th')
                hdrs = []
                for th in hdr:
                    text = th.text
                    hdrs.append(text)
                assert len(hdrs) == 8, "The table you are trying to scrape does not exist on this page"
                hdrs.pop(-1)
                tbl_data = tbl.find_all('tr')
                tbl_data.pop(0)
                for row in tbl_data:
                    stock_symbol = row.find_all('td')
                    for td in stock_symbol:
                        if stock_symbol.index(td)==hdrs.index('Code'):
                            symbol = td.text
                        if stock_symbol.index(td)==hdrs.index('Name'):
                            name = td.text
                            
                    symbols.append(symbol)
                    names.append(name)

            #This code will create the dataframe
            stock_symbol_df = pd.DataFrame({"Ticker": symbols, "Company": names})
            print(f"There are {len(stock_symbol_df)} stocks being traded on {self.exchange_list[i]}.")
    
            #This code will save the df as either a JSON or CSV in a directory called "Stock_Symbol_Lists"
            assert (self.save_type == "CSV") | (self.save_type == "JSON"), "Please enter either 'CSV' or 'JSON'"
            
            if os.path.exists("Stock_Symbol_Lists") == False:
                os.mkdir("Stock_Symbol_Lists")
                print("A Stock_Symbol_Lists directory has been created for you in the location where you saved this scraper")
            
            if self.save_type == "CSV":
                filename = f"{self.exchange_list[i]}_stock_list.csv"
                stock_symbol_df.to_csv(os.path.join('Stock_Symbol_Lists', filename))
                print(f"{filename} successfully saved.")
            else:
                filename = f"{self.exchange_list[i]}_stock_list.json"
                stock_symbol_df.to_json(os.path.join('Stock_Symbol_Lists', filename))
                print(f"{filename} successfully saved.")
    
            if self.return_df:
                output[self.exchange_list[i]] = stock_symbol_df
            
        if self.return_df:
            return output



    # This function retrieves a dictionary of all of the stock symbol lists that you specify with the format {Exchange: Dataframe}
    # Please specify the type of file that you initially saved the dataframes in.

    def retrieve_tickers(self, exchange=None):

        import pandas as pd
        import os
        
        assert os.path.exists("Stock_Symbol_Lists"), "Hmm, it seems as though you have not scraped any stock symbol lists yet. " + \
            "Please run the [Scaper_Instance].scrape_tickers() function to scrape a list for an exchange."

        if exchange != None:
            
            if self.save_type == "CSV":
                
                filename = os.path.join("Stock_Symbol_Lists", f"{exchange}_stock_list.csv")
                assert os.path.exists(filename), "Hmm, you do not seem to have a file for this exchange"
                df = pd.read_csv(filename, index_col = 0)
                return df

            else:
                
                filename = os.path.join("Stock_Symbol_Lists", f"{exchange}_stock_list.json")
                assert os.path.exists(filename), "Hmm, you do not seem to have a file for this exchange"
                df = pd.read_json(filename, index_col = 0)
                return df
                
        else:
            exchanges = {}
            
            if self.save_type == "CSV":
                
                for exchange in self.exchange_list:
                    
                    filename = os.path.join("Stock_Symbol_Lists", f"{exchange}_stock_list.csv")
                    assert os.path.exists(filename), "Hmm, you do not seem to have a file for this exchange"
                    df = pd.read_csv(filename, index_col = 0)
                    exchanges[exchange] = df
                return exchanges
                
            else:
                
                for exchange in exchange_list:
                    
                    filename = os.path.join("Stock_Symbol_Lists", f"{exchange}_stock_list.json")
                    assert os.path.exists(filename), "Hmm, you do not seem to have a file for this exchange"
                    df = pd.read_json(filename, index_col = 0)
                    exchanges[exchange] = df
                return exchanges






    # This function gets a stock's historical pricing for each day since the stock has been traded, or a specified start date. 
    # This function saves the stock's history as a df with the following columns: [Date, Open, High, Low, Close, Adj Close, Volume]
    # If you choose the return_df option, the function will also return the stock df.

    def scrape_stock(stock_symbol, return_df = False, save = True, save_type="CSV", start_date= None, end_date = None):

        import pandas as pd
        import yfinance as yf
        import datetime as dt
        import os
        
        yf.pdr_override()
        # A couple of assert statements to make sure that the parameters are entered correctly
        assert type(stock_symbol) == str, "Please enter the stock symbol to be scraped"+\
            " as a string."
            
        assert (save_type == "CSV") | (save_type == "JSON"), "Please enter your save type as either 'CSV' or 'JSON'."
        
        if start_date != None:

            sd = True
            assert bool(dt.datetime.strptime(start_date, '%Y-%m-%d')), "Make sure you enter your dates" +\
            " in the format YYYY-MM-DD."
        else:
            sd=False
        

        if end_date != None:
            
            assert bool(dt.datetime.strptime(end_date, '%Y-%m-%d')), "Make sure you enter your dates" +\
            " in the format YYYY-MM-DD."

            
            # Informing people that their dates are wrong.
        
            if dt.datetime.now().date() < dt.datetime.strptime(end_date, '%Y-%m-%d').date():
                
                print("I cannot scrape a stock's price in the future. If I could, I would be rich, not writing this code for you. The scraper will return" +\
                          " dates up until the last closed trading day.")

        
        #References internal function
        history_df = Scraper._scrape_stock_information(stock_symbol, start_date, end_date)
        if type(history_df) is str:
            return "Sorry!"

        if sd:
            if history_df.index[0] > dt.datetime.strptime(start_date, '%Y-%m-%d').date():
            
                print(f"This stock did not trade on {start_date}." +\
                      f" {dt.datetime.strftime(history_df.index[0], '%Y-%m-%d')} is when the historical data will start.")

        if save == True:
            if os.path.exists("Historical_Stock_Data") == False:
                
                    os.mkdir("Historical_Stock_Data")
                    print("A 'Historical_Stock_Data' directory has been created for you in the location where you saved this scraper.")
            
        
            if save_type == "CSV":
                
                filename = f"{stock_symbol}.csv"
                history_df.to_csv(os.path.join('Historical_Stock_Data', filename))
                print(f"{filename} successfully saved.")
                
            else:
                
                filename = f"{stock_symbol}.json"
                history_df.to_json(os.path.join('Historical_Stock_Data', filename))
                print(f"{filename} successfully saved.")
        
        
        if return_df:
            return history_df


    #This function scrapes a stock list, and if return_df is set to True, it returns a {Ticker; Dataframe} dictionary

    def scrape_stock_list(stock_symbol_list, return_df = True, save_type="CSV", start_date= None, end_date = None):

        import os
        
        assert type(stock_symbol_list) == list, "Please enter the stock symbol list as a list of stock ticker strings."

        if return_df:

            stock_dict = {}

            for stock_symbol in stock_symbol_list:
    
                    df = scrape_stock(stock_symbol, return_df, save_type, start_date, end_date)
                    stock_dict[stock_symbol] = df
            return stock_dict

        else:

            for stock_symbol in stock_symbol_list:
                
                scrape_stock(stock_symbol, return_df, save_type, start_date, end_date)



    #This function scrapes a whole exchange, and does not allow you to return that data

    def scrape_exchange(self, exchange=None):

        assert (type(exchange) == str) or (exchange==None), "Please enter a valid exchange as a string"

        if exchange == None:
            exchange = self.exchange
            
        if self.save_type == "CSV":

            filename = f"{exchange}_stock_list.csv"
            
            if os.path.exists("Stock_Symbol_Lists", filename):

                tickers = retrieve_tickers(self, exchange)

            else:

                print(f"It seems that you have not scraped {exchange} for tickers yet. I will do this now, it should only take a minute or two.")
                scraper = Scraper([exchange], save_type = "CSV", return_df = True, start_date = self.start_date, end_date = self.end_date)
                tickers = scrape_tickers(scraper)
                
        else: 

            filename = f"{exchange}_stock_list.json"
            
            if os.path.exists("Stock_Symbol_Lists", filename):

                tickers = retrieve_tickers(self, exchange)

            else:

                print(f"It seems that you have not scraped {exchange} for tickers yet. I will do this now, it should only take a minute or two.")
                scraper = Scraper([exchange], save_type = "JSON", return_df = True, start_date = self.start_date, end_date = self.end_date)
                tickers = scrape_tickers(scraper)

        for stock_symbol in tickers["Ticker"]:

            scrape_stock(stock_symbol, return_df = False, save_type = self.save_type, start_date = self.start_date, end_date = self.end_date)


    # This function updates a single stock

    def update_stock(ticker, save_type = "CSV"):

        import numpy as np
        import pandas as pd
        from datetime import datetime as dt
        import os
        
        assert type(ticker) == str, "Please enter a ticker that makes sense"

        if save_type == "CSV":
            
            path = os.path.join('Historical_Stock_Data', f"{ticker}.csv")
            
            if os.path.exists(path):
                
                old_df = pd.read_csv(path, index_col = 0)
                stock_df = Scraper._scrape_stock_information(ticker, start_date=old_df.index[-1], end_date=dt.strftime(dt.now(), "%Y-%m-%d"))
                updated_df = old_df._append(stock_df)
                updated_df.to_csv(path)
                return None
            
            else:
                
                stock_df = Scraper._scrape_stock_information(ticker)
                stock_df.to_csv(path)
                return None

        else:

            path = os.path.join('Historical_Stock_Data', f"{ticker}.json")
            
            if os.path.exists(path):
                
                old_df = pd.read_json(path, index_col = 0)
                stock_df = Scraper._scrape_stock_information(ticker, start_date=old_df.index[-1], end_date=dt.strftime(dt.now(), "%Y-%m-%d"))
                updated_df = old_df._append(stock_df)
                updated_df.to_json(path)
                return None
                
            else:
                
                stock_df = Scraper._scrape_stock_information(ticker)
                stock_df.to_json(path)
                return None
             

        
    # This function updates a list of stocks

    def update_watchlist(watchlist, save_type = "CSV"):

        for stock in watchlist:

            update_stock(stock, save_type = save_type)
            
        return None

    
    # This function updates a whole exchange
    
    def update_exchange(self, exchange):

        import os

        assert type(exchange) == str, "Please enter a valid exchange as a string"

        if self.save_type == "CSV":

            filename = f"{exchange}_stock_list.csv"
            
            if os.path.exists("Stock_Symbol_Lists", filename):

                tickers = retrieve_tickers(self, exchange)

            else:

                print(f"It seems that you have never scraped the {exchange}. Therefore, there is no need to update your securities' historical data, \
                        as there is none. Please double check your Scraper object's save_type, or run 'scrape_tickers' or 'scrape exchange' instead.")
                
                return None
        else:

            filename = f"{exchange}_stock_list.json"
            
            if os.path.exists("Stock_Symbol_Lists", filename):

                tickers = retrieve_tickers(self, exchange)

            else:

                print(f"It seems that you have never scraped the {exchange}. Therefore, there is no need to update your securities' historical data, \
                        as there is none. Please double check your Scraper object's save_type, of run 'scrape_tickers' or 'scrape exchange' instead.")

                return None

        for stock in tickers:

            update_stock(stock, save_type = self.save_type)
            
        return None
    
    
                
            
## WAS WORKING ON UPDATE FUNCTION. IN THE MIDDLE OF SCRAPING ONLY UPDATE DATA FOR A STOCK!!!
        


    
