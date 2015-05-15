####
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
####


from flask import Flask, render_template, request, redirect, Response, url_for
import time, os, json, base64, hmac, urllib
from hashlib import sha1

app = Flask(__name__)

# Listen for GET requests to yourdomain.com/account/
@app.route("/account/")
def account():
    # Show the account-edit HTML page:
    return render_template('account.html')


# Listen for POST requests to yourdomain.com/submit_form/
@app.route("/submit_form/", methods=["POST"])
def submit_form():
    # Collect the data posted from the HTML form in account.html:
    username = request.form["username"]
    full_name = request.form["full_name"]
    avatar_url = request.form["avatar_url"]

    # Provide some procedure for storing the new details
    update_account(username, full_name, avatar_url)
    
    # Redirect to the user's profile page, if appropriate
    return redirect(url_for('profile'))


# Listen for GET requests to yourdomain.com/sign_s3/
#
# Please see https://gist.github.com/RyanBalfanz/f07d827a4818fda0db81 for an example using
# Python 3 for this view.
@app.route('/sign_s3/')
def sign_s3():
    # Load necessary information into the application:
    AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    S3_BUCKET = os.environ.get('S3_BUCKET')

    # Collect information on the file from the GET parameters of the request:
    object_name = urllib.quote_plus(request.args.get('file_name'))
    mime_type = request.args.get('file_type')

    # Set the expiry time of the signature (in seconds) and declare the permissions of the file to be uploaded
    expires = int(time.time()+60*60*24)
    amz_headers = "x-amz-acl:public-read"
 
    # Generate the StringToSign:
    string_to_sign = "PUT\n\n%s\n%d\n%s\n/%s/%s" % (mime_type, expires, amz_headers, S3_BUCKET, object_name)

    # Generate the signature with which the StringToSign can be signed:
    signature = base64.encodestring(hmac.new(AWS_SECRET_KEY, string_to_sign.encode('utf8'), sha1).digest())
    # Remove surrounding whitespace and quote special characters:
    signature = urllib.quote_plus(signature.strip())

    # Build the URL of the file in anticipation of its imminent upload:
    url = 'https://%s.s3.amazonaws.com/%s' % (S3_BUCKET, object_name)

    
    content = json.dumps({
        'signed_request': '%s?AWSAccessKeyId=%s&Expires=%s&Signature=%s' % (url, AWS_ACCESS_KEY, expires, signature),
        'url': url,
    })
   
    return content
    
# Main code
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    
