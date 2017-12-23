import os
from flask import render_template
from fksoundbored import app
import boto3


@app.route('/')
def index():
    BUCKET = 'fksoundbored'
    print('here')
    print(os.environ)

    client = boto3.client('s3',
            aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'))
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

    return render_template('index.html', data=data)
