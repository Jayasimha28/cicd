import boto3

ses = boto3.client('ses')

body = """
Hello, This is from Lambda, implemented by Jay

Thanks & Regards,
Jayasimha
"""

ses.sendemail_email(
	Source = 'jayasimha.cherlopalli@cognizant.com',
	Destination={
		'ToAddresses': [
			'jayasimha.cherlopalli@cognizant.com',
			'Barkha.Singh@cognizant.com'
		]
	},
	Message={
		'Subject':{
			'Data' : 'SES DEMO By Lambda',
			'Charset' : 'UFT-8'
		},
		'Body'={
			'Data' : body,
			'Charset' : 'UFT-8'
		}
	}
)