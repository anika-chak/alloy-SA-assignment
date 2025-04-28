# Alloy Take Home Assignment

To run this project:

```streamlit run main.py```

## Approach
1. Read through the documentation to understand how to authenticate using the given token and secret and produce a successful API call.
2. Use the GET sandbox endpoint to get the required input fields and their specific formatting.
3. Using the correct formatting from the GET request, submit data to the POST sandbox endpoint to produce each type of output (Approved, Manual Review, Denied).
4. Create a simple UI using Streamlit to take in custom inputs and display the API response.

## Observations
The sandbox POST endpoint only requires the name_first input, whereas the full list of inputs obtained from the GET request has additional required fields. I observed this by submitting a POST request with no data and saw that the required fields differ.

It's possible to get a partial result (status code 206) by entering state and country as "New York" and "US", for example. The outcome of this request was "Manual Review", so I added a condition for printing this result in addition to successful API calls where status code = 201.

If I had more time, I would test more thoroughly to ensure that I'm not missing any edge cases in my error handling. I would also improve the output for outcomes other than "Approved" to give more information on why the application couldn't be approved. This can be done by using the error message details already provided by the API, as well as adding more specific messaging for outcomes that are "Manual Review" or "Deny." 
