# Blackhole

This is my 3rd milestone project, it focused on the CRUD system. I tried to allow the user multiple ways to do each one of the CRUD elements.

With this milesone project i tried to focus more on the functionality of the website than the design, focusing on defensive programming and general functionality

---

## UX 

My audience is focused towards everyone, anyone who wants to talk share and comment on day to day things

### User Stories

* As a user i want a place to share my day with other people, and to be able to talk about it and even upload pictures

* As a user I want a place to meet new people and talk to people

* As a user I want a place to show unique and interesting things I like

* As a user I want a place I can post a picture of old items I own that i want to get rid of

---

## Features 

### Existing Features 

* The main feature in this project is the ability to post most things, you can post pictures, videos or even blocks of text

* Another feature is the ability to like and comment on other users posts, which increases the social interactions between users

* Another feature is the ability to change the theme of the website to either dark or light and have it remain the same when the user logs back in regardless of the device


### Future Features 

* One feature i wish to implenet was the ability to message other users privately

* A second feature would be to give the user notifications of messages, post they made that have been liked/commented on and by who

---

## Technologies Used

* Jquery
    * This was used to simplify javascript, although in some areas i choose to not use it
    * https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwi2x93P9tDsAhVrThUIHWDICzIQFjAAegQIBBAC&url=https%3A%2F%2Fjquery.com%2F&usg=AOvVaw1yb1TgbSxtZNKnsTynd_HN

* Flask
    * This was used to simplify python and html 'talking'
    * https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiDvPrc9tDsAhVRt3EKHRTyDTIQFjAAegQIARAC&url=https%3A%2F%2Fflask.palletsprojects.com%2F&usg=AOvVaw10INQEbdYkEQIifZAl5hxD

* Flask-Pymongo
    * This was used to simplify the use of mongodb with python
    * https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwju6Yzo9tDsAhVXRxUIHejfAGEQFjACegQIBRAC&url=https%3A%2F%2Fpypi.org%2Fproject%2Fpymongo%2F&usg=AOvVaw1apMq1nRDAg9X4ld6H6MPI

* MongoDB
    * This was used to store data uploaded from the user
    * https://www.google.com/aclk?sa=l&ai=DChcSEwiw_63w9tDsAhXFse0KHSsoChoYABAAGgJkZw&ae=2&sig=AOD64_2Yj7WsXrvUN21Xym3Yhx3jGclDzw&q&adurl&ved=2ahUKEwjBu6bw9tDsAhV0t3EKHXCcBhQQ0Qx6BAhAEAE

* Cloudinary
    * This was used to store and retrieve images/videos uploaded by the user
    * https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwj4zpv79tDsAhX4VBUIHc35CvUQFjAAegQICRAD&url=https%3A%2F%2Fcloudinary.com%2F&usg=AOvVaw21MpFQypQosqq7PGr-xbWs

* Heroku 
    * This was used to run my app on a live server 
    * https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwj3q7uD99DsAhVeQhUIHSN8BGcQFjAAegQIDxAD&url=https%3A%2F%2Fwww.heroku.com%2F&usg=AOvVaw1V4lhSv6mb_lZj6UUCUXpS

---

## Testing

For the testing i used multiple friends and purposefully trying to break it, in multiple sections i tried to enter empty forms,
and incorrect information to ensure i got the intended error message.

Along with my mentor going onto the site in our sessions and commenting on any issues he had seen.

---

## Deployment

This was deployed via Heroku by connecting my heroku account with my github account, so whenever i push from gitpod to github it will automatically update the live server

To run this locally you will need to install a few extra libaries

`pip3 install flask` 
`pip3 install cloudinary`
`pip3 install pymongo`

this will enable you to run this app locally, but you will need an internet connection to get the full use out of the app

---

## Credits 

### Content 

* callout.jpg
 * from 
 * https://staticshare.america.gov/uploads/2014/10/facebookmap_fromMark.jpg

## Acknowledgements 

I recieved inspiration for this site from pages such as Facebook and Twitter, with a lot of help from the tutors and mentors at code institute


