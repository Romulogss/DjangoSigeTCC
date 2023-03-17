import os

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
PROJECT_ROOT = os.path.abspath(os.path.dirname(BASE_DIR))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p)5iv&k!+j4+s0ll6l=wx$l8rz1^uhkx*_8u@kb7)19v-vc(v5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

DEFAULT_DATABASE_URL = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # djangosige apps:
    'djangosige.apps.base',
    'djangosige.apps.login',
    'djangosige.apps.cadastro',
    'djangosige.apps.vendas',
    'djangosige.apps.compras',
    'djangosige.apps.fiscal',
    'djangosige.apps.financeiro',
    'djangosige.apps.estoque',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Middleware para paginas que exigem login
    'djangosige.middleware.LoginRequiredMiddleware',
]

ROOT_URLCONF = 'djangosige.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # contexto para a versao do sige
                'djangosige.apps.base.context_version.sige_version',
                # contexto para a foto de perfil do usuario
                'djangosige.apps.login.context_user.foto_usuario',
            ],
        },
    },
]

WSGI_APPLICATION = 'djangosige.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'pt-br'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]


FIXTURE_DIRS = [
    os.path.join(BASE_DIR, 'fixtures'),
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = 'media/'

SESSION_EXPIRE_AT_BROWSER_CLOSE = False

LOGIN_NOT_REQUIRED = (
    r'^/login/$',
    r'/login/esqueceu/',
    r'/login/trocarsenha/',
    r'/logout/',
)
