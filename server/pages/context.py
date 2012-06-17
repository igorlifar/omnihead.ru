from feedback.forms import ContactForm

def get_context(s, request):
	l = len(s)
	c = {}
	
	if l == 1 and s[0] == 'index':
		c['css'] = 'index.css'
		c['js'] = 'index.js'
		c['form'] = ContactForm()
		
	return c