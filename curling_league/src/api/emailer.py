import yagmail


class Emailer:
    _sole_instance = None
    sender_address = None

    @classmethod
    def instance(cls):
        if cls._sole_instance is None:
            cls._sole_instance = cls()
        return cls._sole_instance

    @classmethod
    def configure(cls, prop):
        cls.sender_address = prop

    # send_plain_email(recipients, subject, message) -- Note: this is an instance method.
    def send_plain_email(self, recipients, subject, message):
        yag = yagmail.SMTP(self.sender_address)
        for recipient in recipients:
            yag.send(recipient, subject, message)

