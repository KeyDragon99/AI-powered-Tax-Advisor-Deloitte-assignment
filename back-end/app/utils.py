def generate_prompt(tax_data, comments):
    tax_data_str = "\n".join([f"{k}: {v}" for k, v in tax_data.items()])
    if comments:
        return (
            f"Here is the user's tax-related data:\n{tax_data_str}\n\n"
            f"The user has also shared the following comments:\n{comments}\n\n"
            "Based on this information, please provide personalized suggestions and advice regarding their taxes."
        )
    return (
        f"Here is the user's tax-related data:\n{tax_data_str}\n\n"
        "Based on this information, please provide personalized suggestions and advice regarding their taxes."
    )
