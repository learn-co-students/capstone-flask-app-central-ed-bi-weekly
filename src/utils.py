def validate_input(data):
    """
    Prepare raw values from HTML form for making ML prediction

    Parameters:
        data: ImmutableDict of data from the HTML form, representing features

    Returns:
        test_value: a list floating point numbers representing feature values.
        The HTML form is assumed to have numeric inputs.  Additional
        preprocessing may be required if the form contains categorical or text data

        errors: a list of strings representing error messages (which should be
        empty if the form data was valid)
    """
    test_value = []
    errors = []
    
    EXPECTED_FEATURES = ["sepal-length", "sepal-width", "petal-length", "petal-width"]
    
    if not data:
        errors.append("Form data must not be empty")
    else:
        for feature in EXPECTED_FEATURES:
            if feature not in data:
                errors.append(f"'{feature}' is a required field")
            else:
                try:
                    test_value.append(float(data[feature]))
                except ValueError:
                    errors.append(f"Invalid value for field {feature}: '{data[feature]}'")

    return test_value, errors


    
