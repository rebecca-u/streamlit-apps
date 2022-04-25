#import libraries
import pandas as pd
import streamlit as st
import plotly.express as px

#fetch Airbnb NYC listings data from Inside Airbnb using a function
@st.cache()
def get_data():
    url = "http://data.insideairbnb.com/united-states/ny/new-york-city/2021-11-02/visualisations/listings.csv"
    return pd.read_csv(url)

df = get_data()


#Data caching
## start with a heading and a quote
st.title("Airbnb Streamlit app") #st.title for main title
st.markdown("Welcome to the Airbnb streamlit app using a dataset containing NYC listings.")
#st.markdown used for any string written using GitHub Flavored Markdown, often shortened as GFM, is the dialect of Markdown that is currently supported for user content on GitHub.com and GitHub Enterprise.
#This formal specification, based on the CommonMark Spec, defines the syntax and semantics of this dialect.

st.header("Customary quote")#st.header and st.subheader used for section titles 
st.markdown("> I just love to go home, no matter where I am, the most luxorious hotel suite in the world, there is no place like home!!\n\n—Tony Mills.")

#data at a glance 
st.dataframe(df.head())

#code blocks
st.code("""
        @st.cache
        def get_data():
            url = "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-09-12/visualisations/listings.csv"
            return pd.read_csv(url)
        """, language = "python")
        #alternatively st.echo can be used for code blocks
             
#Most expensive Airbnb listings in NYC
##On a map
###st.map displays locations on a map without writing lots of code. Only requirement is that df must contain columns named lat/latitude or lon/longitude.
st.header("Where are the most expensive properties located?")
st.subheader("On a map")
st.markdown("The following map shows the top 1% most expensive Airbnbs priced at $800 and above.")
st.map(df.query("price>=800")[["latitude", "longitude"]].dropna(how="any"))

st.subheader("In a table")
st.markdown("Following are the top five most expensive properties.")
st.write(df.query("price>=800").sort_values("price", ascending=False).head())

#selecting a subset of columns using multiselect widget
st.subheader("Selecting a subset of columns")
st.write(f"Out of the {df.shape[1]} columns, you might want to view only a subset. Streamlit has a [multiselect](https://streamlit.io/docs/api.html#streamlit.multiselect) widget for this.")
defaultcols = ["name", "host_name", "neighbourhood", "room_type", "price"]
cols = st.multiselect("Columns", df.columns.tolist(), default=defaultcols)
st.dataframe(df[cols].head(10))

#Average price by room type in a static table using st.table. Cannot sort it by clicking a column header.
st.header("Average price by room type")
st.write("You can also display static tables. As opposed to a data frame, with a static table you cannot sorting by clicking a column header.")
st.table(df.groupby("room_type").price.mean().reset_index()\
    .round(2).sort_values("price", ascending=False)\
    .assign(avg_price=lambda x: x.pop("price").apply(lambda y: "%.2f" % y)))

#Which hosts have the most properties listed?
st.header("Which host has the most properties listed?")
listingcounts = df.host_id.value_counts()
top_host_1 = df.query('host_id==@listingcounts.index[0]')
top_host_2 = df.query('host_id==@listingcounts.index[1]')
st.write(f"""**{top_host_1.iloc[0].host_name}** is at the top with {listingcounts.iloc[0]} property listings.
**{top_host_2.iloc[1].host_name}** is second with {listingcounts.iloc[1]} listings. Following are randomly chosen
listings from the two displayed as JSON using [`st.json`](https://streamlit.io/docs/api.html#streamlit.json).""")

st.json({top_host_1.iloc[0].host_name: top_host_1\
    [["name", "neighbourhood", "room_type", "minimum_nights", "price"]]\
        .sample(2, random_state=4).to_dict(orient="records"),
        top_host_2.iloc[0].host_name: top_host_2\
    [["name", "neighbourhood", "room_type", "minimum_nights", "price"]]\
        .sample(2, random_state=4).to_dict(orient="records")})

    #finding the distribution of the property price using st.plotly_chart
st.header("What is the distribution of property price?")
st.write("""Select a custom price range from the side bar to update the histogram below displayed as a Plotly chart using
[`st.plotly_chart`](https://streamlit.io/docs/api.html#streamlit.plotly_chart).""")
#add a sidebar and price range slider
##use st.slider to provide a slider that allows selecting a custom range for the histogram and tuck it away into a sidebar.
values = st.sidebar.slider("Price range", float(df.price.min()), float(df.price.clip(upper=1000.).max()), (50., 300.))
f = px.histogram(df.query(f"price.between{values}"), x="price", nbins=15, title="Price distribution")
f.update_xaxes(title="Price")
f.update_yaxes(title="No. of listings")
st.plotly_chart(f)

