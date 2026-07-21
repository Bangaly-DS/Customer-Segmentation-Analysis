import pandas as pd

def preprocess_input(
        salary,
        clv,
        enrollment_year,
        enrollment_month,
        gender,
        education,
        marital_status,
        loyalty_card,
        enrollment_type,
        feature_columns
):
    """
    Preprocess customer input into the format expected by the trained K-Means model.
    """
    # Initialize all features to 0
    input_data = {column: 0 for column in feature_columns}

    # Numerical features
    input_data["Salary"] = salary
    input_data["CLV"] = clv
    input_data["Enrollment Year"] = enrollment_year
    input_data["Enrollment Month"] = enrollment_month

    # Categorical features
    categorical_features = {
        "Gender": gender,
        "Education": education,
        "Marital Status": marital_status,
        "Loyalty Card": loyalty_card,
        "Enrollment Type": enrollment_type
    }
    
    # Recreate one-hot encoding
    for feature, value in categorical_features.items():
        column_name = f"{feature}_{value}"

        if column_name in input_data:
            input_data[column_name] = 1

    input_df = pd.DataFrame([input_data])
    return input_df
