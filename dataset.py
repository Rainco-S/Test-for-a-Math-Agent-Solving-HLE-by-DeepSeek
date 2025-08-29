from datasets import load_dataset
import os

SAVE_FOLDER = "/Users/DELL/PycharmProjects/try/HLE"  # change this to your own path
MAX_SAVE = None  # save every problems

def save_math_problems():
    os.makedirs(SAVE_FOLDER, exist_ok=True)

    dataset = load_dataset("cais/hle", split="test")
    math_dataset = dataset.filter(lambda example: example["category"] == "Math")
    total_count = math_dataset.num_rows

    # number to save
    save_count = total_count if MAX_SAVE is None else min(MAX_SAVE, total_count)

    # save problems to path
    for i in range(save_count):
        sample = math_dataset[i]
        # set names
        filename = f"problem{str(i+1).zfill(4)}.txt"
        file_path = os.path.join(SAVE_FOLDER, filename)

        # write in file content to fit format
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"*** Problem Statement ***\n\n")
            f.write(sample["question"])

        if (i + 1) % 10 == 0:  # show the progress every ten problems
            print(f"已保存 {i + 1}/{save_count} 个问题")


if __name__ == "__main__":
    save_math_problems()