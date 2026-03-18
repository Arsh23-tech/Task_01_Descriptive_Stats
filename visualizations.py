import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = "fb_ads_president_scored_anon.csv"

# Load dataset
df = pd.read_csv(DATA_FILE)

print("Dataset Loaded:", df.shape)

# ------------------------------------------------
# Helper function to safely select columns
# ------------------------------------------------

def get_columns(keyword):
    return [col for col in df.columns if keyword in col.lower()]


# ------------------------------------------------
# 1. Message Type Distribution
# ------------------------------------------------

message_cols = get_columns("msg_type")

if message_cols:
    message_counts = df[message_cols].sum()

    plt.figure(figsize=(12,6))

    message_counts.plot(kind="bar")

    plt.title("Distribution of Political Message Types")
    plt.xlabel("Message Type")
    plt.ylabel("Number of Ads")

    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    plt.savefig("Output/message_type_distribution.png")
    plt.show()

else:
    print("No message type columns found.")


# ------------------------------------------------
# 2. Political Topics
# ------------------------------------------------

topic_cols = get_columns("topic")

if topic_cols:
    topic_counts = df[topic_cols].sum().sort_values(ascending=False)

    clean_topics = [col.replace("illuminating_topic_", "") for col in topic_counts.index]
    
    plt.figure(figsize=(14,6))
    plt.bar(clean_topics, topic_counts)
    plt.xticks(rotation=90)
    plt.title("Political Topics in Ads") 
    plt.ylabel("Number of Ads")

    plt.tight_layout()

    plt.savefig("Output/top_topics.png")
    plt.show()

else:
    print("No topic columns found.")


# ------------------------------------------------
# 3. Incivility Analysis
# ------------------------------------------------

incivility_cols = [col for col in df.columns if "incivility" in col.lower()]

if incivility_cols:

    incivility_data = df[incivility_cols[0]]

    # Replace 0 and 1 with descriptive labels
    incivility_labels = incivility_data.replace({
        0: "Civil Ads",
        1: "Incivil Ads"
    })

    incivility_counts = incivility_labels.value_counts()

    plt.figure(figsize=(6,6))

    incivility_counts.plot(
        kind="pie",
        autopct="%1.1f%%"
    )

    plt.title("Incivility in Political Advertisements")

    plt.ylabel("")
    plt.tight_layout()

    plt.savefig("Output/incivility_rate.png")
    plt.show()

else:
    print("No incivility column found.")