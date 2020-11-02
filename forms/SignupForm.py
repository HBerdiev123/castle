from allauth.account.forms import SignupForm
from profiles.models import Profile

class MyCustomSignupForm(SignupForm):

	def save(self, request):
		user = super(MyCustomSignupForm, self).save(request)
		# cusomized allauth form
		profile = Profile.objects.create(user=user)
		return user