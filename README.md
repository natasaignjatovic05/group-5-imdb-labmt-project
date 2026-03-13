# Inferring Happiness in IMDb Reviews with labMT

For Mini Project 1, see [mini_project_1.md](mini_project_1.md).

## Overview

This project uses the IMDb Large Movie Review Dataset to study how lexicon based happiness varies across review rating bands. We score each review using the labMT lexicon, compare low, medium, and high rated reviews, and estimate uncertainty around these differences. Our goal is not to treat the lexicon as emotional truth, but to test how well it works as a measurement instrument on a new corpus.

## Research Question

How does labMT based happiness vary across IMDb rating bands, and how certain are these differences?

## AI Use Disclosure

This project used ChatGPT for limited support with workflow planning, debugging, and drafting. All code, results, and interpretive claims were checked by the group. We remain responsible for the contents of this repository.

## Credits

| Member | Role |
|--------|------|
| Ricardo/Jack | Repo & workflow lead |
| Ricardo | Data acquisition lead |
| Jack/Andy | Measurement lead |
| Amber/Alessia | Stats & sampling lead |
| Natasha | Visualisation lead |

## Corpus and Provenance

## Methods

### Rating bands

We grouped IMDb reviews into three rating bands using the original numeric `rating` field:

- **low**: ratings 1 to 4
- **medium**: ratings 5 to 6
- **high**: ratings 7 to 10

This grouping gives us a meaningful metadata variable for comparison and supports sampling and inference across review groups.

## Results

## Critical Reflection

## How to Run
