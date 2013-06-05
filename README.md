FlaskDirectUploader
===================

Direct-to-S3 uploads in a Python application running on Heroku
-----------------------------------------------------------------------------

Simple example demonstrating how to accomplish a direct upload to Amazon S3 in a Python web application.

The example focuses on Flask as the web framework and is targeted for use on the Heroku platform. However, nearly all of the code could be used as-is in other Python frameworks (such as Bottle and Django).

This is the companion repository to the Heroku article, [Direct to S3 File Uploads in Python](https://devcenter.heroku.com/articles/s3-upload-python).

This code is mostly ready to be run as cloned, but a function `update_account()` will need to be defined to handle the storing of the POSTed information.

**Running the application**
* Set environment variables for your AWS access key and secret
* Download and install the [Heroku toolbelt](https://toolbelt.heroku.com/)
* Run with ```$ foreman start```

**Deploying the application (see **

