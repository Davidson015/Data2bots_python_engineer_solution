import sys, json

def create_schema(data: dict) -> dict:
  '''
    Returns a dictionary synonymous JSON Schema

      `data` --> the already parsed JSON data

    Creates a Schema object ready to be parsed as JSON.
  '''
  
  refined_data = {}

  # Getting the list of attribute keys in the "message" attr
  key_list = list(data["message"].keys())

  # Getting the message attribute data
  message_data = dict(data["message"])

  for index, value in enumerate(message_data):

    # Determining the type of attribute
    value_type = type(message_data[value])

    if value_type == int:
      type_of_attr = "number"
    elif value_type == str:
      type_of_attr = "string"
    elif value_type == bool:
      type_of_attr = "boolean"
    elif value_type == dict:
      type_of_attr = "array"
    elif value_type == list:
      type_of_attr = "enum"
    else:
      type_of_attr = "null"

    # Creating and populating each attribute schema object
    data = {
      'type': type_of_attr,
      'tag': "",
      'description': "",
      'required': "false"
    }

    # Populating the "refined_data" dictionary
    refined_data[f"{key_list[index]}"] = data

  return refined_data

def main():

  data_file = sys.argv[1]
  schema = data_file.replace("data", "schema")
  
  with open(data_file) as input, open(schema, "w") as output:
    # Reading json data from the data file
    data = json.load(input)
  
    # Getting rid of the "attributes" key
    data.pop("attributes")

    # Creating a new schema object
    data_schema = create_schema(data)

    # Writing to the Schema file
    json.dump(data_schema, output, indent=4)
    
    print("Done.")


if __name__ == "__main__":
  main()
