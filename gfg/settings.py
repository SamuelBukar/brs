# Email settings (remove if not needed)
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'your_email@example.com'
# EMAIL_HOST_PASSWORD = 'your_app_specific_password'

INSTALLED_APPS = [
    # ...existing code...
    'recommendation',
    'book_recommendation',  # Add this line
]

STATICFILES_DIRS = [
    BASE_DIR / "static",  # Main static folder
]
