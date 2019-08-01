# Opioid Distribution in Texas

> “In 2016, approximately 11.5 million people misused prescription pain relievers in the past year, representing 4.3 percent of the population aged 12 or older.”

-- [Key Substance Use and Mental Health Indicators in the United States](https://www.samhsa.gov/data/sites/default/files/NSDUH-FFR1-2016/NSDUH-FFR1-2016.htm#opioid3), 
Prepared for the Substance Abuse and Mental Health Services Administration (SAMHSA), (September, 2017)

The complicated story of opioid prescription and abuse in the United States continues to unfold, and [new data released by the Washington Post](https://www.washingtonpost.com/graphics/2019/investigations/dea-pain-pill-database/) on July 16, 2019 reveals the extent to which pharmaceutical companies throughout the U.S. did little to curb the crisis between 2006 and 2012. Over that time period, [76 billion oxycodone and hydrocodone pain pills](https://www.washingtonpost.com/investigations/76-billion-opioid-pills-newly-released-federal-data-unmasks-the-epidemic/2019/07/16/5f29fd62-a73e-11e9-86dd-d7f0e60391e9_story.html) were shipped and sold across the country, according to the Drug Enforcement Agency (DEA) database from which the Washington Post data was sourced. 

**Project Status**: Active

## Goals:

My goal in this project was two-fold:

First, what has the opioid crisis looked like in Texas? National attention is focused on Midwest and Appalachian states, which have felt the brunt of the crisis, but the effects of easily-accessible, addictive opioid prescription pain killers has been felt nation-wide, including here in the Lone Star State. 

Second, I wanted to answer a question I had reading about this newly-released dataset - So What? This sounds callous, but hear me out - what does the actual tracking of these opioid shipments into communities mean for those communities? Can this data be used to predict a metric that's used to measure the opioid crisis, namely the number of opioid deaths in that community? Or is this data more useful for the attention it brings to the crisis, especially in the lawsuits that have ensued which may potentially stem the overwhelming flow of prescription opiates arount the country? 

I note that this data is extremely limited. It doesn't touch the rise of synthetic opiates, including fentanyl, which are extremely dangerous and the use of which is currently on the rise. We also have no way of tracking what happens after these pills arrive at the buyer pharmacy/practitioner. Thus, we have no way of knowing how many of these pills were prescribed and used for legitimate purposes, versus those that were diverted or misused. A related issue is that we have no way of knowing how pills spread once they arrive at these buyers - for example, the Washington Post notes that there are Veterans Affairs Department distribution pharmacies that serve a regional need but which are considered retail pharmacies, and thus show an outsized impact on those communities than is likely the case. This could easily be true for pharmacies in the Texas data, where communities are over- or under-represented versus actual community use/abuse of these pills.

I humbly admit that I am no domain expert, and a public health expert with extensive experience would have had much better insights on the use and limitations of this data. But I hope to extend the conversation around this crisis and this data, and contribute useful insights which can be reproduced for other states.

## Usage Guide:

This project uses Python, via [Jupyter Notebooks](https://jupyter.org/), to explore, visualize and model data. I use a lot of Python libraries throughout these notebooks, including:

- [Pandas](https://pandas.pydata.org/pandas-docs/stable/index.html): for data manipulation
- [Numpy](https://numpy.org/): for math
- [Sci-Kit Learn](https://scikit-learn.org/stable/): for machine learning methods and data analysis
- [Yellowbrick](https://www.scikit-yb.org/en/latest/index.html): to visualize the machine learning process
- [Plotly](https://plot.ly/python/): for visualizations
- [Dash](https://dash.plot.ly/): for adding interactivity to a Plotly visualization rendered in a web browser

Please visit the above links for more details about installing and using these libraries.
 
## Data - The Washington Post DEA Pill Database:

The CSV used throughout my notebooks was compiled through work in my scratch notebooks, specifically in the [Data Exploration and Manipulation](https://github.com/lindseyberlin/Opioid-Distribution-Texas/blob/master/scratch/Scratch_Data-Exploration-and-Manipulation.ipynb) notebook. Please note, my data is not currently available on this Github due to size issues, but you can access the CSV I used throughout my main notebooks in a [Google Sheet](https://docs.google.com/spreadsheets/d/1OhdCTMMs5VkS1rR760uo6JZ0dPFejcOUPVubL1QCaZA/edit?usp=sharing).

The Washington Post data is sourced from the U.S. Justice Department Drug Enforcement Administration (DEA)’s Office of Diversion Control’s Automation of Reports and Consolidated Orders System (ARCOS). The database was downloaded from the Washington Post's [release of this data](https://www.washingtonpost.com/graphics/2019/investigations/dea-pain-pill-database/). I wrote an explanation of each column in the Washington Post dataset in a [Google Documents page](https://docs.google.com/document/d/1ArSId5WTNZzZHtLuDZetscE-hW45W-nFk-STeaXNFX8/edit#), since none was initially provided.

For my purposes, I downloaded and used only data in which the Buyer, noted by various "BUYER" columns, was located in Texas. Location data was provided in this dataset, and I utilized two location python libraries (geopy and uszipcode) to extract latitude/longitude data. You can follow my process and methodology of testing and utilizing these various location-extraction techniques in my scratch notebooks, soecifically in my [Testing Location Data Techniques](https://github.com/lindseyberlin/Opioid-Distribution-Texas/blob/master/scratch/Scratch_Testing-Location-Data-Techniques.ipynb) and [Gathering and Exporting Location Data](https://github.com/lindseyberlin/Opioid-Distribution-Texas/blob/master/scratch/Scratch_Gathering-Exporting-Location-Data.ipynb) notebooks.

> “It’s important to remember that the number of pills in each county does not necessarily mean those pills went to people who live in that county. The data only shows us what pharmacies the pills are shipped to and nothing else.”

-- [The Washington Post's Database Guide](https://www.washingtonpost.com/national/2019/07/18/how-download-use-dea-pain-pills-database/), July 18, 2019

Total pills data is compiled from the original "DOSAGE_UNIT" column, which tracks the total number of oxycodone or hydrocodone pills shipped between reporters (manufacturers/distributers) around the country and buyers (pharmacies/practitioners) here in Texas.

#### Data - Other Sources:

Total overdose death data is sourced from the Texas Deparment of State Health Services, specifically the Center for Health Statistics' [Opioid-Related Deaths in Texas Data Visualization Dashboard](http://healthdata.dshs.texas.gov/Opioids/Deaths). The dataset is tracking only deaths connected to commonly prescribed semisynthetic opiates, which excludes deaths connected to heroin, methadone, and fentanyl, among others. More specifically, the options selected when downloading the data outlined that the data concerns "all deaths (natural and injury) where opiates were involved" and the opioid category of all "commonly prescribed opioids." Also note that our total overdose death data in the below data includes a placeholder, 2.5, which represents actual numbers between 1 and 9 deaths (rates which were suppressed for privacy reasons). You can examine how I arrived at the number 2.5 by exploring my [Data Exploration and Manipulation](https://github.com/lindseyberlin/Opioid-Distribution-Texas/blob/master/scratch/Scratch_Data-Exploration-and-Manipulation.ipynb) scratch notebook.

Total population data is sourced from the [Texas State Library and Archives Commission](https://www.tsl.texas.gov/ref/abouttx/population.html), which links to the Census data to download. Note that, per year, I am using the July county population estimates - even in years where there was a census conducted. This is for consistency, because if I need to use July estimates in other years I'd prefer to use it each year, not switching to the April 2010 census count and then back to July 2011 estimates (for example).

Prescription rate data is sourced from the [CDC's U.S. Opioid Prescribing Rate Maps](https://www.cdc.gov/drugoverdose/maps/rxrate-maps.html), which tracks retail opioid prescriptions dispensed per 100 persons per year. For this database, a prescription is an initial or refill prescription dispensed at a retail pharmacy, and does not include mail order pharmacy data. Opioid prescriptions include buprenorphine, codeine, fentanyl, hydrocodone, hydromorphone, methadone, morphine, oxycodone, oxymorphone, propoxyphene, tapentadol, and tramadol. Cough and cold prescription medications containing opioids, buprenorphine products typically used to treat opioid use disorder, and methadone dispensed through methadone maintenance treatment programs are not included. My data is available as a [Google sheet](https://docs.google.com/spreadsheets/d/1fJWN3LYSLfiX_vkp4ONo0-dSyhKYmGvoYbmBOrp3PUk/edit?usp=sharing), since the CDC data was not available for a direct download.

Unemployment rate data is sourced from the [Bureau of Labor Statistics](https://data.bls.gov/lausmap/showMap.jsp). The unemployment rate is seasonally adjusted, and shows the percentage of the total labor force per county that is unemployed but seeking active employment/willing to work. My data is available in a [Google sheet](https://docs.google.com/spreadsheets/d/1BVljj8YRMTuZMQSyuwyd2LP2Y71-q-ryJSmkHgIgUbc/edit?usp=sharing), since the BLS data was not available for direct download.

## Contact:

Feel free to reach out here on [Github](https://github.com/lindseyberlin) or through [LinkedIn](https://www.linkedin.com/in/lindseyberlin/).

A presentation on this project is available on [Google Slides](https://docs.google.com/presentation/d/1xfSgZdqGphD8mhNUvy4AmoyA3JsMcHMWR6ofZgVrEi8/edit?usp=sharing).