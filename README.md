# Kibble Converter
Kibble Converter is a resource site that lets pet owners find out what’s in their pet food. This site includes two different converters - one for for foods made in the US (under FDA standards) and foods made in the EU (under FEDIAF standards). It also includes a comparison calculator to let users find the true protein contents of their products, making the process far less tedious. Currently, this only applies to foods made for cats and dogs.

Kibble Converter is a web app created by Shannon Chu. Shannon is passionate about pets, but currently has never owned one. As there was a lack of APIs and reputable sites regarding pet nutrition, she undertook quite the challenge of manually collecting and comparing data in order to create a database for Kibble Converter. As of 2023, Kibble Converter is currently no longer deployed but a demo of its functions can be found here: https://www.youtube.com/watch?v=xbufeOuMMs4

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

https://user-images.githubusercontent.com/87048917/149681031-d21f40e5-8474-4836-8d01-c25a0a178fec.mov

The user will be taken to a disclaimer that includes the corresponding link in regards to pet food labelling standards. A link to FDA's page will be shown if the user chose `Convert US`. If the user chose `Convert EU`, the disclaimer will contain a link to the FEDIAF's page.

![US Disclaimer](https://i.imgur.com/S0pseKn.gif)

![EU Disclaimer](https://imgur.com/6n5pAPv.png)

###Press the `Continue` button after reading the disclaimer 
This will take the user to the form page. Please fill out the form according to the instructions given for each option. There is a `Reset` button in case the user has chosen incorrectly and wishes to clear the form.

![Form Page](https://imgur.com/XCckAGg.gif)

![Form Page 2](https://imgur.com/no6oW1n.png)

###Press the `Submit` button when the user is finished
This button will store the inputs into the database and query back a result, taking the user to a result page where the contents of their pet food will be shown in layman's terms. The user can then choose to share the link to social media by pressing the Facebook or Twitter button OR they can choose to copy the URL to their clipboard with the `🔗` button.

![Result Page](https://i.imgur.com/Qqgc09f.gif)

## <a name="calculate"></a>How to use Kibble Converter's Calculator
###Press the `Calculate` button on the bottom of any page or select `Calculator` from the navigation bar
This will take the user to the calculator. The user should read the following instructions in order to understand how to read their pet food ingredient label.

There are two calculators in order to allow the user to compare two different products simultaneously.
They can be used via entering the required inputs and pressing the corresponding `Submit` button. They can also be cleared by pressing the corresponding `Reset` button.

![Calculator Page](https://i.imgur.com/YGxX8YC.gif)

![Calculator Page 2](https://imgur.com/LoRCwOO.gif)

## <a name="futureplans"></a>Future plans for Kibble Converter
Future plans for this site include getting a domain name, getting an SSL certificate in order for page links to be automatically copied to the user's clipboard and expanding the list of available selections for the user and allowing for more specific multiple selections.

## <a name="author"></a>Author
Shannon Chu is a software engineer in Great Neck, NY. (https://www.linkedin.com/in/shanchu-cs/)
