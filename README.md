# sentimet-analysis
## Read the README.pdf file for a more clear guideline with related screenshots

### Project Guideline
1. Clone/ download the repository from the following link:
    
   https://github.com/Mehedi-909/sentiment-analysis-hugging-face

2. Open the project folder “sentiment_analysis” with a suitable IDE such as PyCharm/ VS Code
   
3. Open a new terminal window

4. Create a virtual environment with the following command:
   
#### Windows OS
> py -m venv venv

#### Unix/ Mac OS
> python -m venv venv 

5. Activate the virtual environment using the following command for Windows OS: 

#### Windows OS
> venv/Scripts/activate   

#### Unix/ Mac OS
> source venv/bin/activate

6. Then install the necessary dependencies using the command:

> pip install -r requirements.txt 

7. After the successful installation, run the following command to run the server:

> python manage.py runserver


Now the project is running on the localhost server. 

You can now hit the url: http://localhost:8000/analyze in a browser to access the browsable API or test it through Postman in the following way:

Send a POST request with request body in JSON format s follows:

{
    "text": "Your text to be analyzed"
}

Then wait for a while to get the response. The response will appear in the following format: 

{
    "sentiment": "Positive / Negative / Neutral"
}

