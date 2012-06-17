from feedback.forms import ContactForm
from django.http import HttpResponse
import json
import time
from django.core.mail import send_mail

def validate(request):
	if request.POST:
		time.sleep(0.5)
		form = ContactForm(request.POST)

		if form.is_valid():
			subject = 'Omnihead Web Site'
			message = 'from: %s \n\n message: %s \n' % (form.cleaned_data['author'], form.cleaned_data['message'])
			frm = 'mail@omnihead.ru'
			to = ['igor.lifar@omnihead.ru', 'customers@omnihead.ru']

			print subject, message, frm, to

			try:
				send_mail('Omnihead Web Site', 'Here is the message.', 'from@example.com', ['igor.lifar@gmail.com'], fail_silently=False)
			except:
				pass

		return HttpResponse(json.dumps({
			'errors': dict(form.errors)
		}))
	return HttpResponse('fuck')