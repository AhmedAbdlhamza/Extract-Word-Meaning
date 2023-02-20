# Extract-Word-Meaning
this code uses the BeautifulSoup library to extract the meanings and origins directly from the Merriam-Webster and Etymology Online websites.
 without the need for APIs. The list of words you want to look up should be in a file called "word_list.txt" in the same directory as the Python script, and the results will be written to a file called "word_results.txt" in the same directory.
 here's a brief explanation of the Python code:
1-First, we read in the list of words we want to look up from a file called "word_list.txt".

2-We then set up the base URLs for the Merriam-Webster and Etymology Online websites.

3-We loop over each word in the list and perform two separate HTTP GET requests to the Merriam-Webster and Etymology Online websites to extract the meaning and origin of each word.

4-For the Merriam-Webster website, we first check if the response status code is 200 (which means the request was successful). If it is, we use BeautifulSoup to extract the text of the first definition from the page. If it isn't, we set the meaning to an empty string.

5-For the Etymology Online website, we do a similar check for the response status code. If it is 200, we use BeautifulSoup to extract the text of the etymology section from the page. If it isn't, we set the origin to an empty string.

6-We then add the word, meaning, and origin to a list of results.

7-Finally, we write the results to a file called "word_results.txt".

Overall, the code uses web scraping techniques to extract information from the Merriam-Webster and Etymology Online websites, and then combines this information into a list of results that are written to a file.
