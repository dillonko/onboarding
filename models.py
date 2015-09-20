class OnboardingError(Exception):
    pass

class OnboardingInfo(object):
    def __init__(self, form):
        self.validate(form)
        for key, value in form.items():
            setattr(self, key, value)

    def validate(self, form):
        required_fields = [
            'firstname',
            'lastname',
            'youremail',
            'drop1',
            'title',
            'drop2',
            'startdate',
            'password',
            'need_pc',
            'pc_type',
            'portable',
            'notes',
        ]

        for field in required_fields:
            value = form.get(field)
            if value is None:
                raise OnboardingError("Missing field {}".format(field))
        return True
