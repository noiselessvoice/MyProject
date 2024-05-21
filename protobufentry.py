import example_pb2

def read_protobuf_entry(serialized_data):
    # Deserialize the binary string to an ExampleMessage instance
    deserialized_message = example_pb2.ExampleMessage()
    deserialized_message.ParseFromString(serialized_data)
    
    # Extract specific fields from the deserialized message
    id_field = deserialized_message.id
    name_field = deserialized_message.name
    email_field = deserialized_message.email

    # Print extracted fields
    print(f"ID: {id_field}")
    print(f"Name: {name_field}")
    print(f"Email: {email_field}")
    
    # Return the extracted fields as a dictionary
    return {
        "id": id_field,
        "name": name_field,
        "email": email_field
    }

if __name__ == "__main__":
    # Example serialized data (this would typically come from an external source)
    example_message = example_pb2.ExampleMessage(id=123, name="John Doe", email="john.doe@example.com")
    serialized_data = example_message.SerializeToString()
    
    # Read the protobuf entry
    read_protobuf_entry(serialized_data)
