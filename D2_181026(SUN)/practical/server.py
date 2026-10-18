from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlsplit
import json


employees = {
    101: {
        "id": 101,
        "name": "Amit",
        "department": "IT",
        "salary": 55000
    },
    102: {
        "id": 102,
        "name": "Priya",
        "department": "HR",
        "salary": 48000
    }
}

next_employee_id = 103

REQUIRED_FIELDS = {"name", "department", "salary"}
ALLOWED_FIELDS = REQUIRED_FIELDS


class APIHandler(BaseHTTPRequestHandler):

    def send_json(self, data, status_code=200, extra_headers=None):
        response = json.dumps(data).encode("utf-8")

        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response)))

        if extra_headers:
            for name, value in extra_headers.items():
                self.send_header(name, value)

        self.end_headers()
        self.wfile.write(response)

    def send_no_content(self):
        self.send_response(204)
        self.send_header("Content-Length", "0")
        self.end_headers()

    def send_error_json(self, message, status_code):
        self.send_json({"error": message}, status_code)

    def get_resource(self):
        path = urlsplit(self.path).path
        parts = path.strip("/").split("/")

        if parts == ["employees"]:
            return "collection", None

        if len(parts) == 2 and parts[0] == "employees":
            if parts[1].isdigit():
                return "employee", int(parts[1])

        return "unknown", None

    def read_json(self):
        content_type = self.headers.get("Content-Type", "")

        if content_type.split(";")[0].strip().lower() != "application/json":
            self.send_error_json(
                "Content-Type must be application/json",
                415
            )
            return None

        try:
            length = int(self.headers.get("Content-Length", "0"))

            if length <= 0 or length > 1_000_000:
                self.send_error_json(
                    "Request body must contain 1 to 1000000 bytes",
                    400
                )
                return None

            raw_body = self.rfile.read(length)
            data = json.loads(raw_body.decode("utf-8"))

        except (ValueError, UnicodeDecodeError, json.JSONDecodeError):
            self.send_error_json("Invalid JSON request body", 400)
            return None

        if not isinstance(data, dict):
            self.send_error_json(
                "Request body must be a JSON object",
                400
            )
            return None

        return data

    def validate_employee(self, data, partial=False):
        fields = set(data)

        if not partial and fields != REQUIRED_FIELDS:
            return (
                "Employee must contain exactly: "
                "name, department, salary"
            )

        if partial and (
            not fields or not fields.issubset(ALLOWED_FIELDS)
        ):
            return "PATCH requires one or more valid employee fields"

        if "name" in data:
            if not isinstance(data["name"], str) or not data["name"].strip():
                return "name must be a non-empty string"

        if "department" in data:
            if (
                not isinstance(data["department"], str)
                or not data["department"].strip()
            ):
                return "department must be a non-empty string"

        if "salary" in data:
            salary = data["salary"]

            if (
                isinstance(salary, bool)
                or not isinstance(salary, (int, float))
                or salary < 0
            ):
                return "salary must be a non-negative number"

        return None

    def do_GET(self):
        resource, employee_id = self.get_resource()

        if resource == "collection":
            self.send_json(list(employees.values()))

        elif resource == "employee":
            employee = employees.get(employee_id)

            if employee is None:
                self.send_error_json("Employee not found", 404)
            else:
                self.send_json(employee)

        else:
            self.send_error_json("Endpoint not found", 404)

    def do_POST(self):
        global next_employee_id

        resource, _ = self.get_resource()

        if resource == "employee":
            self.send_response(405)
            self.send_header("Allow", "GET, PUT, PATCH, DELETE")
            self.send_header("Content-Length", "0")
            self.end_headers()
            return

        if resource != "collection":
            self.send_error_json("Endpoint not found", 404)
            return

        data = self.read_json()

        if data is None:
            return

        error = self.validate_employee(data)

        if error:
            self.send_error_json(error, 400)
            return

        employee_id = next_employee_id
        next_employee_id += 1

        employee = {
            "id": employee_id,
            **data
        }

        employees[employee_id] = employee

        self.send_json(
            employee,
            201,
            {"Location": f"/employees/{employee_id}"}
        )

    def do_PUT(self):
        resource, employee_id = self.get_resource()

        if resource == "collection":
            self.send_response(405)
            self.send_header("Allow", "GET, POST")
            self.send_header("Content-Length", "0")
            self.end_headers()
            return

        if resource != "employee":
            self.send_error_json("Endpoint not found", 404)
            return

        if employee_id not in employees:
            self.send_error_json("Employee not found", 404)
            return

        data = self.read_json()

        if data is None:
            return

        error = self.validate_employee(data)

        if error:
            self.send_error_json(error, 400)
            return

        employee = {
            "id": employee_id,
            **data
        }

        employees[employee_id] = employee
        self.send_json(employee)

    def do_PATCH(self):
        resource, employee_id = self.get_resource()

        if resource == "collection":
            self.send_response(405)
            self.send_header("Allow", "GET, POST")
            self.send_header("Content-Length", "0")
            self.end_headers()
            return

        if resource != "employee":
            self.send_error_json("Endpoint not found", 404)
            return

        if employee_id not in employees:
            self.send_error_json("Employee not found", 404)
            return

        data = self.read_json()

        if data is None:
            return

        error = self.validate_employee(data, partial=True)

        if error:
            self.send_error_json(error, 400)
            return

        employees[employee_id].update(data)
        self.send_json(employees[employee_id])

    def do_DELETE(self):
        resource, employee_id = self.get_resource()

        if resource == "collection":
            self.send_response(405)
            self.send_header("Allow", "GET, POST")
            self.send_header("Content-Length", "0")
            self.end_headers()
            return

        if resource != "employee":
            self.send_error_json("Endpoint not found", 404)
            return

        if employee_id not in employees:
            self.send_error_json("Employee not found", 404)
            return

        del employees[employee_id]
        self.send_no_content()


if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 8000

    server = HTTPServer((HOST, PORT), APIHandler)

    print(f"Server running at http://{HOST}:{PORT}")

    try:
        server.serve_forever()

    except KeyboardInterrupt:
        print("\nStopping server...")

    finally:
        server.server_close()
        print("Server stopped successfully.")