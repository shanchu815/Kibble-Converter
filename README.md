# Kibble Converter
Kibble Converter is a resource site that lets pet owners find out what’s in their pet food. This site includes two different converters - one for for foods made in the US (under FDA standards) and foods made in the EU (under FEDIAF standards). It also includes a comparison calculator to let users find the true protein contents of their products, making the process far less tedious. Currently, this only applies to foods made for cats and dogs.

Kibble Converter is a web app created by Shannon Chu. Shannon is passionate about pets, but currently has never owned one. As there was a lack of APIs and reputable sites regarding pet nutrition, she undertook quite the challenge of manually collecting and comparing data in order to create a database for Kibble Converter. Kibble Converter is currently locally deployed at http://3.91.73.97/ but lacks a domain name.

Each page features a randomly generated cat or dog photo captioned with a random cat or dog fact. These facts and images are obtained from various pet APIs.

## Table of Contents
* [Technologies Used](#technologiesused)
* [How to use Kibble Converter](#use)
* [How to use Kibble Converter's Calculator](#calculate)
* [Future plans for Kibble Converter](#futureplans)
* [About the author](#author)

## <a name="technologiesused"></a>Technologies Used

* Python
* Flask
* PostgresSQL
* SQLAlchemy
* Javascript
* AJAX/JSON
* Jinja2
* CSS
* HTML
* Bootstrap
* Dog Facts API
* The Cat API
* Cat Fact @ ninja API
* Dog.CEO API

(dependencies are listed in requirements.txt)

## <a name="use"></a>How to use Kibble Converter

###Enter the homepage and read `What's in my pet's food?` and the instructions in `How do I use this site?`

###Select either of the two `Convert` buttons.
The user should pick the correct button depending on their location or where their pet food was made.

![Kibble Converter Homepage](/static/readme-images/homepage.gif)

The user will be taken to a disclaimer that includes the corresponding link in regards to pet food labelling standards. A link to FDA's page will be shown if the user chose `Convert US`. If the user chose `Convert EU`, the disclaimer will contain a link to the FEDIAF's page.

![US Disclaimer](/static/readme-images/disclaimerUS.gif)

![EU Disclaimer](/static/readme-images/disclaimerEU.png)

###Press the `Continue` button after reading the disclaimer 
This will take the user to the form page. Please fill out the form according to the instructions given for each option. There is a `Reset` button in case the user has chosen incorrectly and wishes to clear the form.

![Form Page](/static/readme-images/form.gif)

![Form Page 2](/static/readme-images/form2.png)

###Press the `Submit` button when the user is finished
This button will store the inputs into the database and query back a result, taking the user to a result page where the contents of their pet food will be shown in layman's terms. The user can then choose to share the link to social media by pressing the Facebook or Twitter button OR they can choose to copy the URL to their clipboard with the `🔗` button.

![Result Page](/static/readme-images/result.gif)

## <a name="calculate"></a>How to use Kibble Converter's Calculator
###Press the `Calculate` button on the bottom of any page or select `Calculator` from the navigation bar
This will take the user to the calculator. The user should read the following instructions in order to understand how to read their pet food ingredient label.

There are two calculators in order to allow the user to compare two different products simultaneously.
They can be used via entering the required inputs and pressing the corresponding `Submit` button. They can also be cleared by pressing the corresponding `Reset` button.

![Calculator Page](/static/readme-images/calculator.gif)

![Calculator Page 2](/static/readme-images/calculator2.gif)

## <a name="futureplans"></a>Future plans for Kibble Converter
Future plans for this site include getting a domain name, getting an SSL certificate in order for page links to be automatically copied to the user's clipboard and expanding the list of available selections for the user and allowing for more specific multiple selections.

## <a name="author"></a>Author
Shannon Chu is a software engineer in Great Neck, NY. (https://www.linkedin.com/in/shanchu-cs/)