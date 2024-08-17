import pandas as pd

def predict_relevance(document):
    # To ensure that 'Content' is a string
    content = document.get("Content", "")

    # Key Relevant Rule: A document is relevant if it contains certain keywords
    keywords = ["Dollar", "ATS", "Payment Transactions", "Condominium", "Gambling", "Lotteries", "Procurement",
                "Securities and Exchange", "Central Bank", "Assets", "Capital","Treasury", "Exchange"]

    if isinstance(content, str):
        content_lower = content.lower()
        for keyword in keywords:
            if keyword.lower() in content_lower:
                return True
    return False

def label_documents(missing_regulations):
    # This ensures that the DataFrame is a copy, so as to avoid SettingWithCopyWarning
    missing_regulations = missing_regulations.copy()

    # Apply the function and explicitly cast to boolean
    missing_regulations["ContainsRelevantRegulation"] = missing_regulations.apply(
        lambda row: predict_relevance(row), axis=1
    ).astype(bool)

    return missing_regulations[["DocumentID", "ContainsRelevantRegulation"]]

if __name__ == "__main__":
    # Read the used files
    regulations_df = pd.read_csv("C:/Users/oluwa/DATA SCIENCE/Data Science & ML/AI Engineering Mentorship/regulations.csv")
    relevance_data_df = pd.read_csv("C:/Users/oluwa/DATA SCIENCE/Data Science & ML/AI Engineering Mentorship/relevance_data.csv")
    missing_regulations = pd.read_csv("C:/Users/oluwa/Downloads/missing_regulations.csv")


    labeled_df = label_documents(missing_regulations)
    labeled_df.to_csv("C:/Users/oluwa/Downloads/predictions.csv", index=False)
