# Palette:imageSearch

## Summary

ImageSearch uses the Custom Search interface of Google to find images which match the given search term. 

## Google API

The custom parameters of this component require a Google API Key and a Custom Search Engine ID which can be generated on [Googles API Manager](<https://console.developers.google.com/apis/>). 

After logging into the Google API Manager, create a new Project. After the creation process has concluded, you will end up in the Google API Library. Here choose the Custom Search API and enable it. You will be prompted with a warning which suggests to create credentials for your API. Click the "Go to Credentials" Button and choose "Web Browser" in the second drop down list. Next click on the "What Credentials do I need" button, give the API key a name and click "Create API Key". The generated key will be your _Google API Key_. 

Next add a Custom Search Engine by going [here](<https://cse.google.com/cse>). You will find the Search Engine ID under the Basics section of the Setup page. 

Please be advised that by default you have 100 requests per day. To increase this maximum you will have to set up a billing account.
