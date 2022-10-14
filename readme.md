# ReadMe

The Repository holds the slides and code for my Azure Functions demonstration during the JADS Data Experience Day 2022.

## Contents

Aside from the standard files this repo contains 3 folder of Function code ready to be deployed to an Azure Function App.

The end product is a simple application which:
<ol>
    <li> Triggers at midnight and pulls in hourly precipitation data from the KNMI web API from the last day</li>
    <li> Cleans the pulled in data by removing leading/trailing spaces and comment lines</li>
    <li> Stores the cleaned data as a csv file in the linked storage account</li>
    <li> Passes the data to a second worker which can apply extra cleaning steps. This exmaple removes full nan rows 
         to save in storage space.</li>
    <li> Stores the further cleaned data as a csv file in a separate container in the linked storage account</li>

</ol>

### MidnightDataPull
A time triggered function to execute steps 1-3 of the above workflow. Triggers at midnight every day. 
Outputs a blob to the datasets container.

### CleanAndStore
A Blob triggered function which executes steps 4-5 of the above workflow. Triggers upon a blob being inserted to the 
datasets container. Outputs a blob to the cleaned_datasets container.

### HttpDataPull
A Http triggered function which can manually trigger the MidnightDataPull. Not part of the final workflow, but needed 
for live dmeo purposes

## Setup
In order to easily deploy this app with VSCode you must download the Azure Account, Azure Functions and Azure Resources 
Extensions. 

I suggest using VSCode version 1.6.3 as 1.7.2 has an issue with said extensions 
(.isLinux is not recognised as a command).

All other explanation can be found in the docs 
(<a>https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-vs-code?tabs=csharp</a>)

## Improvements
To further improve this example feel free to fork or submit a PR here. Some potential expansions are:
<ul>
<li>A script that cleans up old data files from the storage</li>
<li>Connect up a database instead of the final blob storage</li>
</ul>

## Contact
Feel free to connect with me on LinkedIn <a>https://www.linkedin.com/in/benedmondson/</a> to discuss or if I can help you in any way.