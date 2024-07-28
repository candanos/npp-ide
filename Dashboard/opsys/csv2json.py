# csv2json converter
import pandas as pd
import json
csv_file = r'C:\Users\A488466\Desktop\MF_files_for_integrations.csv'
json_file = r'C:\Users\A488466\Desktop\MF_files_for_integrations.json'
df = pd.read_csv(csv_file)

nested_json = df.groupby('Message Name').apply(lambda x: x.to_dict(orient='records'), include_groups=False).to_json()

# formatted json
json_object = json.loads(nested_json)
json_str = json.dumps(json_object, indent=4)

# unformatted_json
json_str = nested_json

file = open(json_file, "w")
file.write(json_str)
file.close()


# convert to json
# The orient='records' parameter structures the JSON data as a list of records, and lines=True formats the output with each record on a separate line.
# json_data = df.to_json(orient='records', lines=True)
# print(json_data)

# FILTERING

# columns: You can select specific columns and convert them to JSON by specifying the columns:

# selected_columns = df[['User_ID', 'Plan_Type']]
# selected_json = selected_columns.to_json(orient='records', lines=True)
# print(selected_json)

# Convert Specific Rows
# You can convert only specific rows from your CSV data to JSON by filtering the rows based on the conditions you want:
# Selecting specific rows based on a condition
# specific_rows = df[df['Call_Duration'] > 400]
# specific_rows_json = specific_rows.to_json(orient='records', lines=True)
# print(specific_rows_json)

# Grouping data by 'Plan_Type' and converting each group to JSON
# specific_rows = df[df['Message Name'] == 'T659B2']
# json_str = json.dumps(json.loads(specific_rows.to_json()), indent=4)
# print(json_str)

# df = specific_rows
# nested_json = df.groupby('Message Name').apply(lambda x: x.to_dict(orient='records'), include_groups=False).to_json()

# Load the JSON string into a Python object
# json_object = json.loads(nested_json)

# Format and indent the JSON data
# formatted_json = json.dumps(json_object, indent=4)
# print(formatted_json)

