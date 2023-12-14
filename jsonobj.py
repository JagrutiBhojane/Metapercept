# Create JSON object any detail
# E.g. EmployeeData = {{fname:”abc”, lname:”xyz”, id: 1}, {fname:”abc”, lname:”xyz”, id: 2}}
# Apply CURD operation on that JSON Data.
import json
EmployeeData ={'fname':"abc", 'lname':"xyz", id: 1}#, {'fname':"abc", 'lname':"xyz", id: 2}
json_data=json.dumps(EmployeeData)
print(json_data)