# FlaskDirectUploader


## Licensing

The files in this repository are, unless stated otherwise, released under the Apache License. You are free to redistribute this code with or without modification. The full license text is available [here](http://www.apache.org/licenses/LICENSE-2.0).


## Direct-to-S3 uploads in a Python application running on Heroku

Simple example demonstrating how to accomplish a direct upload to Amazon S3 in a Python web application.

The example focuses on Flask as the web framework and is targeted for use on the Heroku platform. However, nearly all of the code could be used as-is in other Python frameworks (such as Bottle and Django). An example using Python 3 and Django is available [here](https://gist.github.com/RyanBalfanz/f07d827a4818fda0db81).

This is the companion repository to the Heroku article, [Direct to S3 File Uploads in Python](https://devcenter.heroku.com/articles/s3-upload-python).

This code is mostly ready to be run as cloned, but a function `update_account()` will need to be defined to handle the storing of the POSTed information.


## Running the application
* Set environment variables for your AWS access key, secret, and bucket name (see [companion article](https://devcenter.heroku.com/articles/s3-upload-python))
* Run `python application.py`
* Visit [localhost:5000/account](http://localhost:5000/account) to try it out


## Deploying the application

See the article [Deploying with Git](https://devcenter.heroku.com/articles/git) for more detailed information on deploying to Heroku.

* Download and install the [Heroku toolbelt](https://toolbelt.heroku.com/)
* Commit your application to a local Git repository (e.g. `git init`, `git add .`, `git commit -m "version 1 commit"`, etc.)
* Create the application on Heroku by adding a Git remote (`$ heroku create`)
* Push your code to the new Heroku repo (`$ git push heroku master`)
