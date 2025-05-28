
# Django Signals are a powerful feature that allows you to attach custom logic to certain events or actions that occur in your Django application.
# Signals provide a way to allow decoupled applications to get notified when certain actions occur elsewhere in the application.

# Understanding Django Signals
# Signals are essentially notifications sent by Django when certain actions happen, such as when a model is saved or deleted. 
# They allow you to execute additional logic automatically when these actions occur.

# Key Concepts
# Signal: A signal is an event that occurs in your application. For example, a signal could be sent when a model instance is saved or deleted.

# Sender: The sender is the specific model or instance that triggers the signal.

# Receiver: A receiver is a function that responds to a signal. It is connected to the signal and will execute when the signal is sent.

# Signal Dispatch: This is the process of sending out the signal and notifying all connected receivers.

# Common Django Signals
# Django provides several built-in signals that you can use:

# 1. pre_save: Sent before a model’s save method is called.
# 2. post_save: Sent after a model’s save method is called.
# 3. pre_delete: Sent before a model’s delete method is called.
# 4. post_delete: Sent after a model’s delete method is called.
# 5. m2m_changed: Sent when a many-to-many relationship is changed.
# 6. request_started: Sent when a request is started.
# 7. request_finished: Sent when a request is finished.

# How to Use Django Signals
# Here’s a step-by-step guide to using Django signals in your project.

# 1. Define a Signal Receiver
# First, define a receiver function that will handle the signal.

# Example:


from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import MyModel

@receiver(post_save, sender=MyModel)
def my_model_post_save(sender, instance, created, **kwargs):
    if created:
        # Send an email after a new instance is created
        send_mail(
            'New Instance Created',
            f'A new instance of {sender.__name__} has been created.',
            'from@example.com',
            ['to@example.com'],
            fail_silently=False,
        )
        
# In this example, my_model_post_save is a receiver function that sends an email whenever a new instance of MyModel is created.

# 2. Connect the Receiver to the Signal
# You can connect the receiver to the signal using the @receiver decorator as shown above, or by using the signal.connect() method.

# Example:


from django.db.models.signals import post_save
from .models import MyModel

def my_model_post_save(sender, instance, created, **kwargs):
    if created:
        # Your logic here
        pass

post_save.connect(my_model_post_save, sender=MyModel)


# 3. Ensure Signal Handlers are Loaded
# Make sure your signal handlers are loaded. Typically, you include them in your app’s apps.py or models.py file. 
# For example, you can import the signals in the ready method of the AppConfig:

# Example:


# apps.py

from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'myapp'

    def ready(self):
        import myapp.signals
        
        
# In this example, myapp.signals would be a module where you define your signal handlers.

# 4. Testing Signals
# You can test signals using Django’s test framework.

# Example:


from django.test import TestCase
from django.db.models.signals import post_save
from .models import MyModel

class MyModelTestCase(TestCase):
    def setUp(self):
        # Connect to the signal
        self.signals_received = []

        def signal_receiver(sender, **kwargs):
            self.signals_received.append(sender)

        post_save.connect(signal_receiver, sender=MyModel)

    def test_signal_on_create(self):
        # Create a new instance and check if the signal was received
        MyModel.objects.create(name='Test')
        self.assertEqual(len(self.signals_received), 1)
        self.assertEqual(self.signals_received[0], MyModel)
        
# Advanced Usage
# 1. Using Custom Signals
# You can also create custom signals if the built-in ones don't meet your needs.

# Example:

from django.db.models.signals import Signal

# Define a custom signal
my_custom_signal = Signal()

def my_custom_receiver(sender, **kwargs):
    print('Custom signal received')

# Connect the receiver to the custom signal
my_custom_signal.connect(my_custom_receiver)

# Send the signal
my_custom_signal.send(sender='my_sender')

# 2. Avoiding Circular Imports
# When working with signals, be careful about circular imports. It's often a good idea to import your signal handlers inside the ready method 
# of the AppConfig to avoid this issue.

# Summary

# Signals: Allow you to attach custom logic to events like model saves and deletes.
# Common Signals: Django provides built-in signals like post_save, pre_delete, and m2m_changed.
# Receiver Functions: Define functions to handle signals and connect them using decorators or signal.connect().
# Ensure Loading: Import your signal handlers in the ready method of AppConfig to ensure they are loaded.
# Testing: Use Django’s testing framework to verify your signal handling.
# By using Django signals, you can make your application more modular and responsive to changes, allowing for more flexible and maintainable code.