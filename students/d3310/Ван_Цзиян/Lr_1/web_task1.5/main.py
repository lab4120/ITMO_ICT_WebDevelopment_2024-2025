import socket
from urllib.parse import parse_qs

# Store subjects and grades
grades = {}

def handle_request(request):
    method, path, _ = request.split(' ', 2)

    if method == 'POST' and path == '/submit':
        # Handle POST request
        body = request.split('\r\n\r\n')[1]
        data = parse_qs(body)

        # Extract subject and grade
        subject = data.get('subject', [''])[0]
        grade = data.get('grade', [''])[0]

        # Save information
        if subject and grade:
            grades[subject] = grade

        # Return response
        response = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n'
        response += '<html><body><h1>Data has been successfully saved!</h1>'
        response += '<a href="/grades">View all grades</a><br>'
        response += '<a href="/">Go back</a></body></html>'
        return response

    elif method == 'GET' and path == '/grades':
        # Handle GET request
        response = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n'
        response += '<html><body><h1>Subjects and Grades</h1>'
        response += '<table border="1">'
        response += '<tr><th>Subject</th><th>Grade</th></tr>'

        for subject, grade in grades.items():
            response += f'<tr><td>{subject}</td><td>{grade}</td></tr>'

        response += '</table><br>'
        response += '<a href="/">Go back</a>'
        response += '</body></html>'
        return response

    elif method == 'GET' and path == '/':
        # Return form page
        response = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n'
        response += '<html><body>'
        response += '<h1>Submit Grade Form</h1>'
        response += '<form method="POST" action="/submit">'
        response += 'Subject: <input type="text" name="subject" required><br>'
        response += 'Grade: <input type="text" name="grade" required><br>'
        response += '<input type="submit" value="Submit">'
        response += '</form></body></html>'
        return response

    else:
        # Handle other requests
        response = 'HTTP/1.1 404 NOT FOUND\r\nContent-Type: text/html\r\n\r\n'
        response += '<html><body><h1>Page Not Found</h1></body></html>'
        return response

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 8081))
    server_socket.listen(5)

    print("Server is running, access it at http://127.0.0.1:8081/ ")

    while True:
        client_socket, address = server_socket.accept()
        print(f'Connection from {address}')

        request = client_socket.recv(1024).decode('utf-8')
        print(f'Received request:\n{request}')

        response = handle_request(request)
        client_socket.sendall(response.encode('utf-8'))

        client_socket.close()

if __name__ == "__main__":
    start_server()