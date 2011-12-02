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
    FOLLOWUP = u'Contactează-ne la <a href="mailto:webdev@rosedu.org">webdev.rosedu.org</a> :)'

    SUBMIT = 'Vreau!'

class StudentConfig(BaseConfig):
    SIGNUP_FILE = 'signup_students.yaml'
    LINES = ['HTML',
             'CSS',
             'JavaScript',
             'MVC',
             'Securitate',
             'REST',
             'Caching',
             u'Scaling',
             'Deployment',
             'Analytics']
    COLS = [u'Știu', u'Învăț']

class InstructorConfig(StudentConfig):
    SIGNUP_FILE = 'signup_instructors.yaml'
    COLS = copy.deepcopy(StudentConfig.COLS)
    COLS.append(u'Predau')
    CONTACT = copy.deepcopy(StudentConfig.CONTACT)
    CONTACT.update({'phone' : u'Număr de telefon:'})

class DateTimeConfig(BaseConfig):
    SIGNUP_FILE = 'signup_date.yaml'
    GREETING = 'Analytics 2'
    LINES = [u'5 decembrie (Luni)',
             u'6 decembrie (Marți)',
             u'10 decembrie (Sâmbătă)']
    COLS = ['16', '18', '20']
