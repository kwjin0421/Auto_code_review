import pylint.lint

def analyze_code(file_content):
    results = []
    pylint_opts = ['--disable=C0114,C0115,C0116']  # Disable docstring warnings
    runner = pylint.lint.Run(pylint_opts + [file_content], exit=False)
    for message in runner.linter.reporter.messages:
        results.append({
            'type': message.msg_id,
            'line': message.line,
            'message': message.msg
        })
    return results