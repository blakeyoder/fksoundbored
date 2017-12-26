import os
from flask import render_template, jsonify
from fksoundbored import app
import boto3


@app.route('/')
def index():

    data = get_data()
    return render_template('index.html', data=data)


@app.route('/api')
def api():
    return jsonify(get_data())


def get_data():
    BUCKET = 'fksoundbored'

    client = boto3.client('s3',
            aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
            aws_session_token=os.environ.get('AWS_SESSION_TOKEN'))
    all_obj = client.list_objects(Bucket=BUCKET)['Contents']

    data = []
    for obj in all_obj:
        meta_data = client.get_object(
                Bucket=BUCKET,
                Key=obj['Key']
                )

        obj_dict = {}
        obj_dict['name'] = meta_data['Metadata']['name']
        obj_dict['url'] = "https://s3.amazonaws.com/{}/{}".format(BUCKET, obj['Key'])
        data.append(obj_dict)

    return data
