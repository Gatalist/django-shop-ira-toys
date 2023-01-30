CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
    'default': {
        # 'skin': 'moono-lisa',
        'skin': 'kama',
        # 'skin': 'moono',
        # 'skin': 'office2013',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 
                        'items': ['Source', '-', 'Save', '-', '-', 'Templates']},
           
            {'name': 'clipboard', 
                        'items': ['Cut', '-', 'Copy', '-', 'Paste', '-', 'PasteText', '-', 'PasteFromWord', '-', 'Undo', '-', 'Redo']},
            
            {'name': 'editing', 
                        'items': ['Find', '-', 'Replace', '-', 'SelectAll']},

            # {'name': 'forms',
            #             'items': ['Checkbox', '-', 'Radio', '-', 'TextField', '-', 'Textarea', '-', 'Select', '-', 'Button',]},
            # '/',
            {'name': 'basicstyles',
                        'items': ['Bold', '-', 'Italic', '-', 'Underline', '-', 'Strike', '-', 'Subscript', '-', 'Superscript', '-', 'RemoveFormat']},

            {'name': 'paragraph',
                        'items': ['NumberedList', '-', 'BulletedList', '-', 'Outdent', '-', 'Indent', '-', 'Blockquote', '-', 'CreateDiv', '-',
                                  'JustifyLeft', '-', 'JustifyCenter', '-', 'JustifyRight', '-', 'JustifyBlock', '-', 'BidiLtr', '-', 'BidiRtl',]},

            {'name': 'links', 
                        'items': ['Link', '-', 'Unlink',]},

            {'name': 'insert',
                        'items': ['Image', '-', 'Youtube', '-', 'Table', '-', 'HorizontalRule', '-', 'Smiley', '-', 'SpecialChar',]},
            
            {'name': 'styles', 
                        'items': ['Styles', 'Format', 'Font', 'FontSize']},

            {'name': 'colors', 
                        'items': ['TextColor', 'BGColor']},

            {'name': 'tools', 
                        'items': ['ShowBlocks']},
        ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
        'width': '100%',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage', # the upload image feature
            # your extra plugins here
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            # 'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath',
            'youtube'
        ]),
    }
}
