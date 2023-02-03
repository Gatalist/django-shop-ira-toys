CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'kama',
        'toolbar_Basic': [['Source', '-', 'Bold', 'Italic']],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 
                     'items': ['Source', '-', 'Save', '-', '-', 'Templates']},
            {'name': 'clipboard', 
                     'items': ['Cut', '-', 'Copy', '-', 'Paste', '-', 'PasteText', '-', 'PasteFromWord', '-', 'Undo', '-', 'Redo']},
            {'name': 'editing', 'items': ['Find', '-', 'Replace', '-', 'SelectAll']},
            {'name': 'basicstyles',
                     'items': ['Bold', '-', 'Italic', '-', 'Underline', '-', 'Strike', '-', 'Subscript', '-', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
                     'items': ['NumberedList', '-', 'BulletedList', '-', 'Outdent', '-', 'Indent', '-', 'Blockquote', '-', 'CreateDiv', '-',
                               'JustifyLeft', '-', 'JustifyCenter', '-', 'JustifyRight', '-', 'JustifyBlock', '-', 'BidiLtr', '-', 'BidiRtl',]},
            {'name': 'links', 'items': ['Link', '-', 'Unlink',]},
            {'name': 'insert',
                     'items': ['Image', '-', 'Youtube', '-', 'Table', '-', 'HorizontalRule', '-', 'Smiley', '-', 'SpecialChar',]},
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['ShowBlocks']},
        ],
        'toolbar': 'YourCustomToolbarConfig',
        'width': '100%',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage',
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
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
