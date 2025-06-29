import pandas as pd
import ast
import os

LABEL_MAP = {
    "0": "O",
    "1": "B-Product",
    "2": "I-Product",
    "3": "B-LOC",
    "4": "I-LOC",
    "5": "B-PRICE",
    "6": "I-PRICE",
}

def manual_labeling_interface(df, output_path, per_channel_limit=10):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    labeled_lines = []
    message_counter = 0
    unique_channels = df["Channel Username"].unique()

    for channel in unique_channels:
        subset = df[df["Channel Username"] == channel].dropna(subset=["Message"])
        if len(subset) < per_channel_limit:
            continue
        sampled = subset.sample(n=per_channel_limit, random_state=42)

        for _, row in sampled.iterrows():
            try:
                tokens = ast.literal_eval(row["Message"])
            except Exception as e:
                print(f"Skipping row: {e}")
                continue

            print("\n" + "="*50)
            print(f"📨 Full Message from {channel}:")
            print(" ".join(tokens))
            print("="*50)

            labels = []
            for i, token in enumerate(tokens):
                print(f"\nToken {i+1}/{len(tokens)}: \033[1m{token}\033[0m")
                print("Choose label:")
                for k, v in LABEL_MAP.items():
                    print(f"  {k}: {v}")
                print("  n: skip message, q: quit")

                choice = input("Your choice: ").strip()
                if choice == "q":
                    print("👋 Exiting and saving progress...")
                    with open(output_path, "w", encoding="utf-8") as f:
                        f.write("\n".join(labeled_lines))
                    print(f"✅ Labeled data saved to {output_path}")
                    return
                elif choice == "n":
                    print("⏭️ Skipping message...")
                    labels = []
                    break
                elif choice in LABEL_MAP:
                    labels.append(LABEL_MAP[choice])
                else:
                    print("⚠️ Invalid input, defaulting to 'O'")
                    labels.append("O")

            if labels:
                for tok, lab in zip(tokens, labels):
                    labeled_lines.append(f"{tok}\t{lab}")
                labeled_lines.append("")  # Separate messages

                message_counter += 1
                if message_counter % 5 == 0:
                    with open(output_path, "w", encoding="utf-8") as f:
                        f.write("\n".join(labeled_lines))
                    print(f"💾 Auto-saved progress after {message_counter} messages.")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(labeled_lines))
    print(f"✅ Saved labeled data to {output_path}")

if __name__ == "__main__":
    df = pd.read_csv("../data/processed/preprocessed_messages.csv")
    df.columns = df.columns.str.strip()
    output_file = "../data/conll/labeled_data.txt"
    manual_labeling_interface(df, output_file, per_channel_limit=10)