student_schema = {
    'title': 'students',
    'type': 'object',
    'required': ['name', 'major', 'gpa'],
    'properties': {
        'name': {
            'type': 'string'
        },
        'major': {
            'type': 'string'
        },
        'gpa': {
            'type': 'number'
        }
    }
}

student = {
    'name': 'John Doe',
    'major': 'Computer Science',
    'gpa': 3.75
}
