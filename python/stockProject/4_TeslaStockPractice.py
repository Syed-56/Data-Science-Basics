import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
from bs4 import XMLParsedAsHTMLWarning
import warnings

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
pio.renderers.default = "iframe"

def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021-06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()
    from IPython.display import display, HTML
    fig_html = fig.to_html()
    display(HTML(fig_html))

stock = yf.Ticker("TSLA")
tesla_data = stock.history(period="max")
tesla_data.reset_index(inplace = True)
print(tesla_data.head())

url = " https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
html_doc = requests.get(url).text

soup = BeautifulSoup(html_doc, "html.parser")

tesla_dataFrame = pd.DataFrame(columns=["Date", "Revenue"])

table = soup.find_all('tbody')[1]  # ✅ correct usage

for row in table.find_all('tr'):
    cols = row.find_all('td')
    date = cols[0].text.strip()
    revenue = cols[1].text.strip()

    tesla_dataFrame = pd.concat([
        tesla_dataFrame,
        pd.DataFrame({"Date": [date], "Revenue": [revenue]})
    ], ignore_index=True)

# Clean and filter
tesla_dataFrame["Revenue"] = tesla_dataFrame["Revenue"].str.replace(',|\\$', '', regex=True)
tesla_dataFrame.dropna(inplace=True)
tesla_dataFrame = tesla_dataFrame[tesla_dataFrame["Revenue"] != ""]

print(tesla_dataFrame.head())
