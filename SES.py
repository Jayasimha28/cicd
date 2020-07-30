import boto3

ses = boto3.client('ses')

body = """
Hello, This is from Lambda, implemented by Jay
Thanks & Regards,
Jayasimha
"""

ses.send_email(
	Source = 'cherlopallijayasimha@gmail.com',
	Destination={
		'ToAddresses': [
			# 'jayasimha.cherlopalli@cognizant.com',
            'cherlopallijayasimha@gmail.com'
			# 'Barkha.Singh@cognizant.com'
		]
	},
	Message={
		'Subject':{
			'Data' : 'SES DEMO By Lambda',
			'Charset' : 'UTF-8'
		},
		'Body':{
            'Text':{
                'Data' : body,
                'Charset' : 'UTF-8'
            }
        }
	}
)
