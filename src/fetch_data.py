from pathlib import Path
import pandas as pd


def parse_filename(filename: str) -> tuple[int, int]:
    """Extract review ID and rating from a filename like '200_8.txt'."""
    stem = filename.replace(".txt", "")
    review_id_str, rating_str = stem.split("_")
    return int(review_id_str), int(rating_str)


def load_reviews(base_dir: Path, split: str, sentiment: str) -> list[dict]:
    """Load all reviews from one folder like train/pos or test/neg."""
    folder = base_dir / split / sentiment
    rows = []

    for file_path in folder.glob("*.txt"):
        review_id, rating = parse_filename(file_path.name)

        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read().strip()

        rows.append(
            {
                "review_id": review_id,
                "rating": rating,
                "sentiment": sentiment,
                "split": split,
                "word_count": len(text.split()),
                "text": text,
            }
        )

    return rows


def main() -> None:
    raw_root = Path("data/raw/aclImdb")
    output_path = Path("data/processed/imdb_reviews.csv")

    all_rows = []

    for split in ["train", "test"]:
        for sentiment in ["pos", "neg"]:
            rows = load_reviews(raw_root, split, sentiment)
            all_rows.extend(rows)

    df = pd.DataFrame(all_rows)
    df = df.sort_values(by=["split", "sentiment", "review_id"]).reset_index(drop=True)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False, encoding="utf-8")

    print(f"Saved {len(df)} reviews to {output_path}")


if __name__ == "__main__":
    main()

    