# -*- coding: utf-8 -*-
import copy
# Regman's config module

class BaseConfig(object):
    # Store registered users and prefereneces here; could be a DB later?
    SIGNUP_FILE = None

    # Greeting banner
    GREETING = u""" Workshop-uri ținute de oameni tineri și deschiși care lucrează
în domeniul web."""

    # Lines and columns for matrix of checkboxes
    # Can be workshop wishlist, date&time, volunteering form
    LINES = None
    COLS = None

    # Profile for an attendant as well as contact info
    PROFILES = {'Elev' : [u'Școală', u'Clasă'],
                'Student' : ['Facultate', 'An'],
                'Angajat' : ['Companie', u'Funcție']}
    CONTACT = {'email' : u'Adresă de e-mail:'}

    # Follow up message
    FOLLOWUP = u'Contactează-ne la <a href="mailto:webdev@rosedu.org">webdev.'
    'rosedu.org</a> :)'

    SUBMIT = 'Vreau!'

class StudentConfig(BaseConfig):
    SIGNUP_FILE = 'signup_students.yaml'
    LINES = [('html' , 'HTML'),
             ('css' , 'CSS'),
             ('javascript' , 'JavaScript'),
             ('mvc' , 'MVC'),
             ('securitate' , 'Securitate'),
             ('rest' , 'REST'),
             ('caching' , 'Caching'),
             ('scaling' , 'Scaling'),
             ('deployment', 'Deployment'),
             ('analytics' , 'Analytics')]
    COLS = [('stiu' , u'Știu'),
            ('invat' , u'Învăț')]

class InstructorConfig(StudentConfig):
    SIGNUP_FILE = 'signup_instructors.yaml'
    COLS = [('stiu' , u'Știu'),
            ('predau' , u'Predau')]
    CONTACT = copy.deepcopy(StudentConfig.CONTACT)
    CONTACT.update({'phone' : u'Număr de telefon:'})

class DateTimeConfig(BaseConfig):
    SIGNUP_FILE = 'signup_date.yaml'
    GREETING = 'Analytics 2'
    LINES = [('data-12-5' , u'5 decembrie (Luni)'),
             ('data-12-6' , u'6 decembrie (Marți)'),
             ('data-12-10' , u'10 decembrie (Sâmbătă)')]
    COLS = [('ora-16' , '16'),
            ('ora-18' , '18'),
            ('ora-20' , '20')]
