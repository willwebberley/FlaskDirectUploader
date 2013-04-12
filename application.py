from flask import Flask, render_template, request
import time, os, json, base64, hmac, sha

app = Flask(__name__)

@app.route("/")
def home():
		return render_template('home.html')

@app.route('/sign_s3/')
def sign_s3():
    AWS_ACCESS_KEY = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    S3_BUCKET = myCoolBucket
    
    object_name = request.args.get('s3_object_name')
    mime_type = request.args.get('s3_object_type')
 
    expires = int(time.time()+400)
    amz_headers = "x-amz-acl:public-read"
 
    put_request = "PUT\n\n%s\n%d\n%s\n/%s/%s" % (mime_type, expires, amz_headers, S3_BUCKET, object_name)
     
    signature = base64.encodestring(hmac.new(AWS_SECRET, put_request, sha).digest())

    url = 'https://%s.s3.amazonaws.com/%s' % (S3_BUCKET, object_name)
    
    return json.dumps({
            'signed_request': '%s?AWSAccessKeyId=%s&Expires=%d&Signature=%s' % (url, AWS_ACCESS_KEY, expires, signature),
            'url': url
        })
    
# Main code
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
